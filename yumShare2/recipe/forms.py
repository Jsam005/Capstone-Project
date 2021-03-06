from .models import RecipeInfo, Ingredient, Direction, Comment
from django.forms.models import inlineformset_factory, ModelForm

class RecipeForm(ModelForm):
    class Meta:
        model = RecipeInfo
        fields = ['title', 'category']

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ()

class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        exclude = ()

IngredientFormSet = inlineformset_factory(RecipeInfo, Ingredient, form=IngredientForm, extra=1)
DirectionFormSet = inlineformset_factory(RecipeInfo, Direction, form=DirectionForm, extra=1)