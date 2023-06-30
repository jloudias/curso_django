## Testes

### Test Runner

- gerencia o execução de todos os testes automatizados
- no python:
  - Unittest : default do Django
  - Pytest : será utilizado no curso

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
  

