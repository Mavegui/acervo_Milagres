# Acervo Milagres

O Acervo Milagres é um projeto de extensão universitária focado na preservação da memória histórica e cultural da vila de Milagres. Através desta plataforma, é possível catalogar, gerenciar e visualizar registros fotográficos e históricos, garantindo que o patrimônio da comunidade seja documentado digitalmente.

## Tecnologias Utilizadas

- Framework: Django 6.0.4
- Linguagem: Python
- Banco de Dados: PostgreSQL (via Supabase)
- Armazenamento: Django Storages (S3/Supabase)
- Servidor de Produção: Gunicorn & WhiteNoise
- Estilização: Tailwind CSS, Js & CSS

## Como Executar o Projeto Localmente

1. Clonar o Repositório:
    ```bash
    git clone https://github.com/Mavegui/acervo_Milagres.git
    cd acervo_Milagres
    ```

2. Configurar o Ambiente Virtual:
    
    Instalar:
    ```bash
    python3 -m venv .venv
    ```

    Executar no Windows:
    ```bash
    .venv\Scripts\activate
    ```
    
    Executar no Linux/Mac:
    ```bash
    source .venv/bin/activate
    ```
    Desativar:
    ```bash
    deactivate
    ```

3. Instalar Dependências:

    ```bash
    pip install -r requirements.txt
    ```
    
4. Configurar Variáveis de Ambiente:

- Renomeie o arquivo .env.example para .env e preencha as credenciais do seu banco de dados e a Secret Key do Django.

5. Rodar Migrations e Servidor:
    ```bash
    python3 manage.py migrate
    python3 manage.py runserver
    ```

- Se lembre de configurar o ALLOWED_HOSTS com a URL usada.

## Segurança

O projeto utiliza variáveis de ambiente para proteger dados sensíveis e implementa políticas de segurança como SSL Redirect e HSTS para o ambiente de produção.
    
## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.