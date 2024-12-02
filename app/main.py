# import requests
# import json
#
# from app.core.init.init import getFastApi
# from app.core.networks.get_lastfm_network import get_lastfm_network
#
# app = getFastApi()
#
# lastfm_network = get_lastfm_network()
#
# def get_track(title: str, artist: str):
#     response = requests.get(f'https://zaycev.net/api/external/pages/search?q={title}+{artist}')
#     return response.json()
#
#
# def get_filezmeta(trackIds: list[str]):
#     response = requests.post('https://zaycev.net/api/external/track/filezmeta', data=json.dumps({
#         "subscription": "false",
#         "trackIds": trackIds
#     }), headers={'Content-Type': 'application/json; charset=utf-8'})
#     return response.json()
#
#
# def get_streaming_url(id: str):
#     response = requests.get(f'https://zaycev.net/api/external/track/play/{id}')
#     return response.json()
#
#
# @app.get("/track")
# async def say_hello(title: str, artist: str):
#     print('Title Artist', title, artist)
#     track = network.get_track(artist, title)
#     print('Track', track)
#     similarTracks = track.get_similar()
#     print('similarTracks', track.get_similar())
#     # tracks = get_track(track.get_title(), track.get_artist())
#     # print('Tracks', tracks)
#     # filezmeta = get_filezmeta(tracks['tracks']['trackIds'])
#     # print('filezmeta', filezmeta)
#     # url = get_streaming_url(filezmeta['tracks'][0]['streaming'])
#     # print('url', url)
#     return similarTracks
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import get_app_settings
from app.api.routes.api import router as api_router

def get_application() -> FastAPI:
    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=settings.api_prefix)
    
    return application

app = get_application()