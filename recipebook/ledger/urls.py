from django.urls import path

from .views import home, recipe1, recipe2

urlpatterns = [
    path('recipes/list', home, name='home'),
    path('recipe/1', recipe1, name='Recipe 1'),
    path('recipe/2', recipe2, name='Recipe 2')
]

app_name = "ledger"