from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.mixins import (
    RetrieveModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
)

from .serializers import CatSerializer
from .permissions import IsCatBreeder
from .models import Cat


class CatPaginator(LimitOffsetPagination):
    default_limit = 3
    offset = 1


class CatsViews(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated, IsCatBreeder]
    pagination_class = CatPaginator

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)
    
    def post(self, requset: Request, *args, **kwargs) -> Response:
        return self.create(requset, *args, **kwargs)
    

class CatViews(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView
):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated, IsCatBreeder]
    lookup_field = "id"

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request: Request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)
