# Architecture

```mermaid
flowchart LR
    C[Client] -->|Tailscale| A[App]
    A --> G[LiteLLM]
    G --> O[Ollama]
```

Client -> app -> gateway -> model. Nothing exposed publicly.
