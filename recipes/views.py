from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import Recipe


# Create your views here.
def home(request):
    '''Exibe todas as receitas em home.html'''
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context = {
        'recipes': recipes,
    })

def category(request, category_id):
    '''Exibe as receitas filtradas por categoria em home.html '''
    recipes = Recipe.objects.filter(category__id = category_id, is_published = True)
    return render(request, 'recipes/pages/category.html', context = { 'recipes': recipes})

def recipe(request, recipe_id):
    '''Exibe detalhes da receita em recipe_view.html'''
    recipe = Recipe.objects.filter(pk = recipe_id, is_published = True).first()
    return render(request, 'recipes/pages/recipe-view.html',context = {
        'recipe': recipe,
        'is_detail_page': True,
    })
