## Arquivos estáticos

### Visão geral

- arquivos com pouca ou nenhuma alteração: css, js, imagens, etc
- podem estar dentro ou fora de uma aplicação
- gerenciados pela app `django.contrib.staticfiles`
- usar sempre *namespace* (pastas separadas) para evitar colisão de nomes

### Arquivos atrelados a uma app

- criar pasta *static* no diretório da aplicação
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

- configurar no `settings.py`, criar a lista `STATICFILES_DIRS`  e adicionar os diretórios desejados
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

### Servidor de produção

- configurações usadas no ambiente de desenvolvimento não valem para o ambiente de produção
- se `DEBUG = False`, no servidor de produção fazer:
  - criar pasta *static* na raiz do projeto
  - configurar STATIC_ROOT
    ```
    STATIC_ROOT = 'static/'
  - encontrar e mover os arquivos estáticos:
    ```
    python manage.py collectstatic
    ``` 

**REFERÊNCIA** : [How to manage static files](https://docs.djangoproject.com/en/4.2/howto/static-files/)



