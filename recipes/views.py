from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404, HttpRequest
from utils.recipes.factory import make_recipe
from .models import Recipe, Category


def home(request: HttpRequest) -> HttpResponse:
    '''Exibe todas as receitas em home.html'''
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: HttpRequest, category_id: int) -> HttpResponse:
    '''Exibe as receitas filtradas por categoria em home.html '''
    # recipes = Recipe.objects.filter(category__id = category_id, is_published = True).order_by('-id')

    # if not recipes:
    #     # return HttpResponse(content='Category Not Found', status=404)
    #     return Http404("Not Found 😞😞😞")

    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f"{recipes[0].category.name} - Category",
    })


def recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    '''Exibe detalhes da receita em recipe_view.html'''
    # recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()

    recipe = get_object_or_404(Recipe, pk=recipe_id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
