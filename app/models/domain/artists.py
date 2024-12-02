from typing import List

from app.models.domain.searched_albums import SearchedAlbum
from app.models.domain.tracks import FetchedTrack


class FetchedArtist:
    ArtistID: str
    Name: str
    Profile_Photo: str
    Subscribers: int
    Albums: List[SearchedAlbum]
    Singles: List[SearchedAlbum]
    Tracks: List[FetchedTrack]
