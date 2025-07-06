# Frontend

## Instalação

Execute os comandos abaixo a partir da raiz do projeto para instalar as dependências do frontend e do backend:

```bash
npm install
pip install -r backend/requirements.txt
```

## Configuração do `.env`

No diretório `frontend`, ajuste o arquivo `.env` informando a variável `VITE_API_URL` com o endereço da API. Exemplo:

```
VITE_API_URL=http://localhost:8000
```

## Execução

Use dois terminais para iniciar cada parte do projeto:

```bash
# Backend
uvicorn backend.main:app --reload

# Frontend
cd frontend && npm run dev
```
