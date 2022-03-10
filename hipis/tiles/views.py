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
    tile = TileForm(request.POST)
    tile.save()
    return redirect("index")

def add_category(request):
    category = CategoryForm(request.POST)
    category.save()
    return redirect("index")
