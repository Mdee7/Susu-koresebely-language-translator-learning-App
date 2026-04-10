# Susu-koresebely-language-translator-learning-App

A cross-platform language technology initiative for **Susu ↔ English ↔ Koré Sèbèli** translation, script learning, and AI-powered language tools.

## Starter structure

```text
.
├── apps/
│   └── api/                  # FastAPI service (MVP)
├── packages/
│   └── nlp/                  # translation and NLP modules
├── data/
│   └── dictionaries/         # lexical JSON datasets
└── docs/                     # architecture and roadmap docs
```

## Quickstart (local)

1. Create and activate a Python 3.11+ environment.
2. Install dependencies:

   ```bash
   pip install -e .[dev]
   ```

3. Run API:

   ```bash
   PYTHONPATH=apps/api:packages/nlp uvicorn app.main:app --reload
   ```

4. Run tests:

   ```bash
   PYTHONPATH=apps/api:packages/nlp pytest
   ```

## Current MVP endpoints

- `GET /health` — health check.
- `POST /v1/translate` — starter translator endpoint backed by a small in-memory lexicon stub.

## Next implementation targets

- Add dictionary loader from `data/dictionaries`.
- Add robust language code validation.
- Add persistence for phrasebook/progress.
- Introduce embedding + retrieval layer for semantic translation assist.
