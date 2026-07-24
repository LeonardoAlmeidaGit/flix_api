# Flix API

API REST completa para gestão de filmes desenvolvida com Django e Django REST Framework. Permite cadastrar e gerenciar filmes, atores, gêneros e avaliações, além de visualizar estatísticas gerais sobre o catálogo.

## 🚀 Tecnologias

- Python
- Django 5
- Django REST Framework
- SimpleJWT
- PostgreSQL

## ✅ Funcionalidades

- Cadastro e gestão de filmes com título, gênero, elenco, data de lançamento e resumo
- Cadastro de atores com nome, data de nascimento e nacionalidade
- Cadastro de gêneros cinematográficos
- Registro de avaliações com estrelas (0 a 5) e comentário
- Cálculo automático de média de avaliações por filme
- Estatísticas gerais: total de filmes, filmes por gênero, total de avaliações e média de estrelas
- API REST completa com autenticação JWT
- Sistema de permissões granular por operação (visualizar, criar, editar, deletar)

## 🔧 Como rodar o projeto localmente

**Pré-requisitos:** Python 3 e um banco PostgreSQL em execução.

**1. Clone o repositório**
```bash
git clone https://github.com/LeonardoAlmeidaGit/flix_api.git
cd flix_api
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Suba um PostgreSQL (opção rápida via Docker)**
```bash
docker run -d --name flix_db -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=flix_api -p 5432:5432 postgres:16
```
> Se já tiver um PostgreSQL local, pule este passo e ajuste as credenciais no `.env`.

**5. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:
```env
SECRET_KEY=cole-sua-SECRET_KEY-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=flix_api
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

**6. Execute as migrations**
```bash
python manage.py migrate
```

**7. Crie um superusuário**
```bash
python manage.py createsuperuser
```

**8. Inicie o servidor**
```bash
python manage.py runserver
```
Acesse http://127.0.0.1:8000 no navegador.

## 🔐 Permissões e Grupos

O sistema utiliza o sistema nativo de grupos e permissões do Django. Para liberar acesso a um usuário, acesse o painel administrativo em `/admin/`, crie um grupo com as permissões desejadas e atribua o usuário a esse grupo.

## 📡 API REST

A API utiliza autenticação JWT. Para obter um token de acesso:

```http
POST /api/v1/authentication/token/
Content-Type: application/json

{
  "username": "seu-usuario",
  "password": "sua-senha"
}
```

Para autenticar nas requisições, envie o token no header: `Authorization: Bearer <access_token>`.

### Endpoints disponíveis

| Recurso      | Listagem / Criação      | Detalhe / Edição / Exclusão |
|--------------|-------------------------|-----------------------------|
| Filmes       | `/api/v1/movies/`       | `/api/v1/movies/<id>/`      |
| Atores       | `/api/v1/actors/`       | `/api/v1/actors/<id>/`      |
| Gêneros      | `/api/v1/genres/`       | `/api/v1/genres/<id>/`      |
| Avaliações   | `/api/v1/reviews/`      | `/api/v1/reviews/<id>/`     |
| Estatísticas | `/api/v1/movies/stats/` | —                           |

## 📁 Estrutura do Projeto

```bash
flix_api/
├── app/              # Configurações principais: settings, urls e permissões
├── authentication/   # Endpoints de autenticação JWT
├── genres/           # Gestão de gêneros
├── actors/           # Gestão de atores
├── movies/           # Gestão de filmes e estatísticas
└── reviews/          # Avaliações de filmes
```

## 👨‍💻 Autor

Leonardo Almeida — [LinkedIn](https://www.linkedin.com/in/leonardo-almeida-dev/) · [GitHub](https://github.com/LeonardoAlmeidaGit)
