import os

import pylast

API_KEY = "5e320382722f151f92454b1b89f10aa8"  # this is a sample key
API_SECRET = "e65234efea5d396b565fdf260dc7d937"


def get_lastfm_network():
    SESSION_KEY_FILE = os.path.join(os.path.expanduser("~"), ".session_key")
    lastfm_network = pylast.LastFMNetwork(API_KEY, API_SECRET)
    if not os.path.exists(SESSION_KEY_FILE):
        skg = pylast.SessionKeyGenerator(lastfm_network)
        url = skg.get_web_auth_url()

        print(f"Please authorize this script to access your account: {url}\n")
        import time
        import webbrowser

        webbrowser.open(url)

        while True:
            try:
                session_key = skg.get_web_auth_session_key(url)
                with open(SESSION_KEY_FILE, "w") as f:
                    f.write(session_key)
                break
            except pylast.WSError:
                time.sleep(1)
    else:
        session_key = open(SESSION_KEY_FILE).read()

    lastfm_network.session_key = session_key

    return lastfm_network
