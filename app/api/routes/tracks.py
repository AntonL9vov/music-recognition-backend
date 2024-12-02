from typing import List

import requests
from fastapi import APIRouter

from app.models.schemas.search import ExploreInResponse, SearchInResponse

router = APIRouter()

OPEN_MUSIC_BASE_URL = 'https://server.openmusic.app'


@router.get('/explore')
def explore():
    res = requests.get(f'{OPEN_MUSIC_BASE_URL}/explore')
    tracks: ExploreInResponse = res.json()
    return tracks


@router.get('/search')
def search(q: str):
    res = requests.get(f'{OPEN_MUSIC_BASE_URL}/search?q={q}')
    search_res: SearchInResponse = res.json()
    return search_res
