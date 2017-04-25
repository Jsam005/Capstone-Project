from django import forms
from .models import RecipeInfo, Ingredient, Direction, Comment

class RecipeTitleForm(forms.ModelForm):
    class Meta:
        model = RecipeInfo
        fields = ['title', 'category']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient', 'quantity', 'measurement']

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['directions', 'cook_time_in_minutes', 'prep_time_in_minutes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']