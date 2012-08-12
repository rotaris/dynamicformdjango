from models import * # Change as necessary
from django.forms import ModelForm

class ListForm(ModelForm):
    """A form for a todo list"""
    class Meta:
        model = List

class ItemForm(ModelForm):
    """A form for todo item"""
    class Meta:
        model = Item
        exclude = ('list',)
