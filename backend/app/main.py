from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Codebase RAG Assistant API",
    description="Local-first API for understanding and searching code repositories.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/", tags=["health"])
def root() -> dict[str, str]:
    """Basic welcome endpoint."""
    return {"message": "Codebase RAG Assistant API is running."}


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Lightweight health check for local development."""
    return {"status": "ok"}
