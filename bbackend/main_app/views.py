from django.shortcuts import render, get_object_or_404
from ninja import NinjaAPI
from typing import List

from django.shortcuts import get_list_or_404
from ninja import NinjaAPI
from ninja.security import django_auth

from . import models, schemas

api = NinjaAPI()


@api.get("/navigation/main", response=schemas.NavigationDisplay)
def get_main_display(request):
    return get_object_or_404(models.NavigationDisplay, deep=0)


@api.get("/navigation/{pk}", response=schemas.NavigationDisplay)
def get_navigation(request, pk: int):
    return get_object_or_404(models.NavigationDisplay, pk=pk)


@api.get("/content", response=List[schemas.Content])
def get_answers(request, category_id: int):
    return get_list_or_404(models.Content, category_id=category_id)

