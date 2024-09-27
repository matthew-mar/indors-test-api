from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from typing import Callable
from .models import Cat


class IsCatBreeder(BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: Callable,
        obj: Cat
    ) -> bool:
        if request.method == "POST":
            return True
        return obj.breeder == request.user
