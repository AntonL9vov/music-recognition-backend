from typing import List

import requests
from fastapi import APIRouter

from app.models.domain.tracks import PopularTracks, PopularTracksPeriods

router = APIRouter()


@router.get('/popular')
def get_popular_tracks(page: int = 1, limit: int = 50, period: PopularTracksPeriods = 'day'):
    res = requests.get(
        f'https://zaycev.net/api/external/pages/index/top?page={page}&limit={limit}&period={period}&entity=track')
    tracks: List[PopularTracks] = res.json()
    return tracks
