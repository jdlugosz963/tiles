from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('add_tile/', add_tile, name="add_tile"),
    path('add_category/', add_category, name="add_category")
]
