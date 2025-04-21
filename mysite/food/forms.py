from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    # holds the informations what fields should be present in that form
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image'] 