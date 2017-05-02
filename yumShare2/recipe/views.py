from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import RecipeInfo, Ingredient, Direction, Comment
from .forms import IngredientFormSet, DirectionFormSet

# Create your views here.

def home(request):
    context = {}
    return render(request, 'recipe/home.html', context)

class ListView(generic.ListView):
    template_name = 'recipe/recipeinfo_list.html'

    def get_queryset(self):
        return RecipeInfo.objects.all()

class DetailView(generic.DetailView):
    model = RecipeInfo, Comment
    template_name = 'recipe/detail.html'

class RecipeCreateView(CreateView):
    model = RecipeInfo
    fields = ['title', 'category']
    success_url = reverse_lazy('recipe:list-recipe')

    def get_context_data(self, **kwargs):
        data = super(RecipeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST, prefix='ingredient')
            data['directions'] = DirectionFormSet(self.request.POST, prefix='direction')
        else:
            data['ingredients'] = IngredientFormSet(prefix='ingredient')
            data['directions'] = DirectionFormSet(prefix='direction')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        directions = context['directions']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()
            if directions.is_valid():
                directions.instance = self.object
                directions.save()
        return super(RecipeCreateView, self).form_valid(form)


#def create_recipe(request):
    # Lets the users create recipes, checks that the form is valid and saves the recipe

    #form = AddRecipeForm(request.POST or None)

    #context = {'form': form}
    #return render(request, 'recipe/create.html', context)

class RecipeUpdateView(UpdateView):
    model = RecipeInfo
    form_class = IngredientFormSet, DirectionFormSet
    success_url = reverse_lazy('recipe:update-recipe')

    def get_object(self):
        pass


    def get_context_data(self, **kwargs):
        context = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ingredients'] = IngredientFormSet(self.request.POST, instance=self.object)
            context['directions'] = DirectionFormSet(self.request.POST, instance=self.object)
        else:
            context['ingredients'] = IngredientFormSet(instance=self.object)
            context['directions'] = DirectionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        directions = context['directions']
        if ingredients.is_valid() and directions.is_valid():
            self.object = form.save()
            ingredients.instance = self.object
            ingredients.save()
            directions.instance = self.object
            directions.save()
        return render(self.get_context_data(form=form))


class RecipeDelete(DeleteView):
    model = RecipeInfo
    success_url = reverse_lazy('recipe:list-recipe')
