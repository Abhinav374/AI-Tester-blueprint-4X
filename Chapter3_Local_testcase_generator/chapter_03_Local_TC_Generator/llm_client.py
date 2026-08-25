import requests


class LLMError(Exception):
    """Raised when generation fails on every provider."""


def _call_ollama(prompt: str, cfg: dict) -> str:
    url = f"{cfg['OLLAMA_URL'].rstrip('/')}/api/generate"
    payload = {"model": cfg["OLLAMA_MODEL"], "prompt": prompt, "stream": False}
    resp = requests.post(url, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.json().get("response", "")


def _call_groq(prompt: str, cfg: dict) -> str:
    if not cfg.get("GROQ_API_KEY"):
        raise LLMError("Groq API key is missing (set it in Settings).")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {cfg['GROQ_API_KEY']}",
        "Content-Type": "application/json",
    }
    body = {
        "model": cfg.get("GROQ_MODEL") or "openai/gpt-oss-20b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }
    resp = requests.post(url, headers=headers, json=body, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def generate(prompt: str, cfg: dict) -> str:
    """Generate with the selected provider; fall back Ollama -> Groq."""
    provider = cfg.get("PROVIDER", "ollama")

    if provider == "groq":
        try:
            return _call_groq(prompt, cfg)
        except (requests.RequestException, LLMError) as exc:
            return _call_ollama(prompt, cfg)  # fallback to local
    else:
        try:
            return _call_ollama(prompt, cfg)
        except (requests.RequestException, KeyError) as exc:
            # Ollama down — fall back to Groq
            return _call_groq(prompt, cfg)


def check_ollama_available(cfg: dict) -> bool:
    try:
        return bool(_call_ollama("ping", cfg))
    except (requests.RequestException, KeyError):
        return False