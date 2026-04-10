# Starter Architecture

## Monorepo layout
- `apps/api`: FastAPI backend service (MVP).
- `packages/nlp`: reusable NLP/translation components.
- `data/dictionaries`: JSON lexical data and future metadata.
- `docs`: architecture and product docs.

## MVP milestones
1. API skeleton with health + translate endpoints.
2. Seed dictionary schema and loader.
3. Replace rule-based stub with retrieval and model-assisted translation.
4. Add auth, user progress, and content moderation pipelines.
