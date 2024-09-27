from .protocols.repositories import CatRepository
from .container import Container
from .dto import CatKeys
from .models import Cat

from dependency_injector.wiring import inject, Provide
from breeder_project.validators import string
from rest_framework.serializers import (
    CurrentUserDefault,
    IntegerField,
    HiddenField,
    FloatField,
    Serializer,
    CharField,
    URLField,
)

class CatSerializer(Serializer):
    id = IntegerField(required=False)
    breed = CharField(allow_blank=False, max_length=150, validators=[string])
    country = CharField(allow_blank=False, max_length=50, validators=[string])
    weight = IntegerField(max_value=50)
    height = FloatField(max_value=100)
    lifetime_from = IntegerField(min_value=1, max_value=10)
    lifetime_to = IntegerField(min_value=10, max_value=30)
    name = CharField(allow_blank=False, max_length=150, validators=[string])
    age = IntegerField(min_value=0)
    photo_link = URLField(allow_blank=True)
    breeder = HiddenField(default=CurrentUserDefault())

    @inject
    def create(
        self,
        validated_data: CatKeys,
        cat_repo: CatRepository = Provide[Container.cat_repository]
    ) -> Cat:
        return cat_repo.create(validated_data)
    
    @inject
    def update(
        self, 
        instance: Cat,
        validated_data: CatKeys,
        cat_repo: CatRepository = Provide[Container.cat_repository]
    ) -> Cat:
        return cat_repo.update_by_model(instance, validated_data)
