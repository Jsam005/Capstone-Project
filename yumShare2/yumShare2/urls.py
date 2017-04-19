"""yumShare2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from recipe.views import recipe_view, create_recipe, update_recipe, delete_recipe, recipe_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recipe/(?P<pk>\d+)$', recipe_view, name='recipe_page'),
    url(r'^recipes/all', recipe_list, name='recipe_list'),
    url(r'^recipes/create_recipe', create_recipe, name='recipe_form'),
    url(r'^recipes/update/(?P<pk>\d+)$', update_recipe, name='update_page'),
    url(r'^recipes/delete/(?P<pk>\d+)$', delete_recipe, name='delete_page'),
]
