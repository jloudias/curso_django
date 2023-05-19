## Arquivos estáticos

### Visão geral

- arquivos com pouca ou nenhuma alteração: css, js, imagens, etc
- podem estar dentro ou fora de uma aplicação
- gerenciados pela app `django.contrib.staticfiles`

### Configuração básica

- criar pasta `static` no diretório da aplicação
- usar sempre `namespace` (hieraquia de pastas dentro da pasta 'static')
- configurar `settings.py` do projeto:
  - STATIC_URL = "static/"
- no template:
```
    {% load static %}  
    ...
    <link rel="stylesheet" href="{% static 'recipes/css/style.css' %}">
```

### Arquivos não atrelados a uma app

- configurar no `settings.py`, criar a lista `STATICFILES_DIR`  e adicionar os diretórios desejados
- Exemplo:
  - criar pasta *base_static* no diretório raiz do projeto
  - não esquecer do namespace `namespace` (global/css , por exemplo)
  - criar a lista em *settings.py*
    ```
    STATICFILES_DIR = [
      BASE_DIR / 'base_static',

    ]
    ```
  - no template, adotar o procedimento do item anterior.
  

