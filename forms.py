from .models import AddWare
from django import forms
from django.forms import ModelForm

class ImportWareForm(ModelForm):
    class Meta:
        model = AddWare
        fields = ['id', 'name', 'description', 'price', 'imported_quantity','image', 'imported', 'exported', 'warehouse_from', 'warehouse_loc', 'warehouse']