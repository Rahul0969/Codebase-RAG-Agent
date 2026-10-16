# Codebase RAG Assistant

A local-first assistant for exploring repositories, searching code by meaning, and answering questions with source-file evidence. This repository is being built incrementally for learning and local development.

## Current status

Commit 1 establishes the FastAPI API and React + Vite interface. Repository indexing, embeddings, Chroma, Ollama, tree-sitter, and MCP are not implemented yet.

## Prerequisites

- Python 3.14 
- Node.js 20.19+ or 22.12+ (recommended for current Vite releases)
- Git

Check your installations in PowerShell:

```powershell
python --version
node --version
npm --version
git --version
```

## Run the backend (PowerShell terminal 1)

From the repository root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

If PowerShell blocks virtual-environment activation, you can run the venv's Python directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Check these URLs in your browser:

- http://127.0.0.1:8000/ — welcome response
- http://127.0.0.1:8000/health — health check
- http://127.0.0.1:8000/docs — interactive API documentation

## Run the frontend (PowerShell terminal 2)

From the repository root in a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite, usually http://localhost:5173. Select **Check connection**; the status should change to **Connected** while the backend is running.

## Commit 1 checks

Backend health check:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

Frontend production build (run from `frontend/`):

```powershell
npm run build
```

