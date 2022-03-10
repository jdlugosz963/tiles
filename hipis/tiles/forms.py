from django import forms
from .models import Tile, Category

class TileForm(forms.ModelForm):
    class Meta:
        model=Tile
        fields = ['name', 'description', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'
