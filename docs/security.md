# Security

## Principles

- **Local-first** — models run on owned hardware; no data leaves the network by default.
- **Private network** — services are reached over Tailscale, never exposed publicly.
- **Least privilege** — containers run non-root; the app binds to `127.0.0.1`.
- **Defense in depth** — secrets are gitignored *and* scanned for in CI.

## Secrets

`.env` is never committed. `.env.example` documents every variable.
`gitleaks` runs in pre-commit and in CI against full history.

## Network

| Service | Binding | Reachable via |
| --- | --- | --- |
| app | 127.0.0.1:8000 | Tailscale |
| litellm | docker network | app only |
| ollama | docker network | litellm only |

## Reporting

See [SECURITY.md](../SECURITY.md).
