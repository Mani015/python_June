
from django import forms
from AppOne.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
# Similar to ModelAdmin we can use the ModelForm class and make a form object linking to the fields defined under models.py


# __all__ includes all fields under the model class. You may alternatively use a tuple of field names.
