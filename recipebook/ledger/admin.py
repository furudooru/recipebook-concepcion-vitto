from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ['image', 'description', 'recipe']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)