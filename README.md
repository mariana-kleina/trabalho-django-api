# API RESTful de Blog - Django REST Framework

API RESTful desenvolvida com **Django** e **Django REST Framework (DRF)** para gerenciamento de um domínio de Blog (`Categoria` e `Artigo`), fundamentada em boas práticas de arquitetura de software, conformidade com o protocolo HTTP, segurança e persistência em banco de dados relacional.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Django**: Framework web principal.
* **Django REST Framework (DRF)**: Construção da API REST.
* **python-dotenv**: Gerenciamento e isolamento de variáveis de ambiente (`.env`).
* **django-filter**: Filtragem dinâmica e avançada nos endpoints da API.
* **SQLite**: Banco de dados relacional (padrão de desenvolvimento).

---

## 🏗️ Arquitetura e Estrutura do Projeto

O projeto segue uma arquitetura em camadas modularizada no app `api`:

```text
trabalho_django_api/
├── api/                   # App modular do domínio
│   ├── filters.py         # Filtros avançados de pesquisa
│   ├── models.py          # Modelagem de dados e integridade referencial (PROTECT)
│   ├── serializers.py     # Serializadores nativos e aninhados
│   ├── services.py        # Camada de serviços / Regras de negócio
│   ├── urls.py            # Roteamento automático via DefaultRouter
│   └── views.py           # ModelViewSet com controle de verbos HTTP
├── config/                # Configurações globais do Django
│   ├── settings.py        # Leitura do .env, Paginação e Registro do DRF
│   └── urls.py            # Mapeamento da rota principal /api/
├── .env                   # Variáveis de ambiente locais (não versionado)
├── .env.example           # Modelo de variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git (.env, .venv, db.sqlite3)
├── manage.py              # Utilitário de linha de comando do Django
└── requirements.txt       # Dependências do projeto
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/trabalho-django-api.git
cd trabalho-django-api
```

### 2. Criar e ativar o ambiente virtual (`.venv`)

* **No Windows (PowerShell/Git Bash):**
  ```bash
  python -m venv .venv
  source .venv/Scripts/activate  # Git Bash
  # ou
  .\.venv\Scripts\Activate       # PowerShell / CMD
  ```

* **No Linux/Mac:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto baseado no arquivo `.env.example`:

```bash
cp .env.example .env
```

Conteúdo padrão do `.env`:
```env
SECRET_KEY=django-insecure-chave-de-desenvolvimento-super-segura
DEBUG=True
```

### 5. Executar as Migrações do Banco de Dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Iniciar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

A API estará acessível em: `http://127.0.0.1:8000/api/`

---

## 📌 Endpoints da API

A API conta com CRUD completo para ambas as entidades, suportando os verbos HTTP: `GET`, `POST`, `PUT`, `PATCH` e `DELETE`.

### 🏷️ Categorias (`/api/categorias/`)

| Verbo | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/categorias/` | Listagem paginada de categorias |
| `GET` | `/api/categorias/<id>/` | Detalhes de uma categoria específica |
| `POST` | `/api/categorias/` | Criação de uma nova categoria |
| `PUT` | `/api/categorias/<id>/` | Atualização completa da categoria |
| `PATCH` | `/api/categorias/<id>/` | Atualização parcial da categoria |
| `DELETE` | `/api/categorias/<id>/` | Remoção da categoria |

### 📰 Artigos (`/api/artigos/`)

| Verbo | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/artigos/` | Listagem paginada de artigos com dados aninhados da categoria |
| `GET` | `/api/artigos/<id>/` | Detalhes de um artigo específico |
| `POST` | `/api/artigos/` | Criação de um novo artigo vinculando `categoria_id` |
| `PUT` | `/api/artigos/<id>/` | Atualização completa do artigo |
| `PATCH` | `/api/artigos/<id>/` | Atualização parcial do artigo |
| `DELETE` | `/api/artigos/<id>/` | Remoção do artigo |

---

## 🔍 Filtros e Paginação

* **Paginação Global:** Configurada globalmente no `settings.py` em 10 itens por página (`PageNumberPagination`).
* **Filtros de Artigos:**
  * Por título (busca parcial): `/api/artigos/?titulo=teste`
  * Por categoria: `/api/artigos/?categoria=1`
  * Por status ativo: `/api/artigos/?ativo=true`
