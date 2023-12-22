
from django import forms

class Product(forms.Form):
    name = forms.CharField(max_length=20)
    quantity = forms.IntegerField()
