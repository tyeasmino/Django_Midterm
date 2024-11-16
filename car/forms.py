from django import forms
from .models import CarBrandModel, CarModel, CommentModel

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrandModel
        fields = '__all__'
    

class CarDetailsForm(forms.ModelForm):
    class Meta: 
        model = CarModel
        fields = '__all__' 
    

class CommentsForm(forms.ModelForm):
    class Meta: 
        model = CommentModel
        fields = ['name', 'email', 'comment'] 