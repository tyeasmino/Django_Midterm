from django.contrib.auth.models import User
from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from .models import PlaceOrderModel

class CarUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs= {'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    

class CarUserUpdateInfofForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    

class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = PlaceOrderModel
        fields = '__all__'
