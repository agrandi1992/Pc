#!/usr/bin/env python3
"""Generate the report.json for Pilotage Commercial PBIP project."""

import json
import uuid

REPORT_DEST = "/home/user/Pc/powerbi_project/pack_projet_independant_pilotage_commercial_pbip/06_Livrables_attendus/Pilotage_Commercial.Report/report.json"

def uid():
    return str(uuid.uuid4())

# ─────────────────────────────────────────────
# Helper: serialized config JSON
# ─────────────────────────────────────────────

def make_shape(x, y, w, h, fill_color, z=0, tab=0):
    config = {
        "name": uid(),
        "layouts": [{"id": 0, "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": tab}}],
        "singleVisual": {
            "visualType": "shape",
            "objects": {
                "line": [{"properties": {"strokeWidth": {"expr": {"Literal": {"Value": "0D"}}}}}],
                "fill": [{"properties": {"fillColor": {"solid": {"color": {"expr": {"Literal": {"Value": f"'{fill_color}'"}}}}}}}]
            }
        }
    }
    return {"x": x, "y": y, "z": z, "width": w, "height": h, "config": json.dumps(config), "filters": "[]"}

def make_textbox(x, y, w, h, text, bold=False, font_size="12pt", color="#000000", z=0, tab=0):
    text_style = {"fontSize": font_size, "color": {"solid": {"color": {"expr": {"Literal": {"Value": f"'{color}'"}}}}}}
    if bold:
        text_style["bold"] = True
    config = {
        "name": uid(),
        "layouts": [{"id": 0, "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": tab}}],
        "singleVisual": {
            "visualType": "textbox",
            "objects": {
                "general": [{"properties": {"paragraphs": [{"textRuns": [{"value": text, "textStyle": text_style}]}]}}]
            }
        }
    }
    return {"x": x, "y": y, "z": z, "width": w, "height": h, "config": json.dumps(config), "filters": "[]"}

def make_button(x, y, w, h, label, z=0, tab=0):
    config = {
        "name": uid(),
        "layouts": [{"id": 0, "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": tab}}],
        "singleVisual": {
            "visualType": "actionButton",
            "objects": {
                "text": [{"properties": {"text": {"expr": {"Literal": {"Value": f"'{label}'"}}}}}],
                "fill": [{"properties": {"show": {"expr": {"Literal": {"Value": "false"}}}}}]
            }
        }
    }
    return {"x": x, "y": y, "z": z, "width": w, "height": h, "config": json.dumps(config), "filters": "[]"}

def make_slicer(x, y, w, h, label="Slicer", z=0, tab=0):
    config = {
        "name": uid(),
        "layouts": [{"id": 0, "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": tab}}],
        "singleVisual": {
            "visualType": "slicer",
            "objects": {
                "general": [{"properties": {"outspace": {"expr": {"Literal": {"Value": "5D"}}}}}],
                "header": [{"properties": {"text": {"expr": {"Literal": {"Value": f"'{label}'"}}}}}]
            }
        }
    }
    return {"x": x, "y": y, "z": z, "width": w, "height": h, "config": json.dumps(config), "filters": "[]"}

def make_chart(x, y, w, h, chart_type="lineChart", title="", z=0, tab=0):
    config = {
        "name": uid(),
        "layouts": [{"id": 0, "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": tab}}],
        "singleVisual": {
            "visualType": chart_type,
            "objects": {
                "title": [{"properties": {"text": {"expr": {"Literal": {"Value": f"'{title}'"}}}}}]
            }
        }
    }
    return {"x": x, "y": y, "z": z, "width": w, "height": h, "config": json.dumps(config), "filters": "[]"}

def make_table(x, y, w, h, title="", z=0, tab=0):
    config = {
        "name": uid(),
        "layouts": [{"id": 0, "position": {"x": x, "y": y, "z": z, "height": h, "width": w, "tabOrder": tab}}],
        "singleVisual": {
            "visualType": "tableEx",
            "objects": {
                "title": [{"properties": {"text": {"expr": {"Literal": {"Value": f"'{title}'"}}}}}]
            }
        }
    }
    return {"x": x, "y": y, "z": z, "width": w, "height": h, "config": json.dumps(config), "filters": "[]"}

# ─────────────────────────────────────────────
# Common header builder
# ─────────────────────────────────────────────

NAV_LABELS = ["Accueil", "Performance", "Affaires", "Réseau MIA", "Rendez-vous", "Alertes", "Glossaire"]

def build_header(tab=0):
    visuals = []
    # Background white
    visuals.append(make_shape(0, 0, 1540, 88, "#FFFFFF", z=0, tab=tab))
    # Blue bottom line
    visuals.append(make_shape(0, 85, 1540, 3, "#0A4E97", z=1, tab=tab+1))
    # Title textbox
    visuals.append(make_textbox(20, 20, 240, 50, "Pilotage Commercial", bold=True, font_size="16pt", color="#0A4E97", z=2, tab=tab+2))
    # Nav buttons
    x = 280
    for i, label in enumerate(NAV_LABELS):
        visuals.append(make_button(x, 22, 100, 42, label, z=3+i, tab=tab+3+i))
        x += 105
    # Slicer perimetre
    visuals.append(make_slicer(1250, 20, 270, 42, "Périmètre", z=15, tab=tab+15))
    return visuals

def build_title_zone(page_title, page_subtitle, tab=0):
    visuals = []
    visuals.append(make_shape(20, 100, 1500, 120, "#0A4E97", z=0, tab=tab))
    visuals.append(make_textbox(40, 115, 400, 40, page_title, bold=True, font_size="20pt", color="#FFFFFF", z=1, tab=tab+1))
    visuals.append(make_textbox(40, 158, 600, 36, page_subtitle, bold=False, font_size="12pt", color="#FFFFFF", z=2, tab=tab+2))
    return visuals

def build_toolbar(tab=0):
    visuals = []
    visuals.append(make_slicer(20, 245, 460, 40, "Période", z=0, tab=tab))
    visuals.append(make_slicer(990, 245, 250, 40, "Axe Organisation", z=1, tab=tab+1))
    visuals.append(make_slicer(1250, 245, 270, 40, "Axe Activité", z=2, tab=tab+2))
    return visuals

KPI_LABELS = [
    ("Volume affaires prod.", 20, 287),
    ("Volume instance", 317, 287),
    ("Volume commissionnées", 614, 287),
    ("Montant moy. rétro", 911, 287),
    ("Nb RDV réalisés", 1208, 287),
]

def build_kpi_row(labels=None, y=305, tab=0):
    if labels is None:
        labels = KPI_LABELS
    visuals = []
    for i, (label, x, w) in enumerate(labels):
        t = tab + i * 10
        # background shape white
        visuals.append(make_shape(x, y, w, 150, "#FFFFFF", z=0, tab=t))
        # icon shape
        visuals.append(make_shape(x+10, y+10, 30, 30, "#E8EEF5", z=1, tab=t+1))
        # label
        visuals.append(make_textbox(x+50, y+10, w-60, 20, label, bold=False, font_size="10pt", color="#667085", z=2, tab=t+2))
        # valeur placeholder
        visuals.append(make_textbox(x+10, y+40, w-20, 40, "—", bold=True, font_size="22pt", color="#0A4E97", z=3, tab=t+3))
        # chip N-1
        visuals.append(make_textbox(x+10, y+90, 120, 22, "Vs N-1 —", bold=False, font_size="10pt", color="#667085", z=4, tab=t+4))
        # chip MTD-1
        visuals.append(make_textbox(x+140, y+90, 120, 22, "Vs MTD-1 —", bold=False, font_size="10pt", color="#667085", z=5, tab=t+5))
        # badge Excel
        visuals.append(make_textbox(x+10, y+122, 80, 20, "Excel: G." + str(i+1), bold=False, font_size="9pt", color="#667085", z=6, tab=t+6))
        # badge BIM
        visuals.append(make_textbox(x+100, y+122, 80, 20, "BIM: OK" if i >= 3 else "BIM: WIP", bold=False, font_size="9pt", color="#667085", z=7, tab=t+7))
    return visuals

# ─────────────────────────────────────────────
# Page builders
# ─────────────────────────────────────────────

def page_config(bg="#F1F5F9"):
    return json.dumps({
        "defaultLayout": {"displayState": {"mode": "default"}},
        "objects": {
            "section": [{"properties": {"background": {"solid": {"color": {"expr": {"Literal": {"Value": f"'{bg}'"}}}}}, "backgroundImage": {}, "wallpaper": {}}}]
        }
    })

def build_page_accueil():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Vue d'ensemble", "Performance commerciale, réseau et alertes", tab=20))
    vc.extend(build_toolbar(tab=30))
    # KPI row
    kpi_labels = [
        ("Volume affaires prod.", 20, 287),
        ("Volume instance", 317, 287),
        ("Volume commissionnées", 614, 287),
        ("Montant moy. rétro", 911, 287),
        ("Nb RDV réalisés", 1208, 287),
    ]
    vc.extend(build_kpi_row(kpi_labels, y=305, tab=40))
    # G04 gauges alertes (y=475)
    gauge_labels = [("Alerte Volume", 20, 480), ("Alerte RDV", 540, 480), ("Alerte Réseau", 1060, 480)]
    for (gl, gx, gy) in gauge_labels:
        vc.append(make_shape(gx, gy, 460, 130, "#FFFFFF", z=0))
        vc.append(make_textbox(gx+10, gy+10, 200, 30, gl, bold=True, font_size="12pt", color="#0A4E97"))
        vc.append(make_textbox(gx+10, gy+50, 200, 40, "NON DISPONIBLE", bold=True, font_size="16pt", color="#667085"))
    # G05 lignes alertes (y=625)
    alert_rows = [
        ("Alertes Critiques", "#D71920", 20, 625),
        ("Alertes Hautes", "#E67E22", 20, 660),
        ("Alertes Moyennes", "#F1C40F", 20, 695),
        ("Alertes Ouvertes", "#0A4E97", 20, 730),
    ]
    for (al, ac, ax, ay) in alert_rows:
        vc.append(make_shape(ax, ay, 480, 30, "#FFFFFF", z=0))
        vc.append(make_shape(ax, ay, 6, 30, ac, z=1))
        vc.append(make_textbox(ax+15, ay+5, 300, 22, al, bold=False, font_size="11pt", color="#1E293B"))
        vc.append(make_textbox(ax+370, ay+5, 100, 22, "—", bold=True, font_size="12pt", color="#1E293B"))
    # Recommandations (y=625, x=520)
    vc.append(make_shape(520, 625, 1000, 135, "#FFFFFF", z=0))
    vc.append(make_textbox(535, 630, 200, 22, "Recommandations", bold=True, font_size="11pt", color="#0A4E97"))
    vc.append(make_textbox(535, 660, 960, 90, "— Données affaires non disponibles. Intégrer fact_affaires pour activer les indicateurs de volume et de performance.", bold=False, font_size="10pt", color="#667085"))
    # G06 charts (y=780)
    vc.append(make_chart(20, 780, 735, 280, "lineChart", "Évolution affaires"))
    vc.append(make_chart(775, 780, 745, 280, "columnChart", "Répartition agences"))
    return vc

def build_page_performance():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Performance réseau", "Indicateurs de performance et trajectoire budgétaire", tab=20))
    # G02_Performance
    vc.append(make_slicer(20, 245, 980, 40, "FP Metric Performance"))
    vc.append(make_slicer(1010, 245, 250, 40, "Axe Organisation"))
    vc.append(make_slicer(1270, 245, 250, 40, "Période"))
    # KPI row
    kpi_labels = [
        ("Vol affaires prod.", 20, 287),
        ("Vol instance", 317, 287),
        ("Vol commissionnées", 614, 287),
        ("Montant moy. rétro", 911, 287),
        ("Taux atteinte budget", 1208, 287),
    ]
    vc.extend(build_kpi_row(kpi_labels, y=305, tab=40))
    # G04 charts (y=475)
    vc.append(make_chart(20, 475, 489, 350, "lineChart", "Évolution volume"))
    vc.append(make_chart(525, 475, 489, 350, "barChart", "Ranking agences"))
    vc.append(make_chart(1030, 475, 489, 350, "columnChart", "Répartition"))
    return vc

def build_page_affaires():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Affaires produites", "Analyse par statut, période et axe d'affaires", tab=20))
    # G02_Toolbar_Affaires
    vc.append(make_slicer(20, 245, 600, 40, "FP Axe Affaires"))
    vc.append(make_slicer(760, 245, 230, 40, "Mois Référence"))
    vc.append(make_slicer(1000, 245, 230, 40, "Mois Comparaison"))
    vc.append(make_slicer(1240, 245, 280, 40, "Périmètre"))
    # KPI row
    kpi_labels = [
        ("Nb affaires prod.", 20, 287),
        ("Vol affaires prod.", 317, 287),
        ("Vol instance", 614, 287),
        ("Vol commissionnées", 911, 287),
        ("Montant moy. rétro", 1208, 287),
    ]
    vc.extend(build_kpi_row(kpi_labels, y=305, tab=40))
    # G04 comparaison mois (y=475)
    for i, (lbl, cx) in enumerate([("Mois Ref.", 20), ("Mois Comp.", 530), ("Delta", 1030)]):
        vc.append(make_shape(cx, 475, 480, 200, "#FFFFFF", z=0))
        vc.append(make_textbox(cx+15, 490, 200, 25, lbl, bold=True, font_size="12pt", color="#0A4E97"))
        vc.append(make_textbox(cx+15, 525, 200, 40, "—", bold=True, font_size="22pt", color="#1E293B"))
    # G05 gauges budget (y=685)
    for i, (gl, gx) in enumerate([("Taux atteinte volume", 20), ("Taux atteinte nombre", 530), ("Taux atteinte rétro", 1030)]):
        vc.append(make_shape(gx, 685, 480, 130, "#FFFFFF", z=0))
        vc.append(make_textbox(gx+15, 700, 300, 25, gl, bold=True, font_size="11pt", color="#0A4E97"))
        vc.append(make_textbox(gx+15, 735, 200, 40, "—%", bold=True, font_size="18pt", color="#198754"))
    # G06 charts (y=825)
    vc.append(make_chart(20, 825, 735, 240, "lineChart", "Évolution volume affaires"))
    vc.append(make_chart(775, 825, 745, 240, "columnChart", "Répartition axe affaires"))
    return vc

def build_page_reseau():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Réseau MIA", "Activité et performance du réseau de mandataires", tab=20))
    # G02_Toolbar_Reseau
    vc.append(make_slicer(20, 245, 520, 40, "FP Axe Réseau"))
    vc.append(make_slicer(550, 245, 250, 40, "Période"))
    vc.append(make_slicer(810, 245, 250, 40, "Périmètre"))
    vc.append(make_button(1310, 245, 210, 40, "Afficher le tableau"))
    # KPI row
    kpi_labels = [
        ("Nb MIA oriasés", 20, 287),
        ("Nb MIA actifs", 317, 287),
        ("Nb MIA productifs", 614, 287),
        ("Nb MIA commissionnés", 911, 287),
        ("Montant moy. rétro", 1208, 287),
    ]
    vc.extend(build_kpi_row(kpi_labels, y=305, tab=40))
    # G04_Map (y=475)
    vc.append(make_shape(20, 475, 850, 540, "#E8EEF5", z=0))
    vc.append(make_textbox(30, 485, 200, 25, "Carte non disponible (placeholder)", bold=False, font_size="10pt", color="#667085"))
    # G04 right: focus agence (x=890, y=475)
    vc.append(make_shape(890, 475, 630, 240, "#FFFFFF", z=0))
    vc.append(make_textbox(905, 490, 200, 25, "Focus Agence", bold=True, font_size="12pt", color="#0A4E97"))
    for i, lbl in enumerate(["Sélectionner une agence..."]):
        vc.append(make_textbox(905, 525+i*30, 600, 25, lbl, bold=False, font_size="10pt", color="#667085"))
    # G05 Right donuts (y=740)
    vc.append(make_chart(890, 740, 310, 290, "donutChart", "Répartition statut"))
    vc.append(make_chart(1220, 740, 310, 290, "donutChart", "Répartition type"))
    # Tableau (y=1040 - dans zone défilable)
    vc.append(make_table(890, 1040, 630, 220, "Détail mandataires"))
    return vc

def build_page_reseau_tableau():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Réseau MIA - Tableau", "Vue détaillée des mandataires", tab=20))
    vc.append(make_slicer(20, 245, 520, 40, "FP Axe Réseau"))
    vc.append(make_slicer(550, 245, 250, 40, "Période"))
    kpi_labels = [
        ("Nb MIA oriasés", 20, 287),
        ("Nb MIA actifs", 317, 287),
        ("Nb MIA productifs", 614, 287),
        ("Nb MIA commissionnés", 911, 287),
        ("Montant moy. rétro", 1208, 287),
    ]
    vc.extend(build_kpi_row(kpi_labels, y=305, tab=40))
    # Tableau détaillé
    vc.append(make_table(20, 475, 1500, 580, "Tableau détaillé mandataires"))
    return vc

def build_page_rdv():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Rendez-vous", "Suivi des rendez-vous prévus, réalisés et taux de réalisation", tab=20))
    # G02_Toolbar_RDV
    vc.append(make_slicer(20, 245, 700, 40, "FP Axe RDV"))
    vc.append(make_slicer(730, 245, 250, 40, "Période"))
    vc.append(make_slicer(990, 245, 250, 40, "Axe Organisation"))
    vc.append(make_slicer(1250, 245, 270, 40, "Périmètre"))
    # KPI row
    kpi_labels = [
        ("Nb RDV réalisés", 20, 287),
        ("Nb RDV prévus", 317, 287),
        ("Nb RDV confirmés", 614, 287),
        ("Taux réalisation", 911, 287),
        ("Taux Visio/Domicile", 1208, 287),
    ]
    vc.extend(build_kpi_row(kpi_labels, y=305, tab=40))
    # G04 charts (y=475)
    vc.append(make_chart(20, 475, 489, 340, "barChart", "Répartition type RDV"))
    vc.append(make_chart(525, 475, 995, 340, "lineChart", "Prévus vs Réalisés"))
    # G05 tableau détail (y=825)
    vc.append(make_table(20, 825, 1500, 240, "Détail rendez-vous"))
    return vc

def build_page_alertes():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Alertes & Recommandations", "Tableau de bord des alertes opérationnelles", tab=20))
    # G02 cards alertes (y=245)
    alert_kpis = [
        ("Alertes Critiques", 20, "#D71920"),
        ("Alertes Hautes", 317, "#E67E22"),
        ("Alertes Moyennes", 614, "#F1C40F"),
        ("Alertes Ouvertes", 911, "#0A4E97"),
        ("Niveau Global", 1208, "#667085"),
    ]
    for (label, x, color) in alert_kpis:
        vc.append(make_shape(x, 245, 287, 150, "#FFFFFF", z=0))
        vc.append(make_shape(x+10, 255, 6, 130, color, z=1))
        vc.append(make_textbox(x+25, 260, 250, 25, label, bold=True, font_size="11pt", color="#1E293B"))
        vc.append(make_textbox(x+25, 295, 200, 50, "—", bold=True, font_size="28pt", color=color))
    # G03 niveaux alertes (y=415)
    niveau_rows = [
        ("Niveau Alerte Volume", 20, 415, "#E8EEF5"),
        ("Niveau Alerte RDV", 530, 415, "#E8EEF5"),
        ("Niveau Alerte Réseau", 1040, 415, "#E8EEF5"),
    ]
    for (label, x, y, bg) in niveau_rows:
        vc.append(make_shape(x, y, 480, 80, bg, z=0))
        vc.append(make_textbox(x+15, y+10, 200, 22, label, bold=True, font_size="11pt", color="#0A4E97"))
        vc.append(make_textbox(x+15, y+40, 350, 28, "NON DISPONIBLE", bold=True, font_size="14pt", color="#667085"))
    # Recommandations (y=515)
    vc.append(make_shape(20, 515, 1500, 130, "#FFFFFF", z=0))
    vc.append(make_textbox(35, 525, 200, 25, "Recommandations automatiques", bold=True, font_size="12pt", color="#0A4E97"))
    vc.append(make_textbox(35, 558, 1450, 80, "— Volume : Données affaires non disponibles. Intégrer fact_affaires.\n— RDV : Vérifier les objectifs de rendez-vous.\n— Réseau : Analyser les mandataires inactifs.", bold=False, font_size="10pt", color="#1E293B"))
    # Table alertes (y=660)
    vc.append(make_table(20, 660, 1500, 400, "Tableau des alertes"))
    return vc

def build_page_glossaire():
    vc = []
    vc.extend(build_header(tab=0))
    vc.extend(build_title_zone("Glossaire KPI", "Définitions et sources des indicateurs", tab=20))
    # Table glossaire
    vc.append(make_table(20, 245, 1500, 810, "Glossaire KPI"))
    return vc

# ─────────────────────────────────────────────
# Build full report
# ─────────────────────────────────────────────

pages_data = [
    ("ReportSection01", "Accueil", 0, build_page_accueil()),
    ("ReportSection02", "Performance", 1, build_page_performance()),
    ("ReportSection03", "Affaires", 2, build_page_affaires()),
    ("ReportSection04", "Réseau MIA", 3, build_page_reseau()),
    ("ReportSection04B", "Réseau MIA - Tableau", 4, build_page_reseau_tableau()),
    ("ReportSection05", "Rendez-vous", 5, build_page_rdv()),
    ("ReportSection06", "Alertes", 6, build_page_alertes()),
    ("ReportSection07", "Glossaire", 7, build_page_glossaire()),
]

sections = []
for (name, display, ordinal, visuals) in pages_data:
    sections.append({
        "name": name,
        "displayName": display,
        "ordinal": ordinal,
        "config": page_config(),
        "displayOption": 0,
        "width": 1540,
        "height": 1080,
        "visualContainers": visuals
    })

report = {
    "id": uid(),
    "resourcePackages": [
        {
            "resourcePackage": {
                "name": "SharedResources",
                "type": 2,
                "items": [],
                "disabled": False
            }
        }
    ],
    "sections": sections,
    "config": json.dumps({
        "version": "5.47",
        "themeCollection": {
            "baseTheme": {
                "name": "CY24SU08",
                "version": "5.47",
                "type": 2
            }
        },
        "activeSectionIndex": 0,
        "visualContainerSyncLoadingTimeout": 0,
        "objects": {
            "section": [{"properties": {"verticalAlignment": {"expr": {"Literal": {"Value": "'Top'"}}}}}]
        }
    }),
    "filters": "[]",
    "layoutOptimization": 0
}

with open(REPORT_DEST, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print("report.json généré avec succès!")
print(f"Pages: {len(sections)}")
total_visuals = sum(len(p['visualContainers']) for p in sections)
print(f"Total visualContainers: {total_visuals}")
for s in sections:
    print(f"  - {s['displayName']}: {len(s['visualContainers'])} visuals")
