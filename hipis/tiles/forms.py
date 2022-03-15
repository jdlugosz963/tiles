from django import forms
from .models import Tile, Category

class TileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TileForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = key.capitalize()
            value.widget.attrs['class'] = "bg-orange-700 p-2 m-2"

    class Meta:
        model=Tile
        fields = ['name', 'description', 'category']


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = key.capitalize()
            value.widget.attrs['class'] = "bg-orange-700 p-2 m-2"

    class Meta:
        model=Category
        fields = '__all__'
