from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .repository import inspect_repository

app = FastAPI(
    title="Codebase RAG Assistant API",
    description="Local-first API for understanding and searching code repositories.",
    version="0.2.0",
)

# Vite's development server runs on port 5173 by default.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


class RepositoryRequest(BaseModel):
    repository_path: str = Field(min_length=1, max_length=4096)


@app.get("/", tags=["health"])
def root() -> dict[str, str]:
    """Basic welcome endpoint."""
    return {"message": "Codebase RAG Assistant API is running."}


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Lightweight health check for local development."""
    return {"status": "ok"}


@app.post("/repository/inspect", tags=["repository"])
def inspect_repository_endpoint(request: RepositoryRequest) -> dict:
    """List supported source-file paths in a selected local repository."""
    try:
        return inspect_repository(request.repository_path)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
