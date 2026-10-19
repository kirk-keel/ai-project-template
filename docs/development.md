# Development

## Setup

```bash
make setup
```

## Common tasks

```bash
make up        # start the stack
make down      # stop it
make logs      # tail logs
make lint      # ruff + black --check
make fmt       # auto-format
make test      # pytest
make security  # gitleaks
```

## Adding a dependency

1. Add it to `requirements.txt` (or `requirements-dev.txt`).
2. Run `make setup`.

Dependabot will keep it current.
