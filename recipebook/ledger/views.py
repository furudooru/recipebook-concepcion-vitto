from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Recipe, Ingredient, RecipeIngredient
# Create your views here.
class HomeListView(ListView):
    model = Recipe
    template_name = 'home.html'
    
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'

