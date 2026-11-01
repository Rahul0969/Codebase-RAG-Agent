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
10. C10 — Security, documentation, and final frontend design

## Current commit
C2 — Safe repository inspection implemented. Automated tests and local API verification are included; the user's Windows environment still needs to run them.

## Done so far
- Created the initial FastAPI and React + Vite foundation (C1).
- Kept the frontend intentionally minimal while backend development takes priority.
- Added `backend/app/repository.py` to list supported repository file paths without reading file contents.
- Added `POST /repository/inspect` with request validation and HTTP 400 handling for invalid paths.
- Added safeguards for ignored dependency/build/cache folders, symlinks/junctions, common environment files, and common private-key files.
- Limited scans to 5,000 files and 20 directory levels.
- Added nine unit tests using Python's built-in `unittest`.
- Updated README with setup, API usage, safety notes, and test instructions.

## Decisions made
- React + Vite frontend; keep it plain until backend functionality is complete.
- FastAPI backend.
- sentence-transformers embeddings.
- Ollama local LLM.
- Chroma vector database.
- tree-sitter AST-aware chunking.
- MCP server exposing repository tools.
- Keras only for an optional reranker.
- Free, local-first implementation with no paid APIs.
- Keep early dependencies and runtime light for a Windows machine with 4 GB RAM.
- One commit at a time; wait for the user to say "next" before advancing.

## Open issues
- Run the test suite and start the API on the user's Windows machine.
- Manually test `POST /repository/inspect` with a real local repository path.
- Keep the API bound to localhost; do not expose arbitrary filesystem inspection to an untrusted network.
- Assess available disk space and hardware before selecting local models.

## Last model + what it did
GPT-6, Coder: implemented C2 repository inspection, FastAPI endpoint, nine unit tests, minimal frontend styling, and updated documentation. Automated tests were run in the build environment; Windows-specific manual verification remains pending.
