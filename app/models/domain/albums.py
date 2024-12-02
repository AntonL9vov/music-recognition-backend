from typing import List

from app.models.domain.searched_artists import SearchedArtist
from app.models.domain.tracks import FetchedTrack


class FetchedAlbum:
    AlbumID: str
    Title: str
    Artwork: str
    AlbumType: str
    Year: int
    Artists: List[SearchedArtist]
    Tracks: List[FetchedTrack]
    Features: List[SearchedArtist]
