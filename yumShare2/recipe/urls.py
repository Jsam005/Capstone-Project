from django.conf.urls import url
from . import views
from recipe import views as v
app_name = 'recipe'

urlpatterns = [
    # /recipe/
    url(r'^$', v.home, name='home'),
    # /recipe/title/
    #url(r'^recipe/(?P<slug>[-\W]+)/$', views.RecipeDetailView.as_view(), name='detail'),
    url(r'^recipe/(?P<title>[-\w]+)/$', views.RecipeDetailView, name='detail'),
    # /recipe/list/
    url(r'^recipe/list/$', views.RecipeListView.as_view(), name='list-recipe'),
    # /recipe/create/
    url(r'^recipe/create/$', views.RecipeCreateView.as_view(), name='create-recipe'),
    # /recipe/title/
    url(r'^recipe/(?P<title>[\w-]+)/update/$', views.RecipeUpdateView.as_view(), name='update-recipe'),
    # /recipe/recipes/title/delete/
    url(r'^recipe/(?P<title>[\w.@+-]+)/delete/$', views.RecipeDelete.as_view(), name='delete-recipe'),
    url(r'^recipe/search/(?P<word>[\w.@+-]+)/', views.search_bar_view, name='search-bar'),
]