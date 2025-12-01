# Micro SaaS Engenharia de Software

Este projeto é um Micro SaaS para gestão de serviços de desenvolvimento de software.
Backend em Django (Python) e Frontend em Vue.js.

## Pré-requisitos

- Python 3.8+
- Node.js 16+
- Ambiente virtual configurado na pasta `.venv`

## Como Rodar

### 1. Backend (Django)

Ative o ambiente virtual e instale as dependências (se ainda não fez):

```bash
# Windows
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Rode as migrações do banco de dados:

```bash
python manage.py migrate
```

Crie um superusuário para acessar o admin:

```bash
python manage.py createsuperuser
```

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

O backend estará rodando em `http://127.0.0.1:8000`.
Acesse o admin em `http://127.0.0.1:8000/admin`.

### 2. Frontend (Vue.js)

Navegue até a pasta `frontend` e instale as dependências:

```bash
cd frontend
npm install
```

Inicie o servidor de desenvolvimento:

```bash
npm run dev
```

O frontend estará rodando geralmente em `http://localhost:5173`.

## Funcionalidades

- **Admin**: Gestão de visitas, clientes, financeiro, manutenções e notificações.
- **Cliente**: Visualização de status de implantação e pagamentos.

## Estrutura

- `config/`: Configurações do projeto Django.
- `gestao/`: App Django com a lógica de negócios.
- `frontend/`: Projeto Vue.js.
