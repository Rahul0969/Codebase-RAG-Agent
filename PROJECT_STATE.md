# PROJECT_STATE.md

## Roadmap
1. C1 — Project foundation
2. C2 — Safe repository inspection
3. C3 — Tree-sitter AST-aware code chunking
4. C4 — Sentence-transformers embeddings and Chroma indexing
5. C5 — Semantic code search
6. C6 — Ollama-powered RAG
7. C7 — Source citations and evidence validation
8. C8 — MCP server and repository tools
9. C9 — API integration and end-to-end testing
10. C10 — Security, documentation, deployment and final frontend design

## Current commit
C3 — Implementation delivered; local dependency installation and verification pending.

## Done so far
- C1 foundation created.
- C2 safe repository inspection and API endpoint added.
- C2 included nine unit tests; they passed in the original build environment.
- C3 added Tree-sitter-based syntax-aware chunking.
- C3 added `POST /repository/chunk`.
- Chunks preserve relative paths, language, syntax kind, optional symbol, and 1-based line ranges.
- Oversized definitions split on line boundaries; files without recognized definitions use module fallback chunks.
- Added C3 unit tests and updated README.

## Decisions
- React + Vite frontend; keep it minimal until backend functionality is complete.
- FastAPI backend.
- sentence-transformers embeddings.
- Ollama local LLM.
- Chroma vector database.
- Tree-sitter AST-aware chunking.
- MCP server exposing repository tools.
- Keras only for an optional reranker.
- Free and local-first; no paid APIs.
- Keep early dependencies and runtime light for a Windows machine with 4 GB RAM.
- One commit at a time.

## Open issues
- Install the new Tree-sitter language-pack dependency on the user's Windows machine.
- Run the full test suite and manually test `POST /repository/chunk`.
- C3 has not been committed in the user's local Git repository.
- Proceed to C4 only after C3 verification.

## Last model + what it did
GPT-6: built the C3 code-chunking implementation, API endpoint, unit tests, and documentation. The current build environment had no network access and did not have Tree-sitter installed, so real-grammar parsing was not executed here; tests use a mocked parser and must be verified locally after installing requirements.
