from django.test import TestCase
from django.urls import reverse  # dado o nome da url, retorna a url completa
from django.urls import resolve  # dado um url, retorna a view a que se refere
from recipes import views
from recipes.models import Category, Recipe, User # como User foi importado em models.py, pode ser chamado por tabela
# from django.contrib.auth.models import User  # chamando User da forma direta


# Create your tests here.
class RecipeViewsTest(TestCase):
    ''' Testa urls da aplicação '''

    # Home
    # ----
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_Ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1 class="center">No recipes found here! 🤔🤔🤔</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):

        # populando a base de dados de testes (memória)
        category = Category.objects.create(name='Castegory')
        author = User.objects.create_user(
            first_name = 'user',
            last_name = 'name',
            username = 'username',
            password='123455',
            email='username@email.com'
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        ) 
        response = self.client.get(reverse('recipes:home'))
        pass


    # Category
    # --------
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category',
                       kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))  # category_id -> nome do parâmetro usado na url
        self.assertEqual(response.status_code, 404)

    # Recipe detail
    # -------------
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id':1}))  # recipe_id -> nome do parâmetro usado na url
        self.assertEqual(response.status_code, 404)

    # Search
    # -------

    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)