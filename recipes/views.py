from typing import Any, Optional
from django.db.models.query import QuerySet
from django.views.generic import (CreateView, 
                                  ListView, 
                                  DetailView, 
                                  DeleteView,
                                  UpdateView
                                  )

# Q is a SQL wrapper that allows us to
# complex database operations in a user-friendly way
from django.db.models import Q

from django.contrib.auth.mixins import (UserPassesTestMixin, 
                                        LoginRequiredMixin
                                        )

from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    """View all recipes"""

    template_name = "recipes/recipes.html"
    model = Recipe
    # Throwing from the back-end to the front-end
    # The ListView automatically generates the list of
    # all recipes, as a result of the model declared above
    # These will be available in the context, through the name
    # given below to the context_object_name, recipes.
    context_object_name = "recipes"
    print('prima della funzione')
    
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(cuisine_types__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class RecipeDetail(DetailView):
    """View a specific recipe"""

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    # Throwing from the back-end to the front-end
    # this time one single recipe is available in the context
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """Create a new recipe"""

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update a recipe"""
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"
    
    def test_func(self):
        # reads like: Is the person making the request
        # the owner of the recipe?
        recipe = self.get_object()
        return self.request.user == recipe.user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = Recipe
    success_url = "/recipes/"
    template_name = "recipes/recipe_confirm_delete.html"
    
    def test_func(self):
        # reads like: Is the person making the request
        # the owner of the recipe?
        recipe = self.get_object()
        return self.request.user == recipe.user