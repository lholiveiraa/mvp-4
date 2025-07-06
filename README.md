# MVP-4

Este projeto é uma aplicação web para predição de doença cardíaca.
O backend em FastAPI carrega um modelo de machine learning e oferece uma rota `/predict`.
O frontend, feito em React, permite enviar os dados do paciente e visualizar o resultado.
O objetivo e demonstrar um MVP integrando modelo de ML, API e interface web.

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

