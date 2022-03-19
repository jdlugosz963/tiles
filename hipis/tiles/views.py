from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tile
from .forms import *
from accounts.forms import LoginForm

def index(request):
    tiles = Tile.objects.all()
    return render(request, "tiles.html", {
        "tiles": tiles,
        "CategoryForm": CategoryForm,
        "TileForm": TileForm,
        "LoginForm": LoginForm
    })

@login_required
def add_tile(request):
    tile = TileForm(request.POST)
    tile.save()
    return redirect("index")

def add_category(request):
    category = CategoryForm(request.POST)
    category.save()
    return redirect("index")
