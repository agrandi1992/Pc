# README_DEPLOIEMENT — Guide de déploiement
*Version: v5.0 | Date: 2025-06-05*

## Phase 1 — Déploiement local (actuel)
Le fichier `PC_LOCAL_v5.zip` contient le modèle Import avec données fictives.

### Prérequis
- Power BI Desktop 2024+ (gratuit)
- Windows (chemin court recommandé, ex: `C:\PBI\`)

### Instructions
1. Extraire `PC_LOCAL_v5.zip` vers `C:\PBI\`
2. Ouvrir `PCL\Pilotage_Commercial.pbip` dans Power BI Desktop
3. Le rapport s'ouvre directement (8 pages, données fictives)
4. Actualiser les données si nécessaire (Accueil > Actualiser)

### Structure des fichiers
```
PCL/
├── Pilotage_Commercial.pbip
├── Pilotage_Commercial.Report/
│   ├── definition.pbir
│   └── report.json        ← 8 pages, 420 visuels
└── Pilotage_Commercial.SemanticModel/
    ├── definition.pbism
    └── model_local.bim    ← 27 tables, 77 mesures, Import mode
```

## Phase 2 — Déploiement Fabric (production)
Pour connecter au Gold layer sur Microsoft Fabric :

1. Ouvrir `model.bim` (DirectLake) dans Power BI Desktop avec connexion Fabric
2. Remplacer `model_local.bim` par `model.bim` dans le répertoire SemanticModel
3. Configurer la connexion Lakehouse (workspace + lakehouse ID)
4. Toutes les tables référencent `schemaName: "gold"` — aucune modification de rapport nécessaire

### Correspondance tables Gold
| Table BIM | Table Fabric Gold | Mode |
|-----------|------------------|------|
| dim_date | gold.dim_date | DirectLake |
| dim_agence | gold.dim_agence | DirectLake |
| dim_mandataire | gold.dim_mandataire | DirectLake |
| fact_affaire | gold.fact_affaire | DirectLake |
| fact_rendez_vous_client | gold.fact_rendez_vous_client | DirectLake |
| fact_alertes | gold.fact_alertes | DirectLake |
| ... (16 tables total) | gold.* | DirectLake |

## Architecture DAX
Toutes les mesures sont dans la table `_Indicateurs`.
Les mesures utilisent la convention: `Nom complet en français`.

### Mesures clés
- **Volume affaires produites** — `CALCULATE(SUM(fact_affaire[chiffre_affaires]), fact_affaire[flag_pu]=1)`
- **Taux atteinte Budget N Volume** — Ratio Volume vs Budget
- **Variation vs N-1** — Comparaison glissante N/N-1

## Support
Pour toute question: contacter l'équipe Data Capfinances.
