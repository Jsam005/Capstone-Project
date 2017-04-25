from django.contrib import admin
from .models import RecipeInfo, Comment, Ingredient, Direction

# Register your models here.

admin.site.register(RecipeInfo)
admin.site.register(Ingredient)
admin.site.register(Direction)
admin.site.register(Comment)
