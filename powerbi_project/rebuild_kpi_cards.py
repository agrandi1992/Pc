#!/usr/bin/env python3
"""
Rebuild KPI card visuals in Power BI PBIP report.json files to match design specification.
"""

import json
import re
import copy
import sys
from pathlib import Path

# ─── Spec constants ────────────────────────────────────────────────────────────

CARD_W = 286
CARD_H = 196

# X positions by card number (1-indexed)
CARD_X_POSITIONS = {1: 22, 2: 324, 3: 626, 4: 928, 5: 1230}

# Spec elements: (suffix, type, x_rel, y_rel, w, h, fill, z_offset)
# z_offset is local within the card (before adding card_z_base)
SPEC_ELEMENTS = [
    # suffix   type       x_rel  y_rel   w     h    fill        z_local
    ("BG",          "shape",   0,    0,    286, 196,  "#FFFFFF",   0),
    ("LEFT",        "shape",   0,    0,    4,   192,  "#0A4E97",   1),
    ("LBL",         "textbox", 18,   14,   175, 22,   None,        2),
    ("ICON",        "shape",   228,  12,   44,  44,   "#EAF3FF",   2),
    ("VAL",         "card",    18,   50,   170, 42,   None,        3),
    ("N1_BG",       "shape",   18,   97,   82,  22,   "#EAF3FF",   1),
    ("N1",          "textbox", 18,   97,   82,  22,   None,        4),
    ("M1_BG",       "shape",   104,  97,   88,  22,   "#EAF3FF",   1),
    ("M1",          "textbox", 104,  97,   88,  22,   None,        4),
    ("BUDGET_TRACK","shape",   18,   138,  251, 6,    "#E8EEF5",   1),
    ("BUDGET_FILL", "shape",   18,   138,  80,  6,    "#0A4E97",   5),
    ("EXCEL_BG",    "shape",   18,   152,  110, 20,   "#EAF3FF",   1),
    ("EXCEL",       "textbox", 18,   152,  110, 20,   None,        5),
    ("BIM_BG",      "shape",   132,  152,  140, 20,   "#EAF7EF",   1),  # default; overridden per BIM text
    ("BIM",         "textbox", 132,  152,  140, 20,   None,        5),
    ("SEP",         "shape",   0,    194,  286, 2,    "#F1F5F9",   2),
]

# All suffix names we manage (for deletion)
MANAGED_SUFFIXES = {
    "BG", "LEFT", "LBL", "ICON", "VAL",
    "N1_BG", "N1", "M1_BG", "M1",
    "BUDGET_TRACK", "BUDGET_FILL",
    "EXCEL_BG", "EXCEL", "BIM_BG", "BIM",
    "SEP"
}

FILES = [
    "/home/user/Pc/powerbi_project/pack_projet_independant_pilotage_commercial_pbip/06_Livrables_attendus/Pilotage_Commercial.Report/report.json",
    "/home/user/Pc/powerbi_project/pack_projet_independant_pilotage_commercial_pbip/07_Livrable_Sans_Affaires/Pilotage_Commercial.Report/report.json",
]

# ─── Helper: build shape visual container ─────────────────────────────────────

def make_shape_vc(name, x, y, z, w, h, fill_color, extra_objects=None):
    """Build a shape visual container dict."""
    objects = {
        "line": [{
            "properties": {
                "strokeWidth": {"expr": {"Literal": {"Value": "0D"}}}
            },
            "selector": {"id": "default"}
        }],
        "fill": [{
            "properties": {
                "fillColor": {
                    "solid": {
                        "color": {
                            "expr": {
                                "Literal": {
                                    "Value": f"'{fill_color}'"
                                }
                            }
                        }
                    }
                },
                "show": {"expr": {"Literal": {"Value": "true"}}}
            },
            "selector": {"id": "default"}
        }]
    }
    if extra_objects:
        objects.update(extra_objects)

    config = {
        "name": name,
        "layouts": [{
            "id": 0,
            "position": {
                "x": x, "y": y, "z": z,
                "height": h, "width": w,
                "tabOrder": z
            }
        }],
        "singleVisual": {
            "visualType": "shape",
            "objects": objects,
            "drillFilterOtherVisuals": True
        }
    }
    return {
        "x": x, "y": y, "z": z, "width": w, "height": h,
        "config": json.dumps(config, ensure_ascii=False),
        "filters": "[]"
    }


# ─── Helper: build textbox visual container ───────────────────────────────────

def make_textbox_vc(name, x, y, z, w, h, text, bold, font_size, color):
    """Build a textbox visual container dict."""
    config = {
        "name": name,
        "layouts": [{
            "id": 0,
            "position": {
                "x": x, "y": y, "z": z,
                "height": h, "width": w,
                "tabOrder": z
            }
        }],
        "singleVisual": {
            "visualType": "textbox",
            "objects": {
                "general": [{
                    "properties": {
                        "paragraphs": [{
                            "textRuns": [{
                                "value": text,
                                "textStyle": {
                                    "bold": bold,
                                    "fontFamily": "Segoe UI",
                                    "fontSize": font_size,
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": f"'{color}'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "fontWeight": "Bold" if bold else "Normal"
                                }
                            }],
                            "horizontalTextAlignment": "Left"
                        }]
                    }
                }]
            }
        }
    }
    return {
        "x": x, "y": y, "z": z, "width": w, "height": h,
        "config": json.dumps(config, ensure_ascii=False),
        "filters": "[]"
    }


# ─── Helper: build card VAL visual container ──────────────────────────────────

def make_val_vc(name, x, y, z, w, h, existing_val_cfg):
    """Build a card VAL visual container, preserving prototypeQuery from existing."""
    # Deep-copy the existing singleVisual config
    existing_sv = existing_val_cfg.get("singleVisual", {})
    new_sv = copy.deepcopy(existing_sv)
    new_sv["visualType"] = "card"

    config = {
        "name": name,
        "layouts": [{
            "id": 0,
            "position": {
                "x": x, "y": y, "z": z,
                "height": h, "width": w,
                "tabOrder": z
            }
        }],
        "singleVisual": new_sv
    }
    return {
        "x": x, "y": y, "z": z, "width": w, "height": h,
        "config": json.dumps(config, ensure_ascii=False),
        "filters": "[]"
    }


# ─── Extract text from textbox config ─────────────────────────────────────────

def extract_textbox_text(cfg):
    """Safely extract text value from textbox config."""
    try:
        paragraphs = cfg["singleVisual"]["objects"]["general"][0]["properties"]["paragraphs"]
        texts = []
        for para in paragraphs:
            for run in para.get("textRuns", []):
                texts.append(run.get("value", ""))
        return " ".join(texts).strip()
    except (KeyError, IndexError, TypeError):
        return ""


# ─── Determine BIM_BG color from BIM text ─────────────────────────────────────

def bim_bg_color(bim_text):
    """Return background color based on BIM text content."""
    normalized = bim_text.lower().replace("\xa0", " ").strip()
    if "bim ok" in normalized:
        return "#EAF7EF"
    elif "placeholder" in normalized:
        return "#FFF3E8"
    else:
        return "#EAF3FF"


# ─── Process a single section ─────────────────────────────────────────────────

def process_section(section, file_label, section_idx):
    """
    Process all KPI cards in a section.
    Returns (new_visual_containers, stats_dict).
    """
    visuals = section.get("visualContainers", [])
    section_name = section.get("displayName", f"Section {section_idx}")

    # ── Step 1: Parse all existing visuals, split KPI vs non-KPI ──────────────
    non_kpi = []
    kpi_by_num = {}  # card_num (int) -> {suffix -> (vc, cfg)}

    kpi_pattern = re.compile(r'^KPI_(\d+)_(.+)$')

    for vc in visuals:
        try:
            cfg = json.loads(vc.get("config", "{}"))
        except json.JSONDecodeError:
            non_kpi.append(vc)
            continue

        name = cfg.get("name", "")
        m = kpi_pattern.match(name)
        if m:
            num = int(m.group(1))
            suffix = m.group(2)
            if num not in kpi_by_num:
                kpi_by_num[num] = {}
            kpi_by_num[num][suffix] = (vc, cfg)
        else:
            non_kpi.append(vc)

    if not kpi_by_num:
        print(f"  [{file_label}] Section {section_idx} ({section_name}): no KPI visuals found, skipping.")
        return visuals, {"sections_processed": 0, "cards_processed": 0, "visuals_created": 0, "visuals_deleted": 0}

    stats = {
        "sections_processed": 1,
        "cards_processed": 0,
        "visuals_created": 0,
        "visuals_deleted": 0,
    }

    # ── Step 2: For each card number, build new visuals ────────────────────────
    new_kpi_vcs = []

    for card_num in sorted(kpi_by_num.keys()):
        card_data = kpi_by_num[card_num]
        stats["visuals_deleted"] += len(card_data)

        # Card position
        card_x = CARD_X_POSITIONS.get(card_num)
        if card_x is None:
            print(f"  [{file_label}] Section {section_idx} ({section_name}): card_num={card_num} has no X mapping, skipping.")
            # Keep existing visuals
            for suffix, (vc, cfg) in card_data.items():
                new_kpi_vcs.append(vc)
            stats["visuals_deleted"] -= len(card_data)
            continue

        # Get Y from existing BG
        bg_vc, bg_cfg = card_data.get("BG", (None, None))
        if bg_vc is not None:
            card_y = bg_vc.get("y", 305)
        else:
            # Fallback: infer from any existing visual
            any_vc = next(iter(card_data.values()))[0]
            card_y = any_vc.get("y", 305)
            print(f"  [{file_label}] Section {section_idx} ({section_name}): KPI_{card_num} missing BG, using y={card_y} from other visual.")

        # Extract preserved content
        # LBL text
        lbl_text = ""
        if "LBL" in card_data:
            lbl_text = extract_textbox_text(card_data["LBL"][1])
        if not lbl_text:
            lbl_text = f"KPI {card_num}"
            print(f"  [{file_label}] Section {section_idx} ({section_name}): KPI_{card_num}_LBL missing or empty, using fallback '{lbl_text}'.")

        # N1 text
        n1_text = "Vs N-1 —"
        if "N1" in card_data:
            extracted = extract_textbox_text(card_data["N1"][1])
            if extracted:
                n1_text = extracted

        # M1 text
        m1_text = "Vs MTD-1 —"
        if "M1" in card_data:
            extracted = extract_textbox_text(card_data["M1"][1])
            if extracted:
                m1_text = extracted

        # EXCEL text
        excel_text = "Excel G.x"
        if "EXCEL" in card_data:
            extracted = extract_textbox_text(card_data["EXCEL"][1])
            if extracted:
                excel_text = extracted

        # BIM text
        bim_text = "BIM placeholder"
        if "BIM" in card_data:
            extracted = extract_textbox_text(card_data["BIM"][1])
            if extracted:
                bim_text = extracted

        # BIM_BG color based on BIM text
        bim_fill = bim_bg_color(bim_text)

        # VAL config (preserved)
        val_existing_cfg = None
        if "VAL" in card_data:
            val_existing_cfg = card_data["VAL"][1]

        # card_z_base
        card_z_base = card_num * 10

        # ── Step 3: Create new visuals ─────────────────────────────────────────
        for suffix, vtype, x_rel, y_rel, w, h, fill, z_local in SPEC_ELEMENTS:
            x = card_x + x_rel
            y = card_y + y_rel
            z = card_z_base + z_local
            name = f"KPI_{card_num}_{suffix}"

            if vtype == "shape":
                # Override BIM_BG fill based on BIM text
                actual_fill = bim_fill if suffix == "BIM_BG" else fill
                vc = make_shape_vc(name, x, y, z, w, h, actual_fill)

            elif vtype == "textbox":
                if suffix == "LBL":
                    vc = make_textbox_vc(name, x, y, z, w, h, lbl_text, True, "10pt", "#667085")
                elif suffix == "N1":
                    vc = make_textbox_vc(name, x, y, z, w, h, n1_text, True, "9pt", "#0A4E97")
                elif suffix == "M1":
                    vc = make_textbox_vc(name, x, y, z, w, h, m1_text, True, "9pt", "#0A4E97")
                elif suffix == "EXCEL":
                    vc = make_textbox_vc(name, x, y, z, w, h, excel_text, True, "8pt", "#0A4E97")
                elif suffix == "BIM":
                    vc = make_textbox_vc(name, x, y, z, w, h, bim_text, True, "8pt", "#0A4E97")
                else:
                    vc = make_textbox_vc(name, x, y, z, w, h, "", False, "9pt", "#333333")

            elif vtype == "card":
                if val_existing_cfg is not None:
                    vc = make_val_vc(name, x, y, z, w, h, val_existing_cfg)
                else:
                    # No existing VAL — create a minimal card placeholder
                    print(f"  [{file_label}] Section {section_idx} ({section_name}): KPI_{card_num}_VAL missing, creating placeholder card.")
                    config = {
                        "name": name,
                        "layouts": [{
                            "id": 0,
                            "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": z}
                        }],
                        "singleVisual": {
                            "visualType": "card",
                            "objects": {
                                "labels": [{
                                    "properties": {
                                        "fontSize": {"expr": {"Literal": {"Value": "'16pt'"}}},
                                        "bold": {"expr": {"Literal": {"Value": "true"}}},
                                        "color": {"solid": {"color": {"expr": {"Literal": {"Value": "'#0A4E97'"}}}}}
                                    }
                                }],
                                "categoryLabels": [{
                                    "properties": {
                                        "show": {"expr": {"Literal": {"Value": "false"}}}
                                    }
                                }]
                            },
                            "drillFilterOtherVisuals": True
                        }
                    }
                    vc = {
                        "x": x, "y": y, "z": z, "width": w, "height": h,
                        "config": json.dumps(config, ensure_ascii=False),
                        "filters": "[]"
                    }
            else:
                continue

            new_kpi_vcs.append(vc)
            stats["visuals_created"] += 1

        stats["cards_processed"] += 1
        print(f"  [{file_label}] Section {section_idx} ({section_name}): KPI_{card_num} rebuilt at x={card_x}, y={card_y} (bim='{bim_text}', bim_bg='{bim_fill}')")

    # Combine non-KPI + new KPI
    section["visualContainers"] = non_kpi + new_kpi_vcs
    return section["visualContainers"], stats


# ─── Process a single file ────────────────────────────────────────────────────

def process_file(filepath):
    """Load, process, validate, and save a report.json file."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}")
        return False

    print(f"\n{'='*70}")
    print(f"Processing: {filepath}")
    print(f"{'='*70}")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_stats = {
        "sections_processed": 0,
        "cards_processed": 0,
        "visuals_created": 0,
        "visuals_deleted": 0,
    }

    file_label = path.parent.parent.parent.name  # e.g. 06_Livrables_attendus

    for i, section in enumerate(data.get("sections", [])):
        _, stats = process_section(section, file_label, i)
        for k in total_stats:
            total_stats[k] += stats.get(k, 0)

    # ── Validate JSON ──────────────────────────────────────────────────────────
    try:
        serialized = json.dumps(data, ensure_ascii=False, indent=2)
        json.loads(serialized)  # re-parse to confirm valid
    except (json.JSONDecodeError, ValueError) as e:
        print(f"ERROR: JSON validation failed for {filepath}: {e}")
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(serialized)

    print(f"\nSummary for {file_label}:")
    print(f"  Sections processed:  {total_stats['sections_processed']}")
    print(f"  Cards rebuilt:       {total_stats['cards_processed']}")
    print(f"  Visuals deleted:     {total_stats['visuals_deleted']}")
    print(f"  Visuals created:     {total_stats['visuals_created']}")
    print(f"  File saved OK:       {filepath}")
    return True


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    success = True
    for filepath in FILES:
        ok = process_file(filepath)
        if not ok:
            success = False

    print(f"\n{'='*70}")
    if success:
        print("ALL FILES PROCESSED SUCCESSFULLY.")
    else:
        print("ONE OR MORE FILES HAD ERRORS — review output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
