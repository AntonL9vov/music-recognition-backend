from typing import Optional, List

from app.models.domain.searched_albums import SearchedAlbum
from app.models.domain.searched_artists import SearchedArtist


class FetchedTrack:
    TrackID: str
    Title: str
    Playback_Clean: Optional[str]
    Playback_Explicit: Optional[str]
    Length: int
    Index: int
    Views: int
    Album: SearchedAlbum
    Features: List[SearchedArtist]


class ImportedTrack:
    TrackID: str
    Title: str
    Playback_Clean: Optional[str]
    Playback_Explicit: Optional[str]
    Length: int
    Index: int
    Views: int
    Album: SearchedAlbum
    Features: List[SearchedArtist]
    titleScore: float
    albumScore: float
    artistScore: float


class PlaylistTrack:
    title: str
    album: str
    artists: str
