from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tile, Comment
from .forms import *
from accounts.forms import LoginForm

def index(request):
    tiles = Tile.objects.all()
    comments = Comment.objects.all()
    return render(request, "tiles.html", {
        "tiles": tiles,
        "CategoryForm": CategoryForm,
        "TileForm": TileForm,
        "LoginForm": LoginForm,
        "comments": comments
    })

@login_required
def add_tile(request):
    tile = TileForm(request.POST)
    tile.save()
    return redirect("index")

@login_required
def add_category(request):
    category = CategoryForm(request.POST)
    category.save()
    return redirect("index")

@login_required
def add_comment(request):
    data = {
        "description": request.POST.get("description", None),
        "tile": get_object_or_404(Tile, pk=request.POST.get("tile", None)),
        "owner": request.user
    }
    comment = Comment(**data)
    comment.save()
    return redirect("index")
