# 🐍 Guia de Execução do Projeto Python com FastAPI, Uvicorn e Virtualenv

Este documento explica detalhadamente **onde e quando executar cada comando** no seu projeto `api-dio-gym`, usando `FastAPI`, `uvicorn`, `venv` e opcionalmente `Docker`. Também descreve **qual é a função de cada comando**.

---

## ✅ Estrutura esperada do projeto

```text
api-dio-gym/
├── workout_api/
│   └── main.py
├── requirements.txt
└── venv/ (ou workspace-venv/)
```

---

## ᾟ2 Ambiente virtual (venv)

### ✉ Função:

Isola as dependências do projeto para que elas não conflitem com outros projetos Python no seu sistema.

### 🔍 Onde executar:

Dentro da pasta raiz do projeto `api-dio-gym`

### ⚙️ Comandos:

```bash
# Criar um novo ambiente virtual (caso ainda não exista)
python -m venv venv

# Ativar (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar (CMD)
venv\Scripts\activate.bat

# Ativar (Linux/macOS)
source venv/bin/activate
```

---

## 📁 Instalação de dependências

### ✉ Função:

Instala todas as bibliotecas listadas no `requirements.txt`

### 🔍 Onde executar:

Dentro da pasta raiz `api-dio-gym` (onde está o `requirements.txt`)

### ⚙️ Comando:

```bash
pip install -r requirements.txt
```

Caso não exista o arquivo `requirements.txt`, crie-o com:

```bash
pip freeze > requirements.txt
```

---

## ⚡ Execução da API com Uvicorn

### ✉ Função:

Inicializa o servidor ASGI que roda o FastAPI, com hot-reload em modo desenvolvimento.

### 🔍 Onde executar:

#### Opção 1: Da raiz do projeto (`api-dio-gym`)

```bash
uvicorn workout_api.main:app --reload
```

- **Por quê?** Aqui você está acessando o arquivo `main.py` que está dentro da pasta `workout_api/`.

#### Opção 2: De dentro da pasta `workout_api/`

```bash
cd workout_api
uvicorn main:app --reload
```

- **Por quê?** Você já está dentro da pasta onde está `main.py`, então não precisa do prefixo `workout_api.`

---

## 🔄 Atualizar o pip (opcional)

### ✉ Função:

Mantém o `pip` atualizado para evitar erros de instalação de pacotes.

### 🔍 Onde executar:

Com ambiente virtual ativado, em qualquer diretório do projeto.

### ⚙️ Comando:

```bash
python -m pip install --upgrade pip
```

---

## ✅ Checklist rápido

| Objetivo                     | Diretório onde executar       | Comando                                 |
| ---------------------------- | ----------------------------- | --------------------------------------- |
| Criar ambiente virtual       | `api-dio-gym/`                | `python -m venv venv`                   |
| Ativar ambiente (PowerShell) | `api-dio-gym/`                | `.\venv\Scripts\Activate.ps1`           |
| Instalar dependências        | `api-dio-gym/`                | `pip install -r requirements.txt`       |
| Rodar API (modo 1 - raiz)    | `api-dio-gym/`                | `uvicorn workout_api.main:app --reload` |
| Rodar API (modo 2 - interno) | `api-dio-gym/workout_api/`    | `uvicorn main:app --reload`             |
| Gerar requirements.txt       | `api-dio-gym/`                | `pip freeze > requirements.txt`         |
| Atualizar pip (opcional)     | Qualquer pasta com venv ativo | `python -m pip install --upgrade pip`   |

---

Se quiser usar Docker, posso gerar um guia semelhante com `Dockerfile`, `docker-compose.yml` e variáveis de ambiente.

