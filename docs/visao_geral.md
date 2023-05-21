## Visão Geral 

### Workflow
|SEQ|AÇÃO|CÓDIGO|
|:--:|:---|:---:|
|1| Criar o projeto|django-admin startproject <projeto>|
|2| Criar aplicação|python manage.py startapp <aplicação>|
|3| Registrar aplicação|INSTALLED_APPS, no arquivo settings.py do projeto|
|4| Criar uma view|criar função no views.py da aplicação|
|5| Criar a rota|lançar caminho e view a ser acionada no urls.py da aplicação|
|6| Incluir rota no urls.py do projeto|import django.urls import path, include urlpatterns = [ ... ]|
|7| Criar template|criar pasta templates na aplicação criar html e lançar na views.py com render()|

### Diferença entre Projeto e Aplicação

- PROJETO:
  - é uma instalação do Django com algumas configurações
- APLICAÇÃO:
  - é um grupo de models, views, templates e urls.
  - interage com o framework para prover funcionalidades específicas
  - podem ser reutilizadas por outros projetos


> PROJETO é o site web e pode conter várias APLICAÇÕES,como: blog, wiki, forum, etc.

### Aplicações
- padrão MVT(Model-View-Template):
  - semelhante ao MVC(Model-View-Controller)
  - Views ~ Controllers (Laravel) 
  - Templates ~ Views (Laravel)
- criando uma aplicação:
    ```
    python manage.py startapp <nome_app>
    ```
- registrar a aplicação no projeto (evita erro "Template Not Found")
	- settings.py
	- INSTALLED_APPS
    	- § '<nome_app_registrado_em_apps.py>',
- aplicações instaladas por default: 
    - admin --> gerenciar nossos dados
    - auth --> autenticação de usuários
    - contenttypes
    - sessions --> controle de sessões: obsoleta: pode deletar
    - messages --> exibe notificações para usuários
    - staticfiles --> servidor de arquivos estáticos: imagens, arquivos CSS, etc

#### Estrutura padrão de uma aplicação

|ITEM|FUNÇÃO|
|:---|:---|
| migrations| pasta com arquivos para gerenciamento de tabelas|
| `__init__.py`| controle de pacotes|
| admin.py| registre os models aqui, para que a app admin possa gerencia-los (CRUD e outros)|
| apps.py| subclasse herdada de AppConfig para configuração desta app, |
| models.py| classes model para a app (semelhante ao Model do PHP)|
| tests.py| unidades de testes (test unit)|
| views.py| contém a lógica para atender requisições do app (semelhante ao Controller do PHP)|
| urls.py| criado pelo usuário para inclusão no urls.py do projeto|
| templates| pasta criada pelo usuário para conter os templates (arquivos HTML)|

### Views
  - views.py 
  - semelhantes aos Controllers, no Laravel
  - contém as ações a serem excutadas
  - primeira view
    ```
    from django.http import HttpResponse
    def say_hello(request):
        return HttpResponse('Hello')
    ```
  - chamando templates
    ```
    from django.shortcuts import render
    def index(request):
        return render(request, '<nome_do_template>', context = { 'name': 'Jorge'})
    ```
    - django busca na pasta templates

### Urls
  - urls.py (criado pelo desenvolvedor)
  - arquivo de rotas 
  - a função `path(rota, view)` passa um objeto `request` para a função chamada
  - a função chamada deve retornar um objeto `response`
  - `DICA` -> importar urls.py das apps para o urls.py do projeto
    - função `include` deve ser importada de `django.urls`
      - recebe 'nome_da_aplicação.nome_arquivo_urls'
  - para acessar views do diretório corrente:
    ```
    from . import views
    ```

#### Modelos de arquivos urls.py
  - urls.py (projeto)

    ```
    from django.contrib import admin
    from django.urls import path, include
    urlpatterns =[
        path("admin", admin.site.urls),
        path("siscond", include('siscond.urls))
    ]
    ```
  - urls.py (aplicação)

    ```
    from django.urls import path
    from . import views
    urlpatterns =[
        path("", views.index, name='index')
        path("about", views.about, name="about")
    ]
	  ```

### Templates

- exibe a página de resposta ao usuário de uma forma amigável
- o django busca os templates em arquivos HTML na pasta 'templates' da aplicação -> criar
- erro "Template Does Not Exist":
  - aplicação não está registrada em INSTALLED_APPS, em settings.py
  - erro de namespace:
    - configurar DIRS[], em TEMPLATES, settings.py
    - para templates fora da aplicação:
  ```
    TEMPLATES = [
      ...
      'DIRS':[ 
        BASE_DIR / 'base_templates',
        ],
    ]
  ```


  `DICA: ` crie estrutura de arquivos e pastas dentro da pasta 'templates' e use path relativo

#### Função render()

- importada no views.py
- parâmetros:
  - requer o objeto request
  - path para o template
  - context -> dicionário com nome da variável e valor a serem passados
  - status -> status da conexão HTTP

**Exemplo:**
  ```
  return render(
    request, 
    'recipes/home.html', 
    context = {
      'name':'Jorge Dias',
    },
    status = 200
  )
  ```

#### Linguagem de template

| TAG/FILTER | DESCRIÇÃO/EXEMPLO |
|:---:|:---|
|{% code %}| códigos como loops, condições, comparações,etc|
|{{ variável }}| renderiza uma variável passada|
|{{ variável \| default:'nothing'}}| filtrar valor default para variável|

- [A linguagem de template do Django](https://docs.djangoproject.com/pt-br/4.2/ref/templates/language/)
- [Referência para tags e filters](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/#)

