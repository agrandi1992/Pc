#!/usr/bin/env python3
"""
Check overlap between Power BI visual containers in PBIP/PBIR JSON files.
Usage:
    python check_powerbi_overlap.py /path/to/report_folder

The script searches recursively for JSON files containing visual layout properties:
    x, y, width, height
It reports overlapping rectangles inside the same page JSON folder.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

MIN_GAP = 8


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def iter_dicts(obj: Any) -> Iterable[Dict[str, Any]]:
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from iter_dicts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_dicts(v)


def extract_visuals(root: Path) -> List[Dict[str, Any]]:
    visuals: List[Dict[str, Any]] = []
    for path in root.rglob("*.json"):
        data = load_json(path)
        if data is None:
            continue
        for d in iter_dicts(data):
            keys = set(d.keys())
            if {"x", "y", "width", "height"}.issubset(keys):
                try:
                    x = float(d["x"])
                    y = float(d["y"])
                    w = float(d["width"])
                    h = float(d["height"])
                    if w <= 0 or h <= 0:
                        continue
                except Exception:
                    continue
                name = str(d.get("name") or d.get("displayName") or d.get("id") or path.stem)
                page = infer_page(path)
                visuals.append({
                    "page": page,
                    "file": str(path.relative_to(root)),
                    "name": name,
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "right": x + w,
                    "bottom": y + h,
                })
    return visuals


def infer_page(path: Path) -> str:
    parts = path.parts
    for i, part in enumerate(parts):
        if part.lower() in {"pages", "sections"} and i + 1 < len(parts):
            return parts[i + 1]
    # Fallback: parent folder is usually the page or visual folder
    return path.parent.name


def overlap(a: Dict[str, Any], b: Dict[str, Any]) -> Tuple[float, float, float]:
    ow = max(0.0, min(a["right"], b["right"]) - max(a["x"], b["x"]))
    oh = max(0.0, min(a["bottom"], b["bottom"]) - max(a["y"], b["y"]))
    return ow, oh, ow * oh


def min_gap(a: Dict[str, Any], b: Dict[str, Any]) -> float:
    # Returns 0 if overlapping; otherwise best-effort minimum horizontal/vertical separation.
    ow, oh, area = overlap(a, b)
    if area > 0:
        return 0.0
    gaps = []
    if a["right"] <= b["x"]:
        gaps.append(b["x"] - a["right"])
    if b["right"] <= a["x"]:
        gaps.append(a["x"] - b["right"])
    if a["bottom"] <= b["y"]:
        gaps.append(b["y"] - a["bottom"])
    if b["bottom"] <= a["y"]:
        gaps.append(a["y"] - b["bottom"])
    return min(gaps) if gaps else 0.0


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python check_powerbi_overlap.py /path/to/report_folder", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    visuals = extract_visuals(root)
    if not visuals:
        print("No visual layout rectangles found. Check PBIP/PBIR structure or JSON keys.")
        return 1

    errors = []
    warnings = []
    for i, a in enumerate(visuals):
        for b in visuals[i + 1:]:
            if a["page"] != b["page"]:
                continue
            ow, oh, area = overlap(a, b)
            if area > 0:
                errors.append((a, b, ow, oh, area))
            else:
                gap = min_gap(a, b)
                if 0 < gap < MIN_GAP:
                    warnings.append((a, b, gap))

    print(f"Visuals found: {len(visuals)}")
    print(f"Overlap errors: {len(errors)}")
    print(f"Gap warnings < {MIN_GAP}px: {len(warnings)}")

    if errors:
        print("\nOVERLAP ERRORS")
        for a, b, ow, oh, area in errors[:200]:
            print(f"- Page={a['page']} | {a['name']} ({a['file']}) overlaps {b['name']} ({b['file']}) | width={ow:.1f}, height={oh:.1f}, area={area:.1f}")
    if warnings:
        print("\nGAP WARNINGS")
        for a, b, gap in warnings[:200]:
            print(f"- Page={a['page']} | {a['name']} near {b['name']} | gap={gap:.1f}px")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
