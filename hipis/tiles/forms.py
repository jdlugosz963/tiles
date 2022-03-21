from django import forms
from .models import *

def set_default_styles(self):
    for key, value in self.fields.items():
        value.widget.attrs['placeholder'] = key.capitalize()
        value.widget.attrs['class'] = "bg-orange-600 p-2 m-2"
        value.label = ""

class TileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TileForm, self).__init__(*args, **kwargs)
        set_default_styles(self)

    class Meta:
        model=Tile
        fields = ['name', 'description', 'category']


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        set_default_styles(self)

    class Meta:
        model=Category
        fields = '__all__'

class CommentFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentFrom, self).__init__(*args, **kwargs)
        set_default_styles(self)

    class Meta:
        model=Comment
        fields = ("description", )
