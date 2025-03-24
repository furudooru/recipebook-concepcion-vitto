from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class ImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [ImageInLine,]
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)