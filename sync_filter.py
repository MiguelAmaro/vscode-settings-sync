import json
import sys
from pathlib import Path

import json5

SAFE_PREFIXES = (
    "editor.",
    "diffEditor.",
    "accessibility.",
    "workbench.",
    "window.",
    "files.",
    "search.",
    "explorer.",
    "breadcrumbs.",
    "terminal.",
)

def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])

    with src.open("r", encoding="utf-8") as f:
        settings = json5.load(f)

    sanitized = {
        key: value
        for key, value in settings.items()
        if key.startswith(SAFE_PREFIXES)
    }

    dst.parent.mkdir(parents=True, exist_ok=True)

    with dst.open("w", encoding="utf-8") as f:
        json.dump(sanitized, f, indent=4, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    main()