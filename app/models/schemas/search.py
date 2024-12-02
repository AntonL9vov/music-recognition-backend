from typing import List

from pydantic.v1 import BaseModel

from app.models.domain.explore import ExploreShelf
from app.models.domain.searched_albums import SearchedAlbum
from app.models.domain.searched_artists import SearchedArtist
from app.models.domain.tracks import FetchedTrack, ImportedTrack


class SearchInResponse:
    Tracks: List[FetchedTrack]
    Albums: List[SearchedAlbum]
    Singles: List[SearchedAlbum]
    Artists: List[SearchedArtist]


class ExactInResponse:
    Tracks: List[ImportedTrack]


class ExploreInResponse:
    Shelves: List[ExploreShelf]


class QuickInResponse:
    Tracks: List[FetchedTrack]
