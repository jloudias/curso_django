## Testes

### Test Runner

- gerencia o execução de todos os testes automatizados
- no python:
  - Unittest : default
  - Pytest : será utilizado no curso

### Pytest

#### Instalação
    ```python -m pip install pytest pytest-django```

- editar *settings.json* do vscode:
    {
        "python.testing.unittestEnabled": false,
        "python.testing.pytestEnabled": true,
        "python.testing.pytestArgs": [
            "."
        ],
    }
    
#### Primeiro teste

- editar arquivo tests.py, no diretório da aplicação (recipes)
    ```
    class RecipeURLsTest(TestCase):
        def test_the_pytest_is_ok(self):
            assert 1==2, "Um não é igual a dois."
    ```
- todo método que começar com *test_* será um teste a ser executado
- para executar teste, no terminal, digite ```pytest```
  

