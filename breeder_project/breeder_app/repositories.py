from .protocols.repositories import CatRepository as CatRepoProtocol
from .dto import CatKeys
from .models import Cat


class CatRepository(CatRepoProtocol):
    def create(self, cat: CatKeys) -> Cat:
        return Cat.objects.create(**cat)

    def update_by_model(self, cat: Cat, to_update: CatKeys) -> Cat:
        for key, value in to_update.items():
            setattr(cat, key, value)
        cat.save()
        return cat
