from dataclasses import dataclass, asdict
from typing import TypedDict
from .models import Breeder


class CatKeys(TypedDict):
    breed: str
    country: str
    weight: int
    height: float
    lifetime_from: int
    lifetime_to: int
    name: str
    age: int
    photo_link: str
    breeder: Breeder
    id: int | None = None
