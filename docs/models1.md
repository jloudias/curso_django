## Models

### Admin - Base de dados inicial

- criando a base de dados da app `admin`
```
    python manage.py migrate
    python manage.py createsuperuser
```

### Models

- subclasse de django.db.models.Model
- cada model = uma tabela do banco de dados
- atributos do model = campos da tabela
- campo *id* é implementado automaticamente
- uma *class* em *models.py* da app <br>
  `class Person(models.Model):`

### Fields
- tipos de campo mais usados
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

### Relacionamentos


#### Relacionamento com a tabela de usuários do Django

  ```
  from django.contrib.auth.models import User
  ...
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  ```

### Migrations

- criar o model
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

#### Exibir um campo do objeto na listagem

- usar o metódo mágico `__str__()`
```
    def __str__(self) -> str:
            return self.<nome_do_campo>
```