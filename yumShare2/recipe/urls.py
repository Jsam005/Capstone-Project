from django.conf.urls import url
from . import views
from recipe import views as v
app_name = 'recipe'

urlpatterns = [
    # /recipe/
    url(r'^$', v.home, name='home'),
    # /recipe/detail/
    url(r'recipe/^(?P<title>[\w.@+-]+)/$', views.DetailView.as_view(), name='detail'),
    # /recipe/recipes/list/
    url(r'^recipe/list/$', views.ListView.as_view(), name='list-recipe'),
    # /recipe/recipes/create/
    # url(r'^recipes/create/$', v.create_recipe, name='create-recipe'),
    url(r'^recipe/create/$', views.RecipeCreateView.as_view(), name='create-recipe'),
    # /recipe/recipes/title/
    url(r'^recipe/(?P<title>[\w.@+-]+)/$', views.RecipeUpdateView.as_view(), name='update-recipe'),
    # /recipe/recipes/title/delete/
    url(r'^recipe/(?P<title>[\w.@+-]+)/delete/$', views.RecipeDelete.as_view(), name='delete-recipe'),
]