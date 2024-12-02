from typing import List

from app.models.domain.searched_artists import SearchedArtist


class SearchedAlbum:
    AlbumID: str
    Title: str
    Artwork: str
    AlbumType: str
    Year: int
    Artists: List[SearchedArtist]
