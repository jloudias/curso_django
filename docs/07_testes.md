## Testes

### Test Runner

- gerencia o execução de todos os testes automatizados
- no python:
  - Unittest : default do Django
  - Pytest : será utilizado no curso
- testes são realizados em uma base de dados vazia, carregada na memória.

### Pytest

#### Instalação

   ``` python -m pip install pytest pytest-django ```
- criar arquivo *pytest.ini*,  no diretório raiz

> [pytest]<br>
> DJANGO_SETTINGS_MODULE = project.settings<br>
> python_files = test.py tests.py test_*.py tests_*.py *_test.py *_tests.py<br>

- editar *settings.json* do vscode:
```
{
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [], 
}
```   

#### Primeiro teste

- editar arquivo tests.py, no diretório da aplicação (recipes)
    ```
    class RecipeURLsTest(TestCase):
        def test_the_pytest_is_ok(self):
            assert 1==2, "Um não é igual a dois."
    ```
- todo método que começar com *test_* será um teste a ser executado
- usar para o teste sempre nome mais explícito possível, independente do tamanho
- para executar teste, no terminal, digite:
  - ```pytest```                 ::::: para test runner pytest
  - ```python manage.py test```  ::::: para test runner Unittest (padrão do Django)
  
#### Teste de urls e views

- criar pasta *tests*, na pasta da app, para armazenar os arquivos de teste
- adicionar *__init__.py*, para pasta ser reconhecida como pacote
- criar arquivo comecçando por *test_* para cada conjunto de testes
- criar classe e definir os métodos para os testes 
- importar de *django.urls* os métodos:
  - reverse(nome_da_URL) ::: dada uma rota, retorna a url
  - resolve(url)  ::: dada uma url, retorna a view 
- asserts utilizados:
  - assertEqual ::: compara valores
  - assertIs  ::: compara objetos

#### Testando o template usado e status code

- self.client()  ::: objeto do Unittest, que recebe todas informações que uma url enviaria a um cliente
- criar uma variável *response* que receba o HttpResponse retornado pela view para o cliente

  ```response = self.client.get(reverse('recipes:home'))```

- assertTemplateUsed ::: informa o template utilizado
  
  ```self.assertEqual(response.status_code, 200)```

  ```self.assertTemplateUsed(response, 'recipes/pages/home.html')```

### Executar um único teste

  ```pytest -k 'nome_do_teste' ```   (no pytest)

  ou

  ```python .\manage.py test -k 'nome_do_teste' ```  (no Unittest)

### Populando a base de dados de teste

- criar um teste contendo os comandos de criação de dados do shell
- utize *pass* e excute o teste

### Duplicar dados
- no django shell, crie uma variável com os dados a serem duplicados
- faça o id = None para evitar que o Django atualize o registro, em vez de duplicá-lo
- salve o registro
- utilize um for para duplicar vários registros

``` 
r = Recipe.objects.get(id=2)
r.id = None
r.save()

for i in range(10): r.id=None; r.save()
```

### Criando slug único

- no *models.py*, configure o campo slug com *unique=True*
- use um *for indexado* para adicionar um índice ao valor do *slug*

```
from models.py import Recipe
recipes = Recipe.objects.all()

for index, recipe in enumerate(recipes): recipe.slug = f'{recipe.slug}-index'; recipe.save()
```

### TDD: Test Driven Development

- criar  teste antes do código de desenvolvimento
- RED -> GREEN -> REFACTORY
  - teste da erro
  - implementar o mínimo necessário para eliminar o erro
  - refatorar, se necessário
