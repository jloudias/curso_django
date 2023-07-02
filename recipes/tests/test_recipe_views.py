from django.test import TestCase
from django.urls import reverse # dado o nome da url, retorna a url completa
from django.urls import resolve # dado um url, retorna a view a que se refere
from recipes import views


# Create your tests here.
class RecipeViewsTest(TestCase):
    ''' Testa urls da aplicação '''
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}) )
        self.assertIs(view.func, views.category)
        
    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,))) 
        self.assertIs(view.func, views.recipe)
