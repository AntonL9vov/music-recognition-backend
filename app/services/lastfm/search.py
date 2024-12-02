from app.main import lastfm_network


def get_track_lastfm(artist: str, title: str):
    return lastfm_network.get_track(artist, title)


def get_similar_tracks(artist: str, title: str):
    track = get_track_lastfm(artist, title)
    return track.get_similar()
