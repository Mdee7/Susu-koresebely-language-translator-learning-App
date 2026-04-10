# Repository Structure

This repository follows the requested layout:

- `/app`
  - `/screens`
  - `/components`
  - `/assets`
  - `/fonts`
- `/Frontend`
  - `/HTML/JS`
  - `/CDN` (fonts & assets)
- `/backend`
  - `/python-services` (Flask + Gunicorn)
  - `/nginx` (reverse proxy config)
  - Docker container setup is optional and can be added later.
- `/data`
  - `/dictionary`
  - `/audio`
  - `/script`
  - `/embeddings`
- `/docs`
  - `README.md`

## Notes

- The existing MVP API artifacts remain in the repository.
- The new `backend/python-services` path provides the requested Flask/Gunicorn structure.
