from django import forms
from . import models

class AddProduct(forms.ModelForm):
    class Meta:
     model=models.Product
     fields=['product','Quantity','rate','description','image']