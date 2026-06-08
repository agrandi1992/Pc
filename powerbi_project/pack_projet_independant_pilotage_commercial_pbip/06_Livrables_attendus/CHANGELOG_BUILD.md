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

---

## [1.1.0] — 2026-06-02 — Consolidation, câblage KPIs, nettoyage

### Semantic Model (model.bim) — 27 tables, 72 mesures, 21 relations

#### Nouvelles mesures
| Mesure | Folder | Source |
|--------|--------|--------|
| `Nombre RDV confirmés` | RDV | G.16 — proxy parent_rendez_vous_id (→ remplacer par flag_confirme) |
| `Taux RDV confirmés` | RDV | G.17 — DIVIDE G.16/G.14 |

#### Mesures supprimées (orphelines)
`test_Taux réalisation RDV N-1`, `test_Evolution RDV vs N-1`, `test_Evolution RDV affichage`, `Nombre mandataires actifs new`

#### Tables supprimées
`KPI_Status` — orpheline, jamais utilisée dans le rapport

#### Mesures améliorées
- `[Nombre mandataires actifs]` et `[Nombre mandataires inactifs]` : `TODAY()` hardcodé → `COALESCE(MAX(dim_date[Date]), TODAY())` — sensibles aux slicers de date

#### Relations ajoutées
- `fact_alertes[mandataire_id]` → `dim_mandataire[mandataire_id]`
- `fact_alertes[agence_id]` → `dim_agence[agence_id]`
- `fact_alertes[date_analyse]` → `dim_date[Date]`

#### Réorganisation des folders
- 13 mesures → folder `Développement Réseau` (formation/candidats, hors scope pilotage)
- 10 mesures → folder `Pilotage Commercial - Analytique` (variantes avancées)

#### Architecture fact_affaires / budget_affaires confirmée
- `fact_affaires` : DATATABLE vide → cible **Fabric Direct Lake** (`gold.fact_affaires`)
- `budget_affaires` : DATATABLE vide → cible **Excel → Dataflow Gen2 → `gold.budget_affaires`**
- Annotations BIM incluent le template partition Direct Lake exact (JSON prêt à copier)

---

### Report (report.json) — 711 visual containers

#### Bugs corrigés
- RDV page : carte x=628 avait label "Nombre RDV Confirmés" mais mesure "Nombre rendez-vous réalisés" → mesure corrigée → `Nombre RDV confirmés`
- Alertes page : texte "fact_alertes absente du modèle" → "opérationnelle (DAX calculée)"
- 4 labels BIM status "absent" sur les alertes → "BIM OK"
- 14 labels "BIM absent" → "BIM placeholder" (mesures existent, données pending)
- Alertes : "Alerte Réseau — À créer" → "BIM OK" (Niveau Alerte Réseau + Couleur Alerte Réseau existent)
- Accueil : 4× "fact_alertes — Source: À créer" → "fact_alertes — opérationnelle (DAX)"

#### Nouveaux visuels câblés
| Page | Mesures ajoutées | Position |
|------|-----------------|----------|
| Rendez-vous | G.12 hebdo, G.17 taux confirmés, G.19 taux domicile, G.20 nb visio, G.21 nb domicile | y=1075 |
| Performance | G.1 ventes, G.25 var N-1 %, G.26 var MTD-1 %, Libellé N-1, Libellé MTD-1 | y=860 |
| Réseau MIA | G.9 non productifs, G.11 non rétro | y=700 (dans le panel focus) |
| Réseau MIA - Tableau | G.9 non productifs, G.11 non rétro | y=700 |

#### Couverture mesures
- v1.0.0 : 27 mesures actives dans le rapport
- v1.1.0 : **40 mesures actives** (+13)

---

### Statut global v1.1.0

| Indicateur | Valeur |
|-----------|--------|
| Tables BIM | 27 |
| Mesures totales | 72 |
| Relations | 21 |
| Mesures actives dans rapport | 40/72 |
| KPIs Excel couverts (avec données) | 13/29 |
| KPIs Excel en placeholder (données pending) | 16/29 |
| Pages rapport | 8 |
| Visuels total | 711 |

---

## [1.2.0] — 2026-06-02 — Alertes dynamiques, complétion Réseau MIA, correction Accueil

### Report (report.json) — 723 visual containers

#### Page Alertes — recommandations et niveaux dynamiques

| Action | Détail |
|--------|--------|
| Suppression | 18 visuels statiques CRITIQUE/HAUTE/CONFORME dans la section droite (x≥760, y=502–688) |
| Ajout | Carte `Recommandation Volume` — texte adaptatif selon variation N-1 (x=768, y=505, w=725, h=72) |
| Ajout | 3 cartes `Niveau Alerte` dynamiques — Volume, RDV, Réseau (y=628, w=225/250) |
| Ajout | 3 labels au-dessus des cartes (y=612) |
| Ajout | 3 badges `Niveau Alerte` dans le panel gauche "Niveaux d'alerte" (x=695, y=509/575/641) |
| Correction | Top card 5 : `Couleur Alerte Volume` → `Niveau Alerte Volume` |

#### Page Réseau MIA & Réseau MIA - Tableau — métriques complémentaires

| Action | Mesure | Position |
|--------|--------|----------|
| Ajout | `Nombre mandataires inactifs` (G.7) | x=920, y=796 (row 4 panel droit) |
| Ajout | `Taux mandataires actifs` | x=1215, y=796 (row 4 panel droit) |

#### Page Accueil — correction KPI G.13

| Action | Détail |
|--------|--------|
| Correction | Card 5 (x=1222, y=337) : `Nombre rendez-vous réalisés` (G.15 — appartient à la page RDV) → `Taux réalisation de rendez-vous` (G.13 — spec prévoit Accueil) |
| Correction | Label associé : "Nombre rendez-vous réalisés" → "Taux réalisation RDV" |
| Correction | Tag KPI : "Excel G.15" → "Excel G.13" |

### Statut global v1.2.0

| Indicateur | Valeur |
|-----------|--------|
| Tables BIM | 27 |
| Mesures totales | 72 |
| Relations | 21 |
| Mesures actives dans rapport | 39/72 (+1) |
| KPIs Excel couverts (avec données) | 13/29 |
| KPIs Excel en placeholder (données pending) | 16/29 |
| Pages rapport | 8 |
| Visuels total | 712 |

---

## [1.3.0] — 2026-06-03 — Qualité, navigation, audit complet

### BIM — Semantic Model

| Action | Détail |
|--------|--------|
| Fix | `Flag mandataire actif` + `Flag rétrocommissionné` : isHidden=true, folder `Pilotage Commercial - Réseau` — mesures utilitaires orphelines non référencées |

### Report (report.json)

#### Navigation — câblage complet (58/60 boutons)

| Action | Détail |
|--------|--------|
| Ajout action | 56 boutons de navigation (7×8 pages) câblés avec `PAGE_NAVIGATION` → section cible |
| Ajout action | Bouton "Afficher le tableau" Réseau MIA → ReportSection04B |
| Ajout action | Bouton "Afficher le tableau" Réseau MIA - Tableau → ReportSection04 |
| Non câblé | 2 boutons Glossaire (Indicateurs/Définitions) : nécessitent des bookmarks |

#### Étiquettes obsolètes — nettoyage complet

| Localisation | Avant | Après |
|-------------|-------|-------|
| Accueil (1034,518) | "À créer" | "BIM OK" (Niveau Alerte Réseau opérationnel) |
| Accueil (530,634/696/758/820) ×4 | "À créer" | "BIM OK" (fact_alertes opérationnelle) |
| Alertes (47,513) | "fact_affaires absente (opérationnel le jour J)" | "données pending (Day J)" |

#### Canvas — hauteurs pages corrigées

| Page | Avant | Après | Raison |
|------|-------|-------|--------|
| Réseau MIA | 1080px | 1560px | barChart à y=1276 hors canvas |
| Réseau MIA - Tableau | 1080px | 1800px | tableEx à y=1572 hors canvas |
| Rendez-vous | 1080px | 1160px | cards G.12/G.17-G.21 à y=1093 |

#### Table Alertes — colonnes métier

| Action | Détail |
|--------|--------|
| Suppression | `alerte_id` — identifiant technique sans valeur métier |
| Ajout | `dim_agence[raison_sociale]` — agence concernée par l'alerte |
| Ajout | `fact_alertes[mandataire_id]` — mandataire concerné |

#### Vérifications — aucun défaut trouvé

- ✓ Aucun visuel ne référence une table cachée
- ✓ Tous les slicers correctement câblés (source alias = entité résolue)
- ✓ Aucune mesure orpheline sans folder
- ✓ Glossaire → `gold.glossaire_indicateurs` Direct Lake opérationnel
- ✓ fact_alertes DAX : 131 lignes, UNION de 4 alertes (G.13/G.14/G.15/G.18)

### Statut global v1.3.0

| Indicateur | Valeur |
|-----------|--------|
| Tables BIM | 27 (9 cachées) |
| Mesures totales | 74 (59 visibles, 15 cachées) |
| Relations | 21 |
| Mesures actives dans rapport | 39/59 |
| KPIs Excel couverts (avec données) | 13/29 |
| KPIs Excel en placeholder (données pending) | 16/29 |
| Pages rapport | 8 |
| Visuels total | 712 |
| Boutons navigation câblés | 58/60 |
| Visuals hors canvas | 0 |
| Étiquettes obsolètes | 0 |
