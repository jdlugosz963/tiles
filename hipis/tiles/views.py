from django.shortcuts import render, redirect
from .models import Tile
from .forms import *

def index(request):
    tiles = Tile.objects.all()
    return render(request, "tiles.html", {
        "tiles": tiles,
        "CategoryForm": CategoryForm,
        "TileForm": TileForm
    })

def add_tile(request):
    tile = Tile.objects.create(**request.POST)
    tile.save()
    return redirect("index")

def add_category(request):
    category = Category.objects.create(**request.POST)
    category.save()
    return redirect("index")
