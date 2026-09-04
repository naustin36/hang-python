import json
from pathlib import Path

CONFIG_FILE = Path("config.json")
DEFAULT_CONFIG = {"wordlist_path": "word_list.txt"}

def validate_file(file_path: str) -> bool | None:
    if not file_path.endswith(".txt"):
        raise ValueError("Filetype must be .txt")
    if len(file_path[0:-4]) == 0:
        raise ValueError("File name must not be blank")
    return True

def load_config() -> dict:
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config_data: dict) -> None:
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=4)

def update_word_file(file_path: str) -> None:
    pass
