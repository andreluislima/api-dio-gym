# 🏋️ API Dio Gym

&#x20;   &#x20;

> API para gerenciamento de academia construída com **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic** e **Docker**.
Essa API foi implementada como parte do primeiro projeto do desafio 01 de Python do Bootcamp SANTANDER | DIO
---

## 📚 Índice

- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🚀 Configuração e Execução](#-configuração-e-execução)
- [📌 Rotas Principais](#-rotas-principais)
- [🧪 Exemplos de Requisições](#-exemplos-de-requisições)

---

## 📁 Estrutura do Projeto

```
api-dio-gym/
├── workout_api/           # Código fonte da aplicação
│   └── main.py            # Ponto de entrada da API
├── alembic.ini            # Configuração do Alembic
├── alembic/               # Scripts de migração do banco
├── requirements.txt       # Dependências do projeto
├── docker-compose.yml     # Configuração do container PostgreSQL
└── workspace-venv/        # Ambiente virtual Python
```

---

## 🚀 Configuração e Execução

### 1️⃣ Criar e Ativar Ambiente Virtual

```bash
python -m venv workspace-venv
```

| Sistema     | Comando                                 |
| ----------- | --------------------------------------- |
| PowerShell  | `./workspace-venv/Scripts/Activate.ps1` |
| CMD Windows | `workspace-venv\Scripts\activate.bat`   |
| Linux/macOS | `source workspace-venv/bin/activate`    |

---

### 2️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

Caso não exista o arquivo:

```bash
pip freeze > requirements.txt
```

---

### 3️⃣ Subir Banco de Dados (Docker)

```bash
docker compose up -d --build
```

> Banco disponível em `localhost:5432`.

---

### 4️⃣ Configurar Alembic

Editar `alembic.ini`:

```
sqlalchemy.url = postgresql+asyncpg://workout:workout@localhost:5432/workout_db
```

Editar `alembic/env.py`:

```python
from workout_api.contrib.models import Base
target_metadata = Base.metadata
```

---

### 5️⃣ Criar e Aplicar Migrações

```bash
alembic revision --autogenerate -m "criação das tabelas iniciais"
alembic upgrade head
```

---

### 6️⃣ Executar a API

```bash
uvicorn workout_api.main:app --reload
```

> Acesse a documentação interativa:
>
> - Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
> - Redoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Rotas Principais

| Método | Endpoint               | Descrição                    |
| ------ | ---------------------- | ---------------------------- |
| GET    | `/`                    | Verifica se API está online  |
| GET    | `/atletas/`            | Lista todos os atletas       |
| POST   | `/atletas/`            | Cadastra um novo atleta      |
| GET    | `/categorias/`         | Lista categorias             |
| GET    | `/centro_treinamento/` | Lista centros de treinamento |

> As rotas podem variar conforme a implementação evoluir.

---

## 🧪 Exemplos de Requisições

### 🔹 Criar um Atleta

**Request:**

```bash
curl -X POST "http://127.0.0.1:8000/atletas/" \
-H "Content-Type: application/json" \
{
  "nome": "Rodrigo de Lima",
  "cpf": "18765432100",
  "idade": 42,
  "peso": 93.2,
  "altura": 1.9,
  "genero": "M",
  "categoria": {
    "nome": "Corrida"
  },
  "centro_treinamento": {
    "nome": "Equipe Prime"
  }
}
```

**Response:**

```json
{
  "id": "09c3eae3-6a93-45cc-9259-e872900647d9",
  "created_at": "2025-07-31T17:49:34.070490Z",
  "nome": "Rodrigo de Lima",
  "cpf": "18765432100",
  "idade": 42,
  "peso": 93.2,
  "altura": 1.9,
  "genero": "M",
  "categoria": {
    "nome": "Corrida"
  },
  "centro_treinamento": {
    "nome": "Equipe Prime"
  }
}
```

### 🔹 Listar Atletas

```bash
curl -X GET http://127.0.0.1:8000/atletas/
```

---


## 📜 Licença

Este projeto é distribuído sob a licença [MIT](LICENSE).

