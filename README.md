# Fastapi-Celery-Cookiecutter

### <b>Usage :</b>
- JWT secret key  (HS256)
```
openssl rand -hex 32
```
- [Create Sentry project](https://sentry.io/)
- Pre-commmit install
```
poetry run pre-commit install
```
### <b>Content :</b>
- FastAPI
  - uvicorn
  - gunicorn
- Postgres
  - tortoise-rom
  - aerich
- Redis
  - aioredis
