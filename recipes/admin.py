from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    
    # sort by name
    @admin.display(ordering='name')
    def name(self, obj):
        return obj.name

admin.site.register(Category, CategoryAdmin)

## registrar o model no app Admin usando um decorator
## a classe tem que vir logo abaixo do registro

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug')

    # sort by title
    @admin.display(ordering='title')
    def name(self, obj):
        return obj.title



