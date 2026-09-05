import json
from pathlib import Path

CONFIG_FILE = Path("config.json")
DEFAULT_CONFIG = {"wordlist_path": "word_list.txt"}

STATS_FILE = Path("stats.json")
DEFAULT_STATS = {
    "games_played":0,
    "wins":0,
    "losses":0,
}

def load_config() -> dict:
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config_data: dict) -> None:
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=4)

def load_stats() -> dict:
    if not STATS_FILE.exists():
        return DEFAULT_STATS

    with open(STATS_FILE, "r") as f:
        return json.load(f)

def save_stats(stats: dict) -> None:
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)
