
from django import forms


class Registration(forms.Form):
    Id = forms.IntegerField()
    Firstname = forms.CharField()
    Lastname = forms.CharField()
    Email = forms.CharField()
