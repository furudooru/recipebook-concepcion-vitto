from django.urls import path
from .views import HomeListView, RecipeDetailView, RecipeCreateView, ImageCreateView

urlpatterns = [
    path('recipes/list', HomeListView.as_view(), name='home'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeCreateView.as_view(), name='create'),
    path('recipe/<int:pk>/add_image', ImageCreateView.as_view(), name='update')
]

app_name = "ledger"