# MVP-4

## Setup

### Backend

Use Python 3.11+.

```bash
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## Execução

Abra dois terminais para iniciar backend e frontend separadamente:

```bash
# Backend
uvicorn backend.main:app --reload

# Frontend
cd frontend && npm run dev
```

## Testes

Execute os testes automatizados com o `pytest` na raiz do projeto:

```bash
pytest
```

