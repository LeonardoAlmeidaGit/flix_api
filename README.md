# Flix API

API REST completa para gestão de filmes desenvolvida com Django e Django REST Framework. Permite cadastrar e gerenciar filmes, atores, gêneros e avaliações, além de visualizar estatísticas gerais sobre o catálogo.

## 🚀 Tecnologias

- Python 3.x
- Django 5.x
- Django REST Framework
- SimpleJWT
- SQLite

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

Pré-requisitos: Python 3.x instalado

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/flix-api.git
cd flix-api
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

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:

SECRET_KET=cole-sua-SECRET_KEY-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

**5. Execute as migrations**
```bash
python manage.py migrate
```

**6. Crie um superusuário**
```bash
python manage.py createsuperuser
```

**7. Inicie o servidor**
```bash
python manage.py runserver
```
Acesse http://127.0.0.1:8000 no navegador.


## 🔐 Permissões e Grupos

O sistema utiliza o sistema nativo de grupos e permissões do Django. Para liberar acesso a um usuário, acesse o painel administrativo em `/admin/`, crie um grupo com as permissões desejadas e atribua o usuário a esse grupo.

## 📡 API REST

A API utiliza autenticação JWT. Para obter um token de acesso:
POST /api/v1/authentication/token/
Content-Type: application/json

{
  "username": "seu-usuario",
  "password": "sua-senha"
}

## Endpoints disponíveis

| Recurso      | Listagem / Criação    | Detalhe / Edição / Exclusão   |
|--------------|-----------------------|-------------------------------|
| Filmes       | /api/v1/movies/       | /api/v1/movies/\<id\>/        |
| Atores       | /api/v1/actors/       | /api/v1/actors/\<id\>/        |
| Gêneros      | /api/v1/genres/       | /api/v1/genres/\<id\>/        |
| Avaliações   | /api/v1/reviews/      | /api/v1/reviews/\<id\>/       |
| Estatísticas | /api/v1/movies/stats/ | —                             |

Para autenticar nas requisições, envie o bearer token no header.

## 📁 Estrutura do Projeto
flix-api/ ├── app/ # Configurações principais, settings, urls e permissões ├── authentication/ # Endpoints de autenticação JWT 
├── genres/ # Gestão de gêneros ├── actors/ # Gestão de atores ├── movies/ # Gestão de filmes e estatísticas ├── reviews/ # Avaliações de filmes

## 👨‍💻 Autor

Leonardo — [LinkedIn](https://www.linkedin.com/in/leonardoalmeida-) · [GitHub](https://github.com/LeonardoAlmeidaGit)
