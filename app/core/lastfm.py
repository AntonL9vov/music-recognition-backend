import pylast

from app.core.settings.app import AppSettings


def get_last_fm_network(settings: AppSettings):
    network = pylast.LastFMNetwork(
        api_key=settings.LAST_FM_API_KEY,
        api_secret=settings.LAST_FM_API_SECRET,
        username=settings.LAST_FM_LOGIN,
        password_hash=pylast.md5(settings.LAST_FM_PASSWORD),
    )

    return network
