import json
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
CONFIG_PATH = BASE_DIR / "config.json"

load_dotenv(ENV_PATH)

# Keys persisted in config.json and/or .env
_KEYS = [
    "JIRA_URL",
    "JIRA_EMAIL",
    "JIRA_API_TOKEN",
    "GROQ_API_KEY",
    "OLLAMA_URL",
    "OLLAMA_MODEL",
    "GROQ_MODEL",
    "PROVIDER",  # "ollama" | "groq"
]


def _defaults():
    """Seed from .env; PROVIDER defaults to ollama."""
    cfg = {k: os.getenv(k, "") for k in _KEYS if k != "PROVIDER"}
    cfg["PROVIDER"] = os.getenv("PROVIDER", "ollama")
    return cfg


def read_config():
    """Return persisted settings, falling back to .env seeds."""
    if CONFIG_PATH.exists():
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            data = {}
    else:
        data = {}

    cfg = _defaults()
    cfg.update({k: v for k, v in data.items() if k in _KEYS})
    return cfg


def write_config(updates: dict) -> dict:
    """Merge updates into the current config and persist; returns full config."""
    cfg = read_config()
    cfg.update({k: v for k, v in updates.items() if k in _KEYS})
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
    return cfg