from enum import Enum

from app.models.domain.genres import Genre
from typing import List, Optional


class TrackUser:
    id: int
    name: str


class TrackFullInfo:
    artistId: int
    artistName: str
    bigImageJpg: str
    bigImageWebp: str
    bitrate: int
    downloadEnabled: bool
    duration: str
    durationTime: int
    explicit: bool
    genres: List[Genre]
    id: str
    imageJpg: str
    imageWebp: str
    lyrics: List[str]
    notAvailable: bool
    playbackEnabled: bool
    possessorInfo: str
    possessors: List[str]
    size: float
    track: str
    user: TrackUser


class TrackInfo(TrackFullInfo):
    bigImageJpg = None
    bigImageWebp = None
    genres = None
    id = None
    lyrics = None
    notAvailable = None
    isArtistForeignAgent: bool
    possessorInfo = None
    possessors = None
    user = None


class PopularTracks:
    trackIds: List[int]
    limit: int
    page: int
    pagesCount: int
    tracksInfo: List[TrackInfo]


class PopularTracksPeriods(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
