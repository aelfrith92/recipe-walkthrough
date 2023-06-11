from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    """ View all recipes """
    template_name = 'recipes/recipes.html'
    model = Recipe
    # Throwing from the back-end to the front-end
    # The ListView automatically generates the list of
    # all recipes, as a result of the model declared above
    # These will be available in the context, through the name
    # given below to the context_object_name, recipes.
    context_object_name = 'recipes'

class AddRecipe(LoginRequiredMixin, CreateView):
    """ Create a new recipe """

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)