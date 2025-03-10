from django.db import models
from django.urls import reverse
from accounts.models import Profile


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("ledger:home", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='recipe')
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("ledger:recipe", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL,
                               null=True, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL,
                                   null=True, related_name='recipe')

    def __str__(self):
        return f'{self.recipe.name}: {self.ingredient.name}: {self.quantity}'