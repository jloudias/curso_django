## Templates: rotas e variáveis

### Evitando colisões

- configure a variável `app_name`, no urls.py da aplicação
- nomear as rota com `name`
- chamar a url com `<nome_da_app>:<nome_da rota>`

```
    # no urls.py
    app_name = "recipes"
    urlpatterns = [
        path('recipes/<int:id>/', views.recipe, name='recipe'),
    ]
    ...
    # no template
    <a href="{% url 'recipes:recipe' recipe.id %}">
```


### Gerando dados fake com Faker

- instalar o módulo Faker<br>
   `pip install Faker`
- criar função para gerar os dados
  ```
    from faker import Faker

    fake = Faker('pt_BR')
    
    def make_recipe():
        return {
            'id': fake.random_number(digits=2),
            'title': fake.sentence(nb_words=6),
            'description': fake.sentence(nb_words=12),
            'preparation_time': fake.random_number(digits=2, fix_len=True),
            'preparation_time_unit': 'Minutos',
            'servings': fake.random_number(digits=2, fix_len=True),
            'servings_unit': 'Porções',
            'preparation_steps': fake.text(3000),
            'created_at': fake.date_time(),
            'author': {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
            },
            'category': {
                'name': fake.word()
            },
            'cover': {
                'url': 'https://loremflickr.com/320/240/food,cook',
            }
        }
    ``` 
- REFERÊNCIA: [Faker Documentation](https://faker.readthedocs.io/en/master/)


### Passando variáveis para o template

-   no views.py, do app, use o parâmetro `context` da função `render`
-   `context` recebe um dicionário 
-   Exemplo:
    ```
    def recipe(request, id):
        return render(request, 'recipes/pages/recipe-view.html',context = {
            'recipe':make_recipe(),
            'is_detail_page': True,
        })
    ```
    - `context` passa um dicionário com as variáveis *recipe* e *is_detail_page*,sendo: 
      - *recipe* -> lista gerada pela função *make_recipe*
      - *is_detail_page* -> booleano