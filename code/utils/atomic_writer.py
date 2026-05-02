import os
import json
import tempfile
import time

def atomic_write_json(filepath: str, data: dict) -> None:
    dir_path = os.path.dirname(filepath)
    with tempfile.NamedTemporaryFile(
        mode='w', dir=dir_path, suffix='.tmp',
        delete=False, encoding='utf-8'
    ) as tmp:
        json.dump(data, tmp, ensure_ascii=False, indent=2)
        tmp_path = tmp.name
    os.replace(tmp_path, filepath)

def safe_read_json(filepath: str, max_retries: int = 3) -> dict:
    for attempt in range(max_retries):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            if attempt == max_retries - 1:
                raise
            time.sleep(0.1)
