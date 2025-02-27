from django.views.generic import ListView, DetailView
from .models import Recipe


class HomeListView(ListView):
    model = Recipe
    template_name = 'home.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
