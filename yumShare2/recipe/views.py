from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import RecipeInfo, Ingredient, Direction, Comment
from .forms import UserForm

# Create your views here.

class ListView(generic.ListView):
    template_name = 'recipe/home.html'

    def get_queryset(self):
        return RecipeInfo.objects.all()

class DetailView(generic.DetailView):
    model = RecipeInfo, Comment
    template_name = 'recipe/detail.html'

class CreateRecipe(CreateView):


#def create_recipe(request):
    # Lets the users create recipes, checks that the form is valid and saves the recipe

    #form = AddRecipeForm(request.POST or None)

    #context = {'form': form}
    #return render(request, 'recipe/create.html', context)

class RecipeUpdate(UpdateView):
    model = RecipeInfo
    fields = ['title', 'category']

class RecipeDelete(DeleteView):
    model = RecipeInfo
    success_url = reverse_lazy('recipe:home')

class UserFormView(View):
    form_class = UserForm
    template_name = 'recipe/registration_form.html'

    # display a new blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process the form data and validate it
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # storing the data locally but not actually saving it yet
            user = form.save(commit=False)

            # cleaned data - data that is formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # saves the user to the database
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('recipe:home')

        return render(request, self.template_name, {'form': form})

