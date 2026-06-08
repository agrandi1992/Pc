# Pack projet indépendant — Pilotage Commercial PBIP

Ce pack sert à ouvrir un nouveau projet indépendant et demander à un agent Power BI / développeur BI de produire un rapport Power BI en format projet `.pbip`, à partir du modèle sémantique original, de l’Excel KPI, de la maquette HTML et des spécifications détaillées.

## Objectif final
Produire un rapport Power BI **Pilotage Commercial** premium, pixel-perfect, orienté métier, avec :

- pages : Accueil, Performance, Affaires, Réseau MIA, Rendez-vous, Alertes, Glossaire ;
- navigation complète ;
- slicers et field parameters ;
- cards fusionnées détaillées ;
- graphes, jauges, tableaux, carte de France ;
- sources KPI Excel affichées / documentées ;
- statut BIM existant / à créer pour chaque élément ;
- contrôle anti-chevauchement ;
- DAX et tables nécessaires ;
- bookmarks, groupes Selection Pane et contrôle de rendu.

## Fichiers essentiels

### 01_Sources_brutes
- `Modele_Original_Pilotage_Commercial.bim` : modèle sémantique original à analyser et enrichir.
- `Pilotage_commercial_KPI.xlsx` : référentiel KPI métier Excel.
- `maquette_HTML_pilotage_commercial.html` : maquette HTML d’origine Pilotage Commercial.

### 02_References_visuelles
- Images PNG page par page enrichies Excel + BIM.
- `maquette_HTML_enrichie_Excel_BIM.html` : version HTML annotée.

### 03_Specifications_PowerBI
- `spec_powerbi_v4_avec_controle_chevauchement.xlsx` : fichier principal à suivre.
- `spec_powerbi_v3_navigation_slicers_fieldparams_visuels.xlsx` : navigation, slicers, field parameters, types de visuels.
- `spec_card_fusionnee_powerbi_option_A_C_v2.xlsx` : template détaillé des cards fusionnées.
- `matrice_kpi_excel_bim_pilotage_commercial.xlsx` : mapping KPI Excel vs modèle BIM.
- fichiers Markdown de prompts complémentaires.

### 04_DAX_et_modele_semantique
- DAX des mesures, alertes, couleurs conditionnelles, field parameters et tables de support.

### 05_Validation_qualite
- `check_powerbi_overlap.py` : script de contrôle des chevauchements dans un projet Power BI.

## Point important
Aucun fichier `.pbip` de base n’a été fourni dans les fichiers sources disponibles. Le pack inclut donc :

- le `.bim` original ;
- les sources KPI ;
- les prompts et specs pour produire le `.pbip` ;
- un emplacement de sortie attendu dans `06_Livrables_attendus`.

Le développeur / agent doit créer le projet `.pbip` cible à partir du modèle BIM original et de ces spécifications.
