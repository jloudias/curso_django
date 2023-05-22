## Templates: herança e blocos.

### Configurando o ambiente.

- criar pasta *base_templates* na raiz do projeto (BASE_DIR)
- editar *settings.py*:
  ```
  TEMPLATES = [
    {
        ...,
        'DIRS': [
            BASE_DIR / 'base_templates',
        ],
        ..., 
  ```
- criar pasta *global*, em *base_templates* (namespace)

### Herança básica.

#### Template pai.

- criar arquivo HTML *base.html*, em *base_templates\global* (template pai)
- delimitar os trechos a serem preenchidos pelo template filho com as tags `block` e `endblock`
```
<head>
    <link rel="stylesheet" href="style.css">   
    <title> {% block title %} My amazing site {% endblock %} </title>
</head>

<body>
    <div id="sidebar">

        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}    
    </div>


    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
```
- no exemplo acima, o conteúdo das tags *block title*, *block sidebar* e *block content* será fornecido pelo template filho.
- caso o template filho não informe o conteúdo, será utilizado o do template pai

#### Template filho

- inicia com a tag `extends` que informa o template pai a ser utilizado.
- informa os valores a serem lançados em cada bloco.
    ```
    {% extends "base.html" %}

    {% block title %}My amazing blog{% endblock %}

    {% block content %}
    {% for entry in blog_entries %}
        <h2>{{ entry.title }}</h2>
        <p>{{ entry.body }}</p>
    {% endfor %}
    {% endblock %}
    ```

### Níveis de herança.

- não há limite para níveis de herança
- uso básico:
  - *base.html*
    - estrutura visual principal do site
  - *base_SECTIONNAME.html
    - uma para cada seção do site
    - extensão de *base.html*
    - design específico de cada seção
      - base_news.html, base_sports.html, etc
  - templates individuais para cada tipo de página
    - extensões de *base_SECTIONNAME.html*
    - news_article.html, blog_entry.html

### Boas práticas

- template filho começa sempre com `{% extends '<path_to_base_template>' %}`
- qto mais `{% block %}`, melhor (o filho não precisa preencher tudo)
- repita o nome do bloco no `{% endblock <nome> %}`
- use `{% block.super %}` para fazer pequenas customizações. Exemplo:
    ```
    {% block branding %}
        <img src="link/to/logo.png" alt="logo">
        {{ block.super }}
    {% endblock %}
    ```
    - o bloco branding do template pai será utilizado com a inserção da imagem com o logo
- blocos não podem ter o mesmo nome no mesmo template



