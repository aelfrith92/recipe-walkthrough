from django.urls import path
from .views import AddRecipe, Recipes


urlpatterns = [
    path('', AddRecipe.as_view(), name='create_recipe'),
    path('recipes/', Recipes.as_view(), name='recipes'),
]