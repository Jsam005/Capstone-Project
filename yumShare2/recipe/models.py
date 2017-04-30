from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class RecipeInfo(models.Model):
    title = models.CharField(max_length=50, editable=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=75, editable=True)
    quantity = models.FloatField(editable=True)
    measurement = models.CharField(max_length=10, editable=True)
    recipe = models.ForeignKey(RecipeInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient

class Direction(models.Model):
    directions = models.TextField(editable=True)
    cook_time_in_minutes = models.FloatField(editable=True)
    prep_time_in_minutes = models.FloatField(editable=True)
    recipe = models.ForeignKey(RecipeInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.directions


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    recipe = models.ForeignKey(RecipeInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

