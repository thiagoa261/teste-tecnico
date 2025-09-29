# 📧 Sistema de Classificação de E-mails

Um sistema completo para classificação inteligente de e-mails utilizando FastAPI e Nuxt.js, com processamento automático via OpenAI GPT.

## 🏗️ Arquitetura do Projeto

```
📦 Email Classification System
├── 🐳 docker-compose.yml           # Orquestração dos containers
├── 🔧 api/                         # Backend FastAPI
│   ├── 📋 requirements.txt         # Dependências Python
│   ├── 🐳 Dockerfile              # Container da API
│   ├── 🔧 docker-compose.yml      # Redis para desenvolvimento
│   ├── ⚙️ .env.example            # Template de variáveis de ambiente
│   └── 📁 src/
│       ├── 🚀 main.py             # Aplicação principal
│       ├── 🎮 controllers/        # Controladores REST
│       │   ├── auth_controller.py
│       │   └── email_controller.py
│       ├── ⚡ core/               # Configurações centrais
│       │   ├── config.py
│       │   ├── guard.py
│       │   └── security.py
│       ├── 🗄️ db/                 # Conexões de banco
│       │   ├── mongo.py
│       │   └── redis.py
│       ├── 📊 models/             # Modelos de dados
│       │   ├── email_model.py
│       │   └── user_model.py
│       └── 🔧 services/           # Lógica de negócio
│           ├── auth_service.py
│           └── email_service.py
└── 🎨 app/                        # Frontend Nuxt.js
    ├── 📦 package.json            # Dependências Node.js
    ├── 🐳 Dockerfile             # Container do frontend
    ├── ⚙️ nuxt.config.ts          # Configuração do Nuxt
    ├── ⚙️ .env.example            # Template de variáveis de ambiente
    └── 📁 app/
        ├── 🏠 app.vue             # Componente raiz
        ├── 🎨 components/         # Componentes Vue
        ├── 📄 pages/              # Páginas da aplicação
        ├── 🛡️ middleware/         # Middlewares de rota
        ├── 📦 stores/            # Estado global (Pinia)
        └── 🔧 composables/       # Composables Vue
```

## 🚀 Tecnologias Utilizadas

### Backend (API)
- **FastAPI** - Framework web moderno e rápido
- **MongoDB** - Banco de dados NoSQL para persistência
- **Redis** - Cache e gerenciamento de sessões
- **OpenAI GPT** - Processamento inteligente de e-mails

### Frontend (App)
- **Nuxt.js 4** - Framework Vue.js full-stack
- **Vue 3** - Framework reativo para UI
- **Pinia** - Gerenciamento de estado
- **Nuxt UI** - Biblioteca de componentes
- **Axios** - Cliente HTTP

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- [Docker](https://www.docker.com/get-started)
- **MongoDB** (pode ser via Docker)
- **Redis** (pode ser via Docker)

## ⚙️ Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd teste-tecnico
```

### 2. Configure as variáveis de ambiente

#### Para a API (`api/.env`)
Copie o arquivo de exemplo e configure:
```bash
cp api/.env.example api/.env
```

Edite o arquivo `api/.env` com suas configurações:
```bash
# Duração da sessão (em segundos)
SESSION_DURATION=14400

# Configurações do MongoDB
MONGO_HOST=mongodb
MONGO_PORT=27017
MONGO_USER=admin
MONGO_PASS=password123
MONGO_DB=email_classification

# Configurações do Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=redis123

# Usuário administrador padrão
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123

# Configurações da OpenAI
GPT_API_TOKEN=sk-your-openai-api-key
GPT_MODEL=gpt-3.5-turbo
GPT_PROMPT=Classifique este email como: spam, importante, promocional, ou pessoal
```

#### Para o App (`app/.env`)
Copie o arquivo de exemplo e configure:
```bash
cp app/.env.example app/.env
```

Edite o arquivo `app/.env`:
```bash
# URL da API
API_URL=http://localhost:8000
```

### 3. Configure os bancos de dados

#### MongoDB
Certifique-se de ter uma instância do MongoDB rodando. Você pode usar Docker:
```bash
docker run -d --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:latest
```

#### Redis
Certifique-se de ter uma instância do Redis rodando. Você pode usar Docker:
```bash
docker run -d --name redis \
  -p 6379:6379 \
  -e REDIS_PASSWORD=redis123 \
  redis:latest redis-server --requirepass redis123
```

## 🚀 Execução

### Usando Docker Compose (Recomendado)

Execute o comando na raiz do projeto:
```bash
docker-compose up -d
```

Isso irá:
- 🔨 Construir as imagens dos containers
- 🚀 Iniciar a API na porta `8000`
- 🎨 Iniciar o frontend na porta `3000`

### Verificando se está funcionando

- **API**: http://localhost:8000
- **Documentação da API**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000

## 📖 Como usar

### 1. Acesso ao Sistema
- Acesse http://localhost:3000
- Faça login com as credenciais configuradas no arquivo `.env`

### 2. Classificação de E-mails
- **Upload de arquivo**: Envie arquivos PDF ou texto
- **Texto direto**: Cole o conteúdo do e-mail diretamente
- **Visualização**: Veja o resultado da classificação e justificativa

### 3. Histórico
- Consulte todos os e-mails que você salvou

## 🔧 Desenvolvimento

### Executar em modo de desenvolvimento

#### API
```bash
cd api
python -m venv nome_da_venv
nome_da_venv\Scripts\Activate
pip install -r requirements.txt
uvicorn src.main:api --reload --port 8000
```

#### Frontend
```bash
cd app
bun install
bun run dev
```

## 📊 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/auth/login` | Autenticação de usuário |
| POST | `/auth/logout` | Logout do usuário |
| POST | `/email/processar` | Processar e-mail via texto |
| POST | `/email/processar/file` | Processar e-mail via arquivo |
| POST | `/email/listar` | Listar e-mails processados |
| POST | `/email/salvar` | Salvar e-mail processado |

## 📝 Logs

Os logs dos containers podem ser visualizados com:
```bash
# Todos os serviços
docker-compose logs -f

# Apenas a API
docker-compose logs -f email-api

# Apenas o frontend
docker-compose logs -f email-app
```

## 🛑 Parar os serviços

```bash
docker-compose down
```