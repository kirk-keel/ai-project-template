#!/usr/bin/env bash
set -euo pipefail
cp -n .env.example .env || true
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install
echo "Ready. Edit .env, then: make up"
