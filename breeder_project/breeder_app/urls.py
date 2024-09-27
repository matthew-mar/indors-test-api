from .views import CatsViews, CatViews 
from django.urls import path

urlpatterns = [
    path("cats/", CatsViews.as_view()),
    path("cats/<int:id>/", CatViews.as_view()),
]
