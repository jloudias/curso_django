## Models

### Admin - Base de dados inicial

- criando a base de dados da app `admin`
```
    python manage.py migrate
    python manage.py createsuperuser
```

### Models

- subclasse de *django.db.models.Model*
- cada model = uma tabela do banco de dados
- atributos do model = campos da tabela
- campo *id* é implementado automaticamente
- uma *class* em *models.py* da app <br>
  `class Person(models.Model):`

### Fields
- tipos de campos mais usados
  - CharField(max_length=25)
  - IntegerField()
  - SlugField()
  - TextField()
  - BooleanField()
  - DateTimeField()
    - auto_now_add = True -> salva data da criação
    - auto_now = True -> salva data da atualização
  - ImageField()
    - upload_to='path_to_images_files'
    - configurar:
      - **MEDIA_URL** e **MEDIA_ROOT**, em `settings.py`
      - `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`, em urls.py

### Relacionamentos


#### Relacionamento com a tabela de usuários do Django

  ```
  from django.contrib.auth.models import User
  ...
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  ```

### Migrations

- criar ou alterar o model:
  - `python manage.py makemigrations` 
  - `python manage.py migrate`
- evitar editar os arquivos de migração


### Admin app

#### Registrando models no app Admin

- editar admin.py, na pasta da aplicação
  
    ```
    from django.contrib import admin
    from .models import Category <-

    class CategoryAdmin(admin.ModelAdmin): <-
        pass

    admin.site.register(Category, CategoryAdmin) <-
    ```

#### Customizando a interface
##### Listar pelo valor de um dos campos

- usar o metódo mágico `__str__()`
```
    def __str__(self) -> str:
            return self.<nome_do_campo>
```

##### Exibir mais campos na listagem

- em admin.py, na clase da tabela, adicionar: <br>
  `list_display = ('name', 'created_at')`
- para listar todos campos<br>
  `list_display = [field.name for field in Category._meta.get_fields()]`

##### Gerando campo slug automaticamente

- em admin.py, na clase da tabela, adicionar: <br>
  `prepopulated_fields = {"slug": ("title",)}`

##### Ordenando campos

- em admin.py, na clase da tabela, adicionar:
```
    # sorting by name
    @admin.display(ordering='name')
    def name(self, obj):
        return obj.name
```

### Shell

- o shell utiliza o manage *objects*
- inicialização do ambiente:
  ```
    python manage.py shell
    >>> from recipe.models import Category, Recipe
  ```
- save() : salva dados no banco de dados
- modo lazy -> faz operações na memória e só chama o bd qdo necessário (save, list, etc)
- QuerySet é um iterable


### Comando mais usados.

- READ
  - Category.objects.all()
  - Category.objects.all().first() `IMPORTANTE` -> para trazer só um registro, use first()
  - Category.objects.all().first().name
  - categories = Category.objects.all() -> gera um QuerySet
    - categories.order_by('id')  -> ASC
    - categories.order_by('-id') -> DESC
    - categories[:2] -> busca dois primeiros registros
  - Category.objects.all().filter(name='Vegano')
  - Category.objects.get(id=5) -> mesmo q filter, mas retorna erro qdo não encontra nada
  - FOREIGN KEY
    - recipes = Recipe.objects.all()
    - recipes.filter(category__name="Cafe da Manhã")

- CREATE
  - new_cat = Category(name = 'Saladas')
  - new_cat.save()
  - Category.objects.create(name = 'Frutas') -> cria e salva direto

- UPDATE
  - new_cat.name = 'Teste' -> altera o
  - new_cat.save()

- DELETE
  - Category.Objects.all().first().delete()
  - save()


- ESTRUTURA
  - receita = Recipe.objects.all().first()
  - receita._meta.get_fields()
  - getattr(recipe, 'id') -> busca valor do campo

#### Criando um usuário no shell
  ```
  >>> from django.contrib.auth.models import User
  >>> User.objects.create_user(first_name='Peter', last_name='Parker', username='pparker', email='pparker@gmail.com', password='senha1234')
  ```
