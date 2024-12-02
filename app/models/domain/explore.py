from typing import List

from app.models.domain.searched_albums import SearchedAlbum


class ExploreShelf:
    Title: str
    Albums: List[SearchedAlbum]
