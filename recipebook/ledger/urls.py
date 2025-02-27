from django.urls import path

from .views import HomeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', HomeListView.as_view(), name='home'),
    path('recipe/<int:pk>', RecipeDetailView.as_view() , name='recipe'),
]

app_name = "ledger"