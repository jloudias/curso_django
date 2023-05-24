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