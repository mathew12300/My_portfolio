import json
from django.conf import settings
from pathlib import Path

def load_projects():
    json_path = Path(settings.BASE_DIR) / "portfolio" / "data" / "projects.json"
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)

