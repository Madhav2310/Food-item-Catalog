from django import forms
from .models import Item

class ItemForm(forms.ModelForm):   # itemform is a var
    class Meta:                 # stores fields
        model = Item
        fields = ['item_name', 'item_desc','item_price','item_image']
        
