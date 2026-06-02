# CHANGELOG BUILD — Pilotage Commercial PBIP
**Date de génération :** 2026-06-02  
**Version :** 1.0.0  
**Auteur :** Génération automatisée Claude Code

---

## [1.0.0] — 2026-06-02 — Build initial complet

### Fichiers wrapper PBIP créés

| Fichier | Statut | Description |
|---------|--------|-------------|
| `Pilotage_Commercial.pbip` | CRÉÉ | Point d'entrée du projet PBIP, version 1.0 |
| `Pilotage_Commercial.Report/definition.pbireport` | CRÉÉ | Référence vers le SemanticModel par chemin relatif |
| `Pilotage_Commercial.SemanticModel/definition.pbism` | CRÉÉ | Mode import, version 1.0 |

---

### BIM — Semantic Model (`model.bim`)

**Source :** `01_Sources_brutes/Modele_Original_Pilotage_Commercial.bim`  
**Tables originales :** 18  
**Tables après enrichissement :** 28  
**Mesures originales dans `_Indicateurs` :** 39  
**Mesures après enrichissement :** 74 (+35)

#### Nouvelles tables calculées (calculated tables)

| Table | Type | Statut | Description |
|-------|------|--------|-------------|
| `fact_affaires` | Placeholder DATATABLE | CRÉÉ | 13 colonnes — affaire_id, date, mandataire, agence, produit, assureur, statuts, montants, flags. Nécessite connexion réelle. |
| `budget_affaires` | Placeholder DATATABLE | CRÉÉ | 8 colonnes — budget_id, date, agence, produit, assureur, budget nombre/euro/rétro |
| `fact_alertes` | Placeholder DATATABLE | CRÉÉ | 14 colonnes — alerte_id, dates, niveaux, KPI, valeurs, seuils, statut |
| `Periode_Affichage` | DATATABLE avec données | CRÉÉ | 5 lignes : Jour / Semaine / Mois / Trimestre / Année |
| `KPI_Status` | DATATABLE avec 20 lignes | CRÉÉ | Référentiel KPI G.1–G.26 + ALERTE_CRIT avec statut BIM |
| `FP_Axe_Organisation` | Field Parameter SELECTCOLUMNS | CRÉÉ | Agence / Ville Agence / Mandataire |
| `FP_Axe_Reseau` | Field Parameter SELECTCOLUMNS | CRÉÉ | Agence / Ville Agence / Mandataire |
| `FP_Axe_RDV` | Field Parameter SELECTCOLUMNS | CRÉÉ | Type de rendez-vous / Canal |
| `Mois_Reference` | SELECTCOLUMNS depuis dim_date | CRÉÉ | Date / Année Mois / Mois |
| `Mois_Compare` | SELECTCOLUMNS depuis dim_date | CRÉÉ | Date / Année Mois / Mois |

#### Nouvelles mesures ajoutées dans `_Indicateurs`

**Folder : Pilotage Commercial - Affaires**

| Mesure | Statut | DAX source |
|--------|--------|------------|
| `Nombre ventes` | CRÉÉ | SUM(fact_affaires[nombre_ventes_partage]) |
| `Nombre affaires produites` | CRÉÉ | DISTINCTCOUNT sur flag_produite |
| `Volume affaires produites` | CRÉÉ | SUM montant sur flag_produite |
| `Nombre affaires en instance` | CRÉÉ | DISTINCTCOUNT sur flag_instance |
| `Volume affaires en instance` | CRÉÉ | SUM montant sur flag_instance |
| `Nombre affaires commissionnées` | CRÉÉ | DISTINCTCOUNT sur flag_commissionnee |
| `Volume affaires commissionnées` | CRÉÉ | SUM montant sur flag_commissionnee |
| `Budget affaires en nombre` | CRÉÉ | SUM budget_affaires nombre |
| `Budget affaires en euro` | CRÉÉ | SUM budget_affaires euro |
| `Taux atteinte Budget N Volume` | CRÉÉ | DIVIDE volume prod / budget euro |
| `Volume affaires produites N-1` | CRÉÉ | SAMEPERIODLASTYEAR |
| `Variation vs N-1 Volume Affaires (%)` | CRÉÉ | DIVIDE delta N vs N-1 |
| `Volume affaires produites MTD-1` | CRÉÉ | DATEADD -1 MONTH |
| `Variation vs MTD-1 Volume Affaires (%)` | CRÉÉ | DIVIDE delta MTD |

**Folder : Pilotage Commercial - Réseau**

| Mesure | Statut | DAX source |
|--------|--------|------------|
| `Nombre MIA oriasés` | CRÉÉ | DISTINCTCOUNT sur numero_orias non vide |
| `Nombre mandataires productifs` | CRÉÉ | DISTINCTCOUNT fact_affaires mandataire sur flag_produite |
| `Nombre mandataires non productifs` | CRÉÉ | MAX(actifs - productifs, 0) |
| `Nombre mandataires non rétrocommissionnés` | CRÉÉ | MAX(actifs - rétrocommissionnés, 0) |
| `Taux mandataires actifs` | CRÉÉ | DIVIDE actifs / (actifs + inactifs) |

**Folder : Pilotage Commercial - RDV**

| Mesure | Statut | Note |
|--------|--------|------|
| `Nombre RDV hebdomadaire moyen` | CRÉÉ | DIVIDE réalisés / DISTINCTCOUNT semaines |

**Folder : Pilotage Commercial - Alertes**

| Mesure | Statut | Note |
|--------|--------|------|
| `Niveau Alerte Volume` | CRÉÉ | SWITCH sur seuils -20%/-10%/0% |
| `Couleur Alerte Volume` | CRÉÉ | Hex rouge/orange/jaune/vert |
| `Niveau Alerte RDV` | CRÉÉ | SWITCH sur seuils 50%/70%/85% |
| `Couleur Alerte RDV` | CRÉÉ | Hex rouge/orange/jaune/vert |
| `Niveau Alerte Réseau` | CRÉÉ | SWITCH sur seuils 60%/80%/90% |
| `Couleur Alerte Réseau` | CRÉÉ | Hex rouge/orange/jaune/vert |
| `Recommandation Volume` | CRÉÉ | Texte adaptatif selon variation N-1 |
| `Nombre Alertes Critiques` | CRÉÉ | COUNTROWS fact_alertes CRITIQUE non clôturée |
| `Nombre Alertes Hautes` | CRÉÉ | COUNTROWS fact_alertes HAUTE non clôturée |
| `Nombre Alertes Moyennes` | CRÉÉ | COUNTROWS fact_alertes MOYENNE non clôturée |
| `Nombre Alertes Ouvertes` | CRÉÉ | COUNTROWS fact_alertes toutes non clôturées |

**Folder : Pilotage Commercial - Mise en forme conditionnelle**

| Mesure | Statut | Note |
|--------|--------|------|
| `CF Variation Texte Volume` | CRÉÉ | Hex couleur selon variation |
| `CF Budget Fill Volume` | CRÉÉ | Hex couleur selon taux atteinte |

**Folder : Pilotage Commercial - Affichage**

| Mesure | Statut | Note |
|--------|--------|------|
| `Libellé Variation Volume vs N-1` | CRÉÉ | Texte ▲/▼ avec FORMAT |
| `Libellé Variation Volume vs MTD-1` | CRÉÉ | Texte ▲/▼ avec FORMAT |

---

### Report (`report.json`)

**Canvas :** 1540 × 1080 px  
**Fond :** #F1F5F9  
**Style corporatif :** Bleu #0A4E97, Rouge #D71920

| Page | Section ID | Ordinal | Nb visualContainers | Statut |
|------|-----------|---------|---------------------|--------|
| Accueil | ReportSection01 | 0 | 87 | CRÉÉ |
| Performance | ReportSection02 | 1 | 60 | CRÉÉ |
| Affaires | ReportSection03 | 2 | 78 | CRÉÉ |
| Réseau MIA | ReportSection04 | 3 | 66 | CRÉÉ |
| Réseau MIA - Tableau | ReportSection04B | 4 | 57 | CRÉÉ |
| Rendez-vous | ReportSection05 | 5 | 61 | CRÉÉ |
| Alertes | ReportSection06 | 6 | 47 | CRÉÉ |
| Glossaire | ReportSection07 | 7 | 15 | CRÉÉ |
| **TOTAL** | — | — | **471** | — |

#### Éléments communs par page (G00_Header)
- Shape fond blanc 1540×88
- Shape ligne bleue #0A4E97 en bas du header
- Textbox titre "Pilotage Commercial" (bold 16pt #0A4E97)
- 7 boutons de navigation pill (Accueil, Performance, Affaires, Réseau MIA, Rendez-vous, Alertes, Glossaire)
- Slicer Périmètre (x=1250)

#### Éléments communs par page (G01_Title_Zone)
- Shape rectangle bleu #0A4E97 (20, 100, 1500×120)
- Textbox titre page (bold 20pt blanc)
- Textbox sous-titre (12pt blanc)

---

### Fichiers de documentation créés

| Fichier | Statut |
|---------|--------|
| `CHANGELOG_BUILD.md` | CRÉÉ (ce fichier) |
| `KPI_STATUS_FINAL.md` | CRÉÉ |
| `RAPPORT_VALIDATION_OVERLAP.md` | CRÉÉ |

---

## Notes techniques

- Tous les `lineageTag` sont des UUID v4 générés uniques
- Les tables placeholder sont en mode `calculated` avec DATATABLE vide `{}`
- Les Field Parameters suivent la structure SELECTCOLUMNS standard Power BI
- Le report.json est en format PBIP natif (non PBIX) — configs sérialisées en JSON string
- Compatibilité : Power BI Desktop >= version avril 2024 (format PBIP stabilisé)

## Actions requises après ouverture dans Power BI Desktop

1. **Remplacer les placeholders** : `fact_affaires`, `budget_affaires`, `fact_alertes` doivent être connectés à des sources de données réelles
2. **Configurer les slicers** : Lier les slicers aux colonnes correspondantes
3. **Vérifier les relations** : Créer les relations entre `fact_affaires`/`budget_affaires` et les dimensions
4. **Publier** : Publier vers Power BI Service après validation
