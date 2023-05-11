# Visão Geral 

## Workflow
|SEQ|AÇÃO|CÓDIGO|
|:--:|:---|:---:|
|1| Criar o projeto|django-admin startproject <projeto>|
|2| Criar aplicação|python manage.py startapp <aplicação>|
|3| Registrar aplicação|INSTALLED_APPS, no arquivo settings.py do projeto|
|4| Criar uma view|criar função no views.py da aplicação|
|5| Criar a rota|lançar caminho e view a ser acionada no urls.py da aplicação|
|6| Incluir rota no urls.py do projeto|import django.urls import path, include urlpatterns = [ ... ]|
|7| Criar template|criar pasta templates na aplicação criar html e lançar na views.py com render()|



## Aplicações
- projeto pode ter uma ou mais aplicações e uma aplicação pode ser utilizada em diversos projetos
- aplicação coresponde a um módulo do site, tipo: 'livro_de _ocorrências', 'blog', 'administração'.
- criando uma aplicação:
	- python manage.py startapp <nome_app>
- registrar a aplicação no projeto (evita erro "Template Not Found")
	- settings.py
	- INSTALLED_APPS
    	- § '<nome_app>',
- aplicações instaladas por default no 
    - admin --> gerenciar nossos dados
    - auth --> autenticação de usuários
    - contenttypes
    - sessions --> controle de sessões: obsoleta: pode deletar
    - messages --> exibe notificações para usuários
    - staticfiles --> servidor de arquivos estáticos: imagens, arquivos CSS, etc

### Estrutura padrão de uma aplicação

|ITEM|FUNÇÃO|
|:---|:---|
| migrations| pasta com arquivos para gerenciamento de tabelas|
| __init__.py| controle de pacotes|
| admin.py| gerenciar como a interface admin vai funcionar para esta app|
| apps.py| module de configuração desta app|
| models.py| classes model para a app (semelhante ao Model do PHP)|
| tests.py| unidades de testes (test unit)|
| views.py| contém as requisições do app (semelhante ao Controller do PHP)|
| urls.py| criado pelo usuário para inclusão no urls.py do projeto|
| templates| pasta criada pelo usuário para conter os templates (arquivos HTML)|

## Views
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

## Urls
  - urls.py
  - arquivo de rotas 
  - importar urls.py das apps para o url.py do projeto
  - urls.py (projeto)

    ```
    from django.contrib import admin
    from django.urls import path, include
    urlpatterns =[
        path("admin", admin.site.urls),
        path("siscond", include('siscond.urls))
    ```
  - urls.py (aplicação)

    ```
    from django.urls import path
    from . import views
    urlpatterns =[
        path("", views.index, name='index')
        path("about", views.about, name="about")
	````
