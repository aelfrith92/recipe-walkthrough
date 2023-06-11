from django.urls import path
from .views import (AddRecipe, 
                    Recipes, 
                    RecipeDetail,
                    DeleteRecipe,
                    UpdateRecipe,
                    )


urlpatterns = [
    path("create/", AddRecipe.as_view(), name="create_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("edit/<int:pk>/", UpdateRecipe.as_view(), name="edit_recipe"),
    path("delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
]
