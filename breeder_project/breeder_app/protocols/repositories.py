from typing import Protocol
from ..dto import CatKeys
from ..models import Cat


class CatRepository(Protocol):
    def create(self, cat: CatKeys) -> Cat:
        ...

    def update_by_model(self, cat: Cat, to_update: CatKeys) -> Cat:
        ...
