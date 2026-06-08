#!/usr/bin/env python3
"""Script to generate the enriched BIM for Pilotage Commercial PBIP project."""

import json
import uuid
import copy

BIM_SOURCE = "/home/user/Pc/powerbi_project/pack_projet_independant_pilotage_commercial_pbip/01_Sources_brutes/Modele_Original_Pilotage_Commercial.bim"
BIM_DEST = "/home/user/Pc/powerbi_project/pack_projet_independant_pilotage_commercial_pbip/06_Livrables_attendus/Pilotage_Commercial.SemanticModel/model.bim"

def uid():
    return str(uuid.uuid4())

with open(BIM_SOURCE, 'r', encoding='utf-8') as f:
    bim = json.load(f)

# ─────────────────────────────────────────────
# 1. NEW CALCULATED TABLES
# ─────────────────────────────────────────────

new_tables = []

# fact_affaires placeholder
new_tables.append({
    "name": "fact_affaires",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "DATATABLE(",
            "    \"affaire_id\", STRING,",
            "    \"date_affaire\", DATETIME,",
            "    \"mandataire_id\", STRING,",
            "    \"agence_id\", STRING,",
            "    \"produit_id\", STRING,",
            "    \"assureur_id\", STRING,",
            "    \"statut_affaire\", STRING,",
            "    \"montant_affaire\", CURRENCY,",
            "    \"montant_retrocommission\", CURRENCY,",
            "    \"nombre_ventes_partage\", INTEGER,",
            "    \"flag_produite\", BOOLEAN,",
            "    \"flag_instance\", BOOLEAN,",
            "    \"flag_commissionnee\", BOOLEAN,",
            "    {}",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "affaire_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[affaire_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "date_affaire", "dataType": "dateTime", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[date_affaire]", "formatString": "General Date", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "mandataire_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[mandataire_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "agence_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[agence_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "produit_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[produit_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "assureur_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[assureur_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "statut_affaire", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[statut_affaire]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "montant_affaire", "dataType": "decimal", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[montant_affaire]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "montant_retrocommission", "dataType": "decimal", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[montant_retrocommission]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "nombre_ventes_partage", "dataType": "int64", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[nombre_ventes_partage]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "flag_produite", "dataType": "boolean", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[flag_produite]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "flag_instance", "dataType": "boolean", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[flag_instance]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "flag_commissionnee", "dataType": "boolean", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[flag_commissionnee]", "lineageTag": uid(), "summarizeBy": "none"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# budget_affaires placeholder
new_tables.append({
    "name": "budget_affaires",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "DATATABLE(",
            "    \"budget_id\", STRING,",
            "    \"date_budget\", DATETIME,",
            "    \"agence_id\", STRING,",
            "    \"produit_id\", STRING,",
            "    \"assureur_id\", STRING,",
            "    \"budget_affaires_nombre\", INTEGER,",
            "    \"budget_affaires_euro\", CURRENCY,",
            "    \"budget_retrocommission\", CURRENCY,",
            "    {}",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "budget_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[budget_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "date_budget", "dataType": "dateTime", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[date_budget]", "formatString": "General Date", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "agence_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[agence_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "produit_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[produit_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "assureur_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[assureur_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "budget_affaires_nombre", "dataType": "int64", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[budget_affaires_nombre]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "budget_affaires_euro", "dataType": "decimal", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[budget_affaires_euro]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "budget_retrocommission", "dataType": "decimal", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[budget_retrocommission]", "lineageTag": uid(), "summarizeBy": "sum"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# fact_alertes placeholder
new_tables.append({
    "name": "fact_alertes",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "DATATABLE(",
            "    \"alerte_id\", STRING,",
            "    \"date_analyse\", DATETIME,",
            "    \"date_detection\", DATETIME,",
            "    \"niveau_priorite\", STRING,",
            "    \"categorie_alerte\", STRING,",
            "    \"kpi_concerne\", STRING,",
            "    \"valeur_actuelle\", DOUBLE,",
            "    \"seuil_alerte\", DOUBLE,",
            "    \"ecart\", DOUBLE,",
            "    \"agence_id\", STRING,",
            "    \"mandataire_id\", STRING,",
            "    \"impact_metier\", STRING,",
            "    \"recommandation\", STRING,",
            "    \"statut_alerte\", STRING,",
            "    {}",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "alerte_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[alerte_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "date_analyse", "dataType": "dateTime", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[date_analyse]", "formatString": "General Date", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "date_detection", "dataType": "dateTime", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[date_detection]", "formatString": "General Date", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "niveau_priorite", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[niveau_priorite]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "categorie_alerte", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[categorie_alerte]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "kpi_concerne", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[kpi_concerne]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "valeur_actuelle", "dataType": "double", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[valeur_actuelle]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "seuil_alerte", "dataType": "double", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[seuil_alerte]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "ecart", "dataType": "double", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[ecart]", "lineageTag": uid(), "summarizeBy": "sum"},
        {"type": "calculatedTableColumn", "name": "agence_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[agence_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "mandataire_id", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[mandataire_id]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "impact_metier", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[impact_metier]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "recommandation", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[recommandation]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "statut_alerte", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[statut_alerte]", "lineageTag": uid(), "summarizeBy": "none"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# Periode_Affichage
new_tables.append({
    "name": "Periode_Affichage",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "DATATABLE(",
            "    \"Periode\", STRING,",
            "    \"Ordre\", INTEGER,",
            "    {",
            "        {\"Jour\", 1},",
            "        {\"Semaine\", 2},",
            "        {\"Mois\", 3},",
            "        {\"Trimestre\", 4},",
            "        {\"Ann\\u00e9e\", 5}",
            "    }",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "Periode", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Periode]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Ordre", "dataType": "int64", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Ordre]", "lineageTag": uid(), "summarizeBy": "sum"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# KPI_Status
kpi_rows = [
    ("G.1","Nombre de ventes","Performance","G.1","BIM absent","fact_affaires à créer","Nécessite fact_affaires"),
    ("G.2","Nombre d'affaires produites","Affaires","G.2","BIM absent","fact_affaires à créer","Nécessite fact_affaires"),
    ("G.3","Volume d'affaires produites","Accueil,Performance,Affaires","G.3","BIM absent","fact_affaires à créer","Nécessite fact_affaires"),
    ("G.4","Budget affaires en nombre","Affaires","G.4","BIM absent","budget_affaires à intégrer","Nécessite budget_affaires"),
    ("G.5","Budget affaires en euro","Affaires","G.5","BIM absent","budget_affaires à intégrer","Nécessite budget_affaires"),
    ("G.6","Nombre mandataires actifs","Réseau,Accueil","G.6","BIM OK","_Indicateurs[Nombre mandataires actifs]","Disponible"),
    ("G.7","Nombre mandataires inactifs","Réseau","G.7","BIM OK","_Indicateurs[Nombre mandataires inactifs]","Disponible"),
    ("G.8","Nombre mandataires productifs","Réseau","G.8","BIM absent","Mesure à créer","Nécessite fact_affaires"),
    ("G.9","Nombre mandataires non productifs","Réseau","G.9","BIM absent","Mesure à créer","Dérivable de G.6-G.8"),
    ("G.10","Nombre mandataires rétrocommissionnés","Réseau","G.10","BIM OK","_Indicateurs[Nombre mandataires rétrocommissionnés]","Disponible"),
    ("G.11","Nombre mandataires non rétrocommissionnés","Réseau","G.11","BIM absent","Mesure à créer","Dérivable de G.6-G.10"),
    ("G.12","RDV hebdomadaire moyen","RDV","G.12","BIM à créer","Calculable depuis RDV+Date","Dérivable"),
    ("G.13","Taux réalisation RDV","Accueil,RDV,Alertes","G.13","BIM OK","_Indicateurs[Taux réalisation de rendez-vous]","Disponible"),
    ("G.14","Nombre RDV prévus","RDV","G.14","BIM OK","_Indicateurs[Nombre rendez-vous prévus]","Disponible"),
    ("G.15","Nombre RDV réalisés","RDV","G.15","BIM OK","_Indicateurs[Nombre rendez-vous réalisés]","Disponible"),
    ("G.18","Taux RDV visioconférence","RDV","G.18","BIM OK","_Indicateurs[Taux rendez vous réalisés en visioconférence]","Disponible"),
    ("G.19","Taux RDV domicile","RDV","G.19","BIM OK","_Indicateurs[Taux rendez-vous faits à domicile]","Disponible"),
    ("G.20","Nombre RDV visio","RDV","G.20","BIM OK","_Indicateurs[Nombre rendez-vous réalisés en visioconférence]","Disponible"),
    ("G.21","Nombre RDV domicile","RDV","G.21","BIM OK","_Indicateurs[Nombre rendez-vous réalisés à domicile]","Disponible"),
    ("ALERTE_CRIT","Nombre Alertes Critiques","Alertes","À créer","BIM absent","fact_alertes à créer","Nécessite fact_alertes")
]

kpi_row_dax = []
for r in kpi_rows:
    kpi_row_dax.append('        {"' + r[0] + '","' + r[1] + '","' + r[2] + '","' + r[3] + '","' + r[4] + '","' + r[5] + '","' + r[6] + '"}')

new_tables.append({
    "name": "KPI_Status",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": ["DATATABLE(",
            "    \"KPI_ID\", STRING,",
            "    \"KPI_Label\", STRING,",
            "    \"Page\", STRING,",
            "    \"Source_Excel\", STRING,",
            "    \"Statut_BIM\", STRING,",
            "    \"Mesure_BIM\", STRING,",
            "    \"Note\", STRING,",
            "    {"] + kpi_row_dax + ["    }",")"]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "KPI_ID", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[KPI_ID]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "KPI_Label", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[KPI_Label]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Page", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Page]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Source_Excel", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Source_Excel]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Statut_BIM", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Statut_BIM]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Mesure_BIM", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Mesure_BIM]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Note", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Note]", "lineageTag": uid(), "summarizeBy": "none"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# Field Parameters
# FP_Axe_Organisation
new_tables.append({
    "name": "FP_Axe_Organisation",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "SELECTCOLUMNS(",
            "    {",
            "        (1, \"Agence\", NAMEOF(dim_agence[raison_sociale])),",
            "        (2, \"Ville Agence\", NAMEOF(dim_agence[ville_agence])),",
            "        (3, \"Mandataire\", NAMEOF(dim_mandataire[mandataire_id]))",
            "    },",
            "    \"Ordre\", [Value1],",
            "    \"FP_Axe_Organisation\", [Value2],",
            "    \"FP_Axe_Organisation Fields\", [Value3]",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "Ordre", "dataType": "int64", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Ordre]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "FP_Axe_Organisation", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[FP_Axe_Organisation]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "FP_Axe_Organisation Fields", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[FP_Axe_Organisation Fields]", "lineageTag": uid(), "summarizeBy": "none", "dataCategory": "FieldList"}
    ],
    "annotations": [
        {"name": "PBI_ResultType", "value": "Table"},
        {"name": "PBI_NavigationStepName", "value": "Navigation"}
    ]
})

# FP_Axe_Reseau
new_tables.append({
    "name": "FP_Axe_Reseau",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "SELECTCOLUMNS(",
            "    {",
            "        (1, \"Agence\", NAMEOF(dim_agence[raison_sociale])),",
            "        (2, \"Ville Agence\", NAMEOF(dim_agence[ville_agence])),",
            "        (3, \"Mandataire\", NAMEOF(dim_mandataire[mandataire_id]))",
            "    },",
            "    \"Ordre\", [Value1],",
            "    \"FP_Axe_Reseau\", [Value2],",
            "    \"FP_Axe_Reseau Fields\", [Value3]",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "Ordre", "dataType": "int64", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Ordre]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "FP_Axe_Reseau", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[FP_Axe_Reseau]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "FP_Axe_Reseau Fields", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[FP_Axe_Reseau Fields]", "lineageTag": uid(), "summarizeBy": "none", "dataCategory": "FieldList"}
    ],
    "annotations": [
        {"name": "PBI_ResultType", "value": "Table"},
        {"name": "PBI_NavigationStepName", "value": "Navigation"}
    ]
})

# FP_Axe_RDV
new_tables.append({
    "name": "FP_Axe_RDV",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "SELECTCOLUMNS(",
            "    {",
            "        (1, \"Type de rendez-vous\", NAMEOF(dim_type_rendez_vous_client[libelle_type_rendez_vous])),",
            "        (2, \"Canal\", NAMEOF(fact_rendez_vous_client[type_rendez_vous_id]))",
            "    },",
            "    \"Ordre\", [Value1],",
            "    \"FP_Axe_RDV\", [Value2],",
            "    \"FP_Axe_RDV Fields\", [Value3]",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "Ordre", "dataType": "int64", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Ordre]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "FP_Axe_RDV", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[FP_Axe_RDV]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "FP_Axe_RDV Fields", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[FP_Axe_RDV Fields]", "lineageTag": uid(), "summarizeBy": "none", "dataCategory": "FieldList"}
    ],
    "annotations": [
        {"name": "PBI_ResultType", "value": "Table"},
        {"name": "PBI_NavigationStepName", "value": "Navigation"}
    ]
})

# Mois_Reference
new_tables.append({
    "name": "Mois_Reference",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "SELECTCOLUMNS(",
            "    dim_date,",
            "    \"Date\", dim_date[Date],",
            "    \"Ann\\u00e9e Mois\", dim_date[annee_mois],",
            "    \"Mois\", dim_date[nom_du_mois]",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "Date", "dataType": "dateTime", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Date]", "formatString": "General Date", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Année Mois", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Année Mois]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Mois", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Mois]", "lineageTag": uid(), "summarizeBy": "none"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# Mois_Compare
new_tables.append({
    "name": "Mois_Compare",
    "lineageTag": uid(),
    "mode": "calculated",
    "calculatedTableExpression": {
        "kind": "calculated",
        "expression": [
            "SELECTCOLUMNS(",
            "    dim_date,",
            "    \"Date\", dim_date[Date],",
            "    \"Ann\\u00e9e Mois\", dim_date[annee_mois],",
            "    \"Mois\", dim_date[nom_du_mois]",
            ")"
        ]
    },
    "columns": [
        {"type": "calculatedTableColumn", "name": "Date", "dataType": "dateTime", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Date]", "formatString": "General Date", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Année Mois", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Année Mois]", "lineageTag": uid(), "summarizeBy": "none"},
        {"type": "calculatedTableColumn", "name": "Mois", "dataType": "string", "isNameInferred": True, "isDataTypeInferred": True, "sourceColumn": "[Mois]", "lineageTag": uid(), "summarizeBy": "none"}
    ],
    "annotations": [{"name": "PBI_ResultType", "value": "Table"}]
})

# ─────────────────────────────────────────────
# 2. NEW MEASURES for _Indicateurs
# ─────────────────────────────────────────────

new_measures = [
    {
        "name": "Nombre ventes",
        "expression": "COALESCE(SUM(fact_affaires[nombre_ventes_partage]), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre affaires produites",
        "expression": "COALESCE(CALCULATE(DISTINCTCOUNT(fact_affaires[affaire_id]), fact_affaires[flag_produite] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Volume affaires produites",
        "expression": "COALESCE(CALCULATE(SUM(fact_affaires[montant_affaire]), fact_affaires[flag_produite] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0.00 €",
        "lineageTag": uid()
    },
    {
        "name": "Nombre affaires en instance",
        "expression": "COALESCE(CALCULATE(DISTINCTCOUNT(fact_affaires[affaire_id]), fact_affaires[flag_instance] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Volume affaires en instance",
        "expression": "COALESCE(CALCULATE(SUM(fact_affaires[montant_affaire]), fact_affaires[flag_instance] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0.00 €",
        "lineageTag": uid()
    },
    {
        "name": "Nombre affaires commissionnées",
        "expression": "COALESCE(CALCULATE(DISTINCTCOUNT(fact_affaires[affaire_id]), fact_affaires[flag_commissionnee] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Volume affaires commissionnées",
        "expression": "COALESCE(CALCULATE(SUM(fact_affaires[montant_affaire]), fact_affaires[flag_commissionnee] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0.00 €",
        "lineageTag": uid()
    },
    {
        "name": "Budget affaires en nombre",
        "expression": "COALESCE(SUM(budget_affaires[budget_affaires_nombre]), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Budget affaires en euro",
        "expression": "COALESCE(SUM(budget_affaires[budget_affaires_euro]), 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0.00 €",
        "lineageTag": uid()
    },
    {
        "name": "Taux atteinte Budget N Volume",
        "expression": "DIVIDE([Volume affaires produites], [Budget affaires en euro], 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "0.0%",
        "lineageTag": uid()
    },
    {
        "name": "Volume affaires produites N-1",
        "expression": "CALCULATE([Volume affaires produites], SAMEPERIODLASTYEAR(dim_date[Date]))",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0.00 €",
        "lineageTag": uid()
    },
    {
        "name": "Variation vs N-1 Volume Affaires (%)",
        "expression": "DIVIDE([Volume affaires produites] - [Volume affaires produites N-1], [Volume affaires produites N-1], 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "0.0%",
        "lineageTag": uid()
    },
    {
        "name": "Volume affaires produites MTD-1",
        "expression": "CALCULATE([Volume affaires produites], DATEADD(dim_date[Date], -1, MONTH))",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "#,0.00 €",
        "lineageTag": uid()
    },
    {
        "name": "Variation vs MTD-1 Volume Affaires (%)",
        "expression": "DIVIDE([Volume affaires produites] - [Volume affaires produites MTD-1], [Volume affaires produites MTD-1], 0)",
        "displayFolder": "Pilotage Commercial - Affaires",
        "formatString": "0.0%",
        "lineageTag": uid()
    },
    {
        "name": "Nombre MIA oriasés",
        "expression": "COALESCE(CALCULATE(DISTINCTCOUNT(dim_mandataire[mandataire_id]), NOT ISBLANK(dim_mandataire[numero_orias])), 0)",
        "displayFolder": "Pilotage Commercial - Réseau",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre mandataires productifs",
        "expression": "COALESCE(CALCULATE(DISTINCTCOUNT(fact_affaires[mandataire_id]), fact_affaires[flag_produite] = TRUE()), 0)",
        "displayFolder": "Pilotage Commercial - Réseau",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre mandataires non productifs",
        "expression": "MAX([Nombre mandataires actifs] - [Nombre mandataires productifs], 0)",
        "displayFolder": "Pilotage Commercial - Réseau",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre mandataires non rétrocommissionnés",
        "expression": "MAX([Nombre mandataires actifs] - [Nombre mandataires rétrocommissionnés], 0)",
        "displayFolder": "Pilotage Commercial - Réseau",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Taux mandataires actifs",
        "expression": "DIVIDE([Nombre mandataires actifs], [Nombre mandataires actifs] + [Nombre mandataires inactifs], 0)",
        "displayFolder": "Pilotage Commercial - Réseau",
        "formatString": "0.0%",
        "lineageTag": uid()
    },
    {
        "name": "Nombre RDV hebdomadaire moyen",
        "expression": "DIVIDE([Nombre rendez-vous réalisés], DISTINCTCOUNT(dim_date[numero_de_la_semaine]), 0)",
        "displayFolder": "Pilotage Commercial - RDV",
        "formatString": "#,0.0",
        "lineageTag": uid()
    },
    {
        "name": "Niveau Alerte Volume",
        "expression": "VAR VarPct = [Variation vs N-1 Volume Affaires (%)]\nRETURN SWITCH(TRUE(),\n    ISBLANK(VarPct), \"NON DISPONIBLE\",\n    VarPct < -0.20, \"CRITIQUE\",\n    VarPct < -0.10, \"HAUTE\",\n    VarPct < 0, \"MOYENNE\",\n    \"CONFORME\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Couleur Alerte Volume",
        "expression": "SWITCH([Niveau Alerte Volume],\n    \"CRITIQUE\", \"#D71920\",\n    \"HAUTE\", \"#E67E22\",\n    \"MOYENNE\", \"#F1C40F\",\n    \"CONFORME\", \"#198754\",\n    \"#667085\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Niveau Alerte RDV",
        "expression": "VAR Taux = [Taux réalisation de rendez-vous]\nRETURN SWITCH(TRUE(),\n    ISBLANK(Taux), \"NON DISPONIBLE\",\n    Taux < 0.50, \"CRITIQUE\",\n    Taux < 0.70, \"HAUTE\",\n    Taux < 0.85, \"MOYENNE\",\n    \"CONFORME\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Couleur Alerte RDV",
        "expression": "SWITCH([Niveau Alerte RDV],\n    \"CRITIQUE\", \"#D71920\",\n    \"HAUTE\", \"#E67E22\",\n    \"MOYENNE\", \"#F1C40F\",\n    \"CONFORME\", \"#198754\",\n    \"#667085\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Niveau Alerte Réseau",
        "expression": "VAR Taux = [Taux mandataires actifs]\nRETURN SWITCH(TRUE(),\n    ISBLANK(Taux), \"NON DISPONIBLE\",\n    Taux < 0.60, \"CRITIQUE\",\n    Taux < 0.80, \"HAUTE\",\n    Taux < 0.90, \"MOYENNE\",\n    \"CONFORME\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Couleur Alerte Réseau",
        "expression": "SWITCH([Niveau Alerte Réseau],\n    \"CRITIQUE\", \"#D71920\",\n    \"HAUTE\", \"#E67E22\",\n    \"MOYENNE\", \"#F1C40F\",\n    \"CONFORME\", \"#198754\",\n    \"#667085\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Recommandation Volume",
        "expression": "VAR VarPct = [Variation vs N-1 Volume Affaires (%)]\nRETURN SWITCH(TRUE(),\n    ISBLANK(VarPct), \"Donnée volume affaires indisponible : intégrer fact_affaires.\",\n    VarPct < -0.10, \"Identifier les agences contributrices au recul et déclencher un plan de relance.\",\n    VarPct < 0, \"Surveiller la trajectoire et challenger les zones en retrait.\",\n    \"Sécuriser l'atterrissage.\")",
        "displayFolder": "Pilotage Commercial - Alertes",
        "lineageTag": uid()
    },
    {
        "name": "Nombre Alertes Critiques",
        "expression": "COALESCE(CALCULATE(COUNTROWS(fact_alertes), fact_alertes[niveau_priorite] = \"CRITIQUE\", fact_alertes[statut_alerte] <> \"Cloturee\"), 0)",
        "displayFolder": "Pilotage Commercial - Alertes",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre Alertes Hautes",
        "expression": "COALESCE(CALCULATE(COUNTROWS(fact_alertes), fact_alertes[niveau_priorite] = \"HAUTE\", fact_alertes[statut_alerte] <> \"Cloturee\"), 0)",
        "displayFolder": "Pilotage Commercial - Alertes",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre Alertes Moyennes",
        "expression": "COALESCE(CALCULATE(COUNTROWS(fact_alertes), fact_alertes[niveau_priorite] = \"MOYENNE\", fact_alertes[statut_alerte] <> \"Cloturee\"), 0)",
        "displayFolder": "Pilotage Commercial - Alertes",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "Nombre Alertes Ouvertes",
        "expression": "COALESCE(CALCULATE(COUNTROWS(fact_alertes), fact_alertes[statut_alerte] <> \"Cloturee\"), 0)",
        "displayFolder": "Pilotage Commercial - Alertes",
        "formatString": "#,0",
        "lineageTag": uid()
    },
    {
        "name": "CF Variation Texte Volume",
        "expression": "SWITCH(TRUE(),\n    ISBLANK([Variation vs N-1 Volume Affaires (%)]), \"#0A4E97\",\n    [Variation vs N-1 Volume Affaires (%)] >= 0, \"#198754\",\n    [Variation vs N-1 Volume Affaires (%)] > -0.10, \"#E67E22\",\n    \"#D71920\")",
        "displayFolder": "Pilotage Commercial - Mise en forme conditionnelle",
        "lineageTag": uid()
    },
    {
        "name": "CF Budget Fill Volume",
        "expression": "SWITCH(TRUE(),\n    ISBLANK([Taux atteinte Budget N Volume]), \"#E8EEF5\",\n    [Taux atteinte Budget N Volume] >= 1, \"#198754\",\n    [Taux atteinte Budget N Volume] >= 0.8, \"#E67E22\",\n    \"#D71920\")",
        "displayFolder": "Pilotage Commercial - Mise en forme conditionnelle",
        "lineageTag": uid()
    },
    {
        "name": "Libellé Variation Volume vs N-1",
        "expression": "VAR v = [Variation vs N-1 Volume Affaires (%)]\nRETURN SWITCH(TRUE(),\n    ISBLANK(v), \"Vs N-1 —\",\n    v >= 0, \"▲ Vs N-1 \" & FORMAT(v, \"+0.0%;-0.0%\"),\n    \"▼ Vs N-1 \" & FORMAT(v, \"+0.0%;-0.0%\"))",
        "displayFolder": "Pilotage Commercial - Affichage",
        "lineageTag": uid()
    },
    {
        "name": "Libellé Variation Volume vs MTD-1",
        "expression": "VAR v = [Variation vs MTD-1 Volume Affaires (%)]\nRETURN SWITCH(TRUE(),\n    ISBLANK(v), \"Vs MTD-1 —\",\n    v >= 0, \"▲ Vs MTD-1 \" & FORMAT(v, \"+0.0%;-0.0%\"),\n    \"▼ Vs MTD-1 \" & FORMAT(v, \"+0.0%;-0.0%\"))",
        "displayFolder": "Pilotage Commercial - Affichage",
        "lineageTag": uid()
    }
]

# ─────────────────────────────────────────────
# 3. Apply changes to BIM
# ─────────────────────────────────────────────

# Add new tables
bim['model']['tables'].extend(new_tables)

# Add new measures to _Indicateurs
for t in bim['model']['tables']:
    if t['name'] == '_Indicateurs':
        if 'measures' not in t:
            t['measures'] = []
        for m in new_measures:
            measure_obj = {
                "name": m['name'],
                "expression": m['expression'],
                "displayFolder": m['displayFolder'],
                "lineageTag": m['lineageTag']
            }
            if 'formatString' in m:
                measure_obj['formatString'] = m['formatString']
            t['measures'].append(measure_obj)
        break

# Update model name
bim['name'] = 'Pilotage_Commercial'

# ─────────────────────────────────────────────
# 4. Save enriched BIM
# ─────────────────────────────────────────────
with open(BIM_DEST, 'w', encoding='utf-8') as f:
    json.dump(bim, f, indent=2, ensure_ascii=False)

print("BIM enrichi généré avec succès !")
print(f"Tables: {len(bim['model']['tables'])}")

# Count measures
for t in bim['model']['tables']:
    if t['name'] == '_Indicateurs':
        print(f"Mesures dans _Indicateurs: {len(t.get('measures', []))}")
