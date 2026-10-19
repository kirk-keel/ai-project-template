.RECIPEPREFIX = >
.PHONY: setup up down logs test lint fmt security clean

setup:
> cp -n .env.example .env || true
> pip install -r requirements.txt -r requirements-dev.txt
> pre-commit install

up:
> docker compose up -d --build

down:
> docker compose down

logs:
> docker compose logs -f

test:
> pytest -q

lint:
> ruff check src tests
> black --check src tests

fmt:
> ruff check --fix src tests
> black src tests

security:
> gitleaks detect --source . --redact -v

clean:
> docker compose down -v
