from django.conf.urls import url
from . import views
app_name = 'recipe'
from recipe import views as v

urlpatterns = [
    # /recipe/
    url(r'^$', views.ListView.as_view(), name='home'),
    # /recipe/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /recipe/detail/
    url(r'^(?P<title>[\w.@+-]+)/$', views.DetailView.as_view(), name='detail'),
    # /recipe/recipes/add/
    url(r'^recipes/create/$', v.create_recipe, name='create-recipe'),
    # /recipe/recipes/pk/
    url(r'^(?P<title>[\w.@+-]+)/$', views.RecipeUpdate.as_view(), name='update-recipe'),
    # /recipe/recipes/pk/delete/
    url(r'^recipes/(?P<title>[\w.@+-]+)/delete/$', views.RecipeDelete.as_view(), name='delete-recipe'),
]