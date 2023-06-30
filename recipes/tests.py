from django.test import TestCase
from django.urls import reverse # dado o nome da url, retorna a url completa


# Create your tests here.
class RecipeURLsTest(TestCase):
    ''' Testa urls da aplicação '''
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipes_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1}) # Passando argumentos com dict
        self.assertEqual(url, '/recipes/category/1/')
        
    def test_recipes_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', args=(1,)) # Passando argumentos com tupla
        self.assertEqual(url, '/recipes/1/')
