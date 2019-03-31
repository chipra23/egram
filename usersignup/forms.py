from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=False,help_text='optional')
    mobile=PhoneNumberField(help_text='compulsory')
    Locality=forms.CharField(max_length=100,help_text='compulsory')
    District=forms.CharField(max_length=50,help_text='compulsary')
    State=forms.CharField(max_length=50,help_text='compulsary')
    pincode=forms.IntegerField(help_text='compulsary')
  
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile', 'email','Locality','District','State','pincode', 'password1', 'password2', )