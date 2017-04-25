from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeInfo, Ingredient, Direction, Comment
from .forms import RecipeTitleForm, IngredientForm, DirectionForm, CommentForm

# Create your views here.

def detailed_view(request, title=None):
    recipe = get_object_or_404(RecipeInfo, title=title)
    ingredient = Ingredient.objects.get(recipe=recipe)
    direction = Direction.objects.get(recipe=recipe)
    comment = recipe.comment_set.all()
    template = "recipes.html"
    context = {
        'recipe': recipe,
        'comment': comment,
        'ingredient': ingredient,
        'direction': direction,
    }
    return render(request, template, context)

def create_recipe(request):
    # Lets the users create recipes, checks that the form is valid and saves the recipe

    if request.method == 'GET':
        form = RecipeTitleForm(data=request.POST)
        if form.is_valid():
            return redirect('/recipes/')

    context = {'form': form}
    return render(request, 'create_recipe.html', context)

def update_recipe(request):

    recipe = RecipeInfo.objects.get()

    if request.method == 'GET':
        form = RecipeTitleForm(instance=recipe)

    elif request.method == 'POST':
        form = RecipeTitleForm(instance=recipe, data=request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('/recipes/')

    context = {'form': form}
    return render(request, 'create_recipe.html', context)

def delete_recipe(request):

    recipe = RecipeInfo.objects.get()
    recipe.delete()                     # Delete step
    return redirect('/recipes')         # Success!

def recipe_list(request):
    # Generates a list of all recipes
    recipes = RecipeInfo.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes.html', context)

