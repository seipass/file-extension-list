from __future__ import annotations
def run(paths):
 from pathlib import Path
 return [Path(p).suffix for p in paths]
