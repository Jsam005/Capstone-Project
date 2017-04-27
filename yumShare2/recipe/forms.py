from django.contrib.auth.models import User
from django import forms
from django.forms.models import inlineformset_factory
from .models import RecipeInfo, Ingredient, Direction, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeInfo
        fields = ['title', 'category']