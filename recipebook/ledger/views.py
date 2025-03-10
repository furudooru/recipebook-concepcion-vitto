from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


class HomeListView(ListView):
    model = Recipe
    template_name = 'home.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = 'login.html'
