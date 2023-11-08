from django import forms
from .models import *

class contact_form(forms.Form):
    email = forms.EmailField(widget= forms.TextInput)
    tittle = forms.CharField(widget= forms.TextInput)
    text = forms.CharField(widget= forms.Textarea)

class add_product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['name',  'price', 'stock', 'categories', 'marca','image', 'description'] #'_all_'
        