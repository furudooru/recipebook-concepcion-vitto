from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class HomeListView(ListView):
    model = Recipe
    template_name = 'home.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = 'login.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'create.html'
    form_class = RecipeForm
    redirect_field_name = 'login.html'

    
    

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'add-image.html'
    form_class = RecipeImageForm
    redirect_field_name = 'login.html'
