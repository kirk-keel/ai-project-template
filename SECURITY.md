# Security Policy

## Reporting
Open an issue or email the maintainer.

## Threat model
- Local-first: models run on owned hardware.
- Private network: services reached over Tailscale, never exposed publicly.
- Secrets: `.env` gitignored; gitleaks scans history.
- Containers run non-root.
