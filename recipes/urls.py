from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    # urls mais específicas (sem parâmetros) sempre no começo
    path('', views.home, name='home'),
    path('recipes/search/', views.search, name='search'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:recipe_id>/', views.recipe, name='recipe'),  
]
