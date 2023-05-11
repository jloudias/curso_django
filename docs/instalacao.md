# Preparando o Ambiente de Trabalho
<br>

## Instalação do Python e Ambiente Virtual
- instalar Python
  - marcar opção "Add Python to PATH"
- criar ambiente virtual
    ```
    mkdir <projeto> 
    cd <projeto>
    python -m venv .venv  
    .venv\Scripts\activate 
    .venv\Scripts\deactivate 
    ```
## Configuração do VSCode
- alterar permissões do Windows para execução de scripts<br>
`Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`
- usar interpretador Python do ambiente virtual
    ```
    <ctrl> + <shift> + <p> 
    Python: select interpreter
    copiar o path do python no ambiente virtual
    ```
  `ATENÇÃO` vscode só inicializa automaticamente ambiente virtual se houver algum arquivo .py aberto 

## Instalação do Django
- instalando pré-requisitos
    ```
    .venv\Scripts\activate                  # ativa o ambiente virtual
    python -m pip install setuptools wheel  # scripts para geração e distribuição de pacotes
    pip install pillow                      # modulo de tratamento de imagens
    ```
- instalação do django 
    ```
    .venv\Scripts\activate 
    python -m pip install django
    pip freeze                      # lista pacotes instalados no ambiente virtual
    ```
- criar projeto no django
    ```
    django-admin startproject <projeto> .    # o ponto evita duplicidade de pastas
    ```
- testar a instalação:
    ```
    python manage.py runserver
    visualizar site no navegador.(http://localhost:8000)
    ```

## Configuração do GitHub
- criar repositório <projeto_nome> no GitHub
- gerar uma chave SSH:
    ```
    # serão gerados os arquivos id_rsa e id_rsa.pub, no diretório .ssh
    ssh-keygen  -t rsa -b 4096 -C "jloudias@gmail.com"
    ```
- no site do GitHub, em Settings/SSH and GPG keys
    ```
    > clicar no botão New SSh key
    > definir um nome para chave
    > adicionar o conteúdo do arquivo id_rsa.pub ao valor da chave
    ```
- inicializar o repositório:
    ```
    git init # na raiz do projeto, cria a pasta .git
    git remote add origin git@github.com:jloudias/<nome_projeto>.git	
    ```
- criar os arquivos: 
  - `.gitignore` -> arquivos e pastas a serem excluídos da sincronização
  - `README.md`  -> descrição do repositório
<br> <br>
- sincronizar o repositório:
    ```
    git add .
    git commit -m "first commit"
    git push
    ```

	
