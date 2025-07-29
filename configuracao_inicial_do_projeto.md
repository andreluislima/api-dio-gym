# 🐍 Guia Definitivo: Execução de Projeto Python com FastAPI, Uvicorn e Virtualenv

Este guia orienta passo a passo a configuração e execução do projeto `api-dio-gym`, explicando **o que fazer**, **em que ordem**, **onde executar** e **por que fazer**.

---

## 📁 Estrutura Esperada do Projeto

```text
api-dio-gym/
├── workout_api/
│   └── main.py
├── requirements.txt
└── workspace-venv/ (ou venv/)
```

---

## 🚀 Etapas do Projeto

---

### 1. 🔧 Criar e Ativar o Ambiente Virtual

#### ✉️ **Função**

Isola as dependências do projeto, evitando conflitos com outros projetos Python.

#### 📍 **Onde executar**

Na raiz do projeto: `api-dio-gym/`

#### ⚙️ **Comandos**

```bash
# Criar o ambiente virtual
python -m venv workspace-venv
```

Ativar o ambiente virtual:

| Sistema       | Comando                                 |
| ------------- | --------------------------------------- |
| PowerShell    | `.\workspace-venv\Scripts\Activate.ps1` |
| CMD (Windows) | `workspace-venv\Scripts\activate.bat`   |
| Linux/macOS   | `source workspace-venv/bin/activate`    |

---

### 2. 📆 Atualizar o `pip` (opcional, mas recomendado)

#### ✉️ **Função**

Evita problemas com instalação de pacotes.

#### 📍 **Onde executar**

Qualquer pasta, desde que o ambiente virtual esteja **ativado**.

#### ⚙️ **Comando**

```bash
python -m pip install --upgrade pip
```

---

### 3. 📁 Instalar as Dependências do Projeto

#### ✉️ **Função**

Instala as bibliotecas necessárias a partir do `requirements.txt`.

#### 📍 **Onde executar**

Na raiz do projeto: `api-dio-gym/`

#### ⚙️ **Comando**

```bash
pip install -r requirements.txt
```

> 💡 **Não tem **``** ainda?**\
> Gere com:

```bash
pip freeze > requirements.txt
```

---

### 4. ⚡ Executar o Projeto com `uvicorn`

#### ✉️ **Função**

Roda o servidor FastAPI com `hot-reload` em modo desenvolvimento.

#### 🛣️ **Duas formas de rodar:**

✅ **Opção 1 - Executar da raiz (**``**):**

```bash
uvicorn workout_api.main:app --reload
```

✅ **Opção 2 - Executar de dentro da pasta **``**:**

```bash
cd workout_api
uvicorn main:app --reload
```

---

### 5. 🐘 Subir Banco de Dados com Docker (opcional)

> Apenas se estiver usando banco Postgres via Docker.

#### ✉️ **Função**

Sobe o container com banco de dados PostgreSQL usando `docker-compose`.

#### 📍 **Onde executar**

Na pasta que contém o `docker-compose.yml`

#### ⚙️ **Comando (via WSL/Linux)**

```bash
docker compose up -d --build
```

---

## ✅ Resumo Final: Checklist de Execução

| Etapa                        | Diretório                      | Comando                                 |
| ---------------------------- | ------------------------------ | --------------------------------------- |
| Criar ambiente virtual       | `api-dio-gym/`                 | `python -m venv workspace-venv`         |
| Ativar ambiente (PowerShell) | `api-dio-gym/`                 | `.\workspace-venv\Scripts\Activate.ps1` |
| Atualizar pip (opcional)     | qualquer (venv ativo)          | `python -m pip install --upgrade pip`   |
| Instalar dependências        | `api-dio-gym/`                 | `pip install -r requirements.txt`       |
| Gerar requirements.txt       | `api-dio-gym/`                 | `pip freeze > requirements.txt`         |
| Rodar API (modo 1 - raiz)    | `api-dio-gym/`                 | `uvicorn workout_api.main:app --reload` |
| Rodar API (modo 2 - interno) | `api-dio-gym/workout_api/`     | `uvicorn main:app --reload`             |
| Subir banco com Docker       | onde está `docker-compose.yml` | `docker compose up -d --build`          |

---

Se quiser, posso gerar um `README.md` completo com seções adicionais como `.env`, `Dockerfile`, variáveis de ambiente, estrutura modular, e boas práticas com FastAPI.

