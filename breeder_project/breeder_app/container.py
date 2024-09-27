from dependency_injector.providers import Configuration, Factory
from dependency_injector.containers import DeclarativeContainer

from .protocols.repositories import CatRepository as CatRepoProtocol
from .repositories import CatRepository

from typing import Self


class Container(DeclarativeContainer):
    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    config = Configuration()

    cat_repository: CatRepoProtocol = Factory(CatRepository)
