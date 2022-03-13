from django import forms
from .models import Tile, Category

class TileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TileForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = key.capitalize()

    class Meta:
        model=Tile
        fields = ['name', 'description', 'category']


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = key.capitalize()

    class Meta:
        model=Category
        fields = '__all__'
