# MASTER PROMPT — AGENT IA POWER BI
## Pilotage Commercial COMEX — Standard Big Four — Capfinances
### Version 1.0 | Document de référence pour développement PBIP

---

> **CONSIGNE GLOBALE :** Ce document est le référentiel unique pour produire un rapport Power BI  
> de qualité Big Four certifié. Chaque prompt est autonome et séquencé. Ne pas sauter d'étape.  
> Ne jamais inventer de KPI. Valider chaque livrable avant de passer à l'étape suivante.  
> Travailler en mode projet, par itérations. À chaque tâche, prendre de la hauteur sur l'ensemble  
> de ce qui est réalisé et de ce qui reste à faire.

---

## FICHIERS D'ENTRÉE (à joindre à chaque prompt)

| Fichier | Rôle |
|---------|------|
| `PC_LOCAL_v6.zip` | Fichier PBIP de base — point de départ obligatoire |
| `Capfinances_charte_V1.pdf` | Charte graphique officielle — couleurs, typographies, logos |
| `mapping_kpi_maquette_comex_bigfour_v5.xlsx` | Mapping KPI Excel → DAX → visuel |
| `maquette_b64.json` | Images des 8 pages de maquette encodées en base64 |

**Convention nommage Power BI :**
```
PAGE_GROUPE_ELEMENT   ex: PERF_KPI1_VAL, NAV_BTN_ACC, GRP_HDR
```

---

## PALETTE COULEURS CAPFINANCES (charte officielle)

| Token | Hex | Usage |
|-------|-----|-------|
| BP (Brand Primary) | #051E73 | Sidebar, titres principaux, KPI valeurs |
| B8 | #3C41BE | Header, boutons actifs |
| B6 | #8096FF | Accents secondaires |
| B2 | #E6EBFA | Fonds cards, bandes alternées tableau |
| RN (Rouge Négatif) | #F05062 | Variations négatives, alertes critiques |
| GP (Vert Positif) | #00B050 | Variations positives, statuts OK |
| GS (Gris Surface) | #F6F7FB | Fond page content |
| WH | #FFFFFF | Blanc — texte sur fond sombre |
| TM (Texte Moyen) | #374151 | Labels, descriptions |
| TL (Texte Léger) | #6B7280 | Sous-titres, métadonnées |
| GR (Gris Bordure) | #E5E7EB | Séparateurs, bordures |

---

## TYPOGRAPHIE

| Élément | Police | Taille | Graisse | Couleur |
|---------|--------|--------|---------|---------|
| Titre page (header) | Segoe UI | 18pt | SemiBold | #FFFFFF |
| Sous-titre page | Segoe UI | 10pt | Regular | #C8D4F0 |
| Titre section | Segoe UI | 11pt | SemiBold | BP #051E73 |
| KPI valeur principale | Segoe UI | 22pt | Bold | BP #051E73 |
| KPI label | Segoe UI | 9pt | Regular | TM #374151 |
| KPI variation | Segoe UI | 10pt | SemiBold | GP/#RN selon signe |
| Corps tableau | Segoe UI | 9pt | Regular | #1F2937 |
| En-tête tableau | Segoe UI | 9pt | SemiBold | #FFFFFF fond BP |
| Navigation sidebar | Segoe UI | 10pt | Regular | #C8D4F0 |
| Navigation active | Segoe UI | 10pt | SemiBold | #FFFFFF |

---

## DIMENSIONS CANVAS & ZONES

```
Canvas total : 1440 × 900 px
Sidebar      : x=0,    y=0,   w=220, h=900   (GRP_NAV)
Header       : x=220,  y=0,   w=1220, h=65   (GRP_HDR)
Content area : x=220,  y=65,  w=1220, h=835
─────────────────────────────────────────────
Content X start : CX = 235  (220 + 15 padding)
Content Y start : CY = 80   (65 + 15 padding)
Content W usable: 1190 px
─────────────────────────────────────────────
KPI row height  : 130 px    (y= CY=80)
Charts y start  : CY + 150 = 230 px
Charts height   : 265 px
Table y start   : CY + 430 = 510 px
Table height    : 350 px
```

---

## STRUCTURE Z-INDEX (couches visuelles)

| Couche | Z range | Éléments |
|--------|---------|----------|
| Fond page | 1 | CONTENT_BG |
| Content | 2–12 | Tous visuels de données |
| Groups content | 3 | Conteneurs groupe |
| Header | 80–85 | GRP_HDR et enfants |
| Sidebar | 90–95 | GRP_NAV et enfants |

---

## HIÉRARCHIE GROUPES (Volet Sélection)

```
GRP_NAV                    ← sidebar navigation (toutes pages)
  NAV_BG, NAV_LOGO, NAV_SUBTITLE, NAV_SEP
  NAV_BTN_ACC/PERF/AFF/RES/RDV/MAN/ALT/GLO
  NAV_HL_{PAGE}, NAV_BAR_{PAGE}  (highlight page active)
  NAV_VERSION

GRP_HDR                    ← header (toutes pages)
  HDR_BG, HDR_TITLE, HDR_SUBTITLE
  HDR_SLC_ANNEE, HDR_SLC_EXERCICE, HDR_SLC_AGENCE
  HDR_SLC_CENTRE, HDR_SLC_MANDATAIRE, HDR_SLC_PRODUIT
  HDR_BTN_SELECTIONS

GRP_{PG}_KPI               ← rangée KPI cards
  {PG}_KPI{n}_BG, {PG}_KPI{n}_ACCENT, {PG}_KPI{n}_LBL
  {PG}_KPI{n}_VAL, {PG}_KPI{n}_VAR, {PG}_KPI{n}_ICON

GRP_{PG}_SEC1              ← section graphique gauche
  {PG}_SEC1_TITLE, {PG}_SEP1, {PG}_CHART1_BG, {PG}_CHART_*

GRP_{PG}_SEC2              ← section graphique droite
  {PG}_SEC2_TITLE, {PG}_SEP2, {PG}_CHART2_BG, {PG}_CHART_*

GRP_{PG}_TABLE             ← section tableau détail
  {PG}_SEC3_TITLE, {PG}_SEP3, {PG}_TBL_*

CONTENT_BG                 ← fond page — NON groupé
```

---


---
# PHASE 0 — AUDIT DU FICHIER PBIP DE BASE

## ✅ CHECKLIST DE VALIDATION AVANT EXÉCUTION
```
□ Le fichier PC_LOCAL_v6.zip s'ouvre sans erreur dans Power BI Desktop
□ Les 8 pages sont présentes : Accueil, Performance, Affaires, Réseau MIA,
  Rendez-vous, Mandataires, Alertes, Glossaire
□ model.bim se charge (aucune erreur de partition dans la barre d'état)
□ 27 tables visibles dans le volet Données
□ 75+ mesures dans la table _Indicateurs
□ Aucune mesure affiche [Erreur] dans la vue rapport
□ Volet Sélection : chaque page a des groupes GRP_* nommés
□ 0 visuel sans nom dans le volet Sélection
```

## PROMPT 0A — AUDIT STRUCTUREL

**POINT DE DÉPART :** Fichier `PC_LOCAL_v6.zip` → décompresser → ouvrir `PCL/Pilotage_Commercial.pbip`

**TÂCHE :**
1. Ouvrir le fichier PBIP fourni en pièce jointe
2. Parcourir les 8 pages et noter pour chaque page :
   - Liste des visuels présents (nom, type, position)
   - Liste des mesures utilisées
   - Éléments manquants par rapport à la maquette (images base64 en pièce jointe)
   - Éléments incorrects (type de visuel, position, taille, couleur)
3. Ouvrir le fichier model.bim et noter :
   - Tables présentes vs attendues
   - Mesures présentes vs manquantes
   - Relations manquantes
4. Produire un rapport d'écart PBIP actuel vs maquette cible

**VALIDATION :**
- Ne modifier aucun fichier dans cette phase
- Produire uniquement un document d'écart structuré
- Comparer visuel par visuel avec les images de maquette encodées en base64

---

## PROMPT 0B — AUDIT CHARTE GRAPHIQUE

**TÂCHE :**
1. Lire `Capfinances_charte_V1.pdf` intégralement
2. Extraire et documenter :
   - Palette couleurs officielle (tous les codes hex)
   - Polices autorisées et leurs variantes
   - Règles de mise en page (marges, espacements, grilles)
   - Usage du logo (tailles, zones d'exclusion)
   - Règles de mise en forme conditionnelle (couleurs positif/négatif)
   - Exemples de visualisations validées
3. Comparer avec la palette définie dans ce document
4. Signaler tout écart avec la charte officielle

---


---
# PHASE 1 — FICHIER MAPPING KPI DÉTAILLÉ

## ✅ CHECKLIST DE VALIDATION
```
□ Chaque KPI visible dans la maquette a une entrée dans le mapping
□ Chaque KPI mappé existe dans model.bim (mesure ou colonne)
□ Aucun KPI inventé (tout doit venir de l'Excel source ou du BIM)
□ Les KPI "À RETIRER" de la feuille 4 de l'Excel ne sont PAS intégrés
□ Le mapping distingue bien : KPI affiché | mesure DAX | table source
```

## PROMPT 1 — GÉNÉRATION DU FICHIER MAPPING

**TÂCHE :**
Créer un fichier `MAPPING_KPI_FINAL.csv` avec les colonnes suivantes :

```
PAGE | ZONE | KPI_MAQUETTE | MESURE_DAX | TABLE_BIM | FORMAT | 
COND_FORMAT | NOTES
```

**Règles impératives :**
1. Ne mapper que les KPI présents dans la maquette ET validés dans l'Excel
2. Ne pas inventer de mesures DAX — utiliser uniquement celles de `_Indicateurs`
3. Si une mesure DAX n'existe pas, l'indiquer dans la colonne NOTES (À CRÉER)
4. Référencer l'image maquette de la page correspondante pour chaque KPI

**KPI VALIDÉS (source : feuille "KPI VALIDÉS" de l'Excel) :**

| Périmètre | KPI Validé | Mesure DAX attendue |
|-----------|------------|---------------------|
| RÉSEAU | ORIASÉS | Nombre MIA oriasés |
| RÉSEAU | MIA PRODUCTIFS | Nombre mandataires productifs |
| RÉSEAU | TURNOVER MANDATAIRE | À créer si absent |
| PERFORMANCE FINANCE | NB CONTRATS | Nombre ventes |
| PERFORMANCE FINANCE | COLLECTE | Volume affaires produites |
| PERFORMANCE FINANCE | CAA | Volume affaires commissionnées |
| PERFORMANCE FINANCE | CAA YTD | (cumul YTD) |
| PORTEFEUILLE | TAUX DE RÉTENTION PP 12 MOIS | À créer si absent |
| PORTEFEUILLE | TAUX DE REPRISE | À créer si absent |
| PORTEFEUILLE | VOLUME DES ENCOURS | À créer si absent |
| AVANCEMENT | TAUX D'AVANCEMENT CONTRATS | Taux atteinte Budget N Volume |
| AVANCEMENT | TAUX D'AVANCEMENT COLLECTE | À créer si absent |
| AVANCEMENT | TAUX D'AVANCEMENT CAA | À créer si absent |

**KPI À NE PAS INTÉGRER (source : feuille "À RETIRER") :**
- Marge / Taux de marge
- Alertes / Recommandations automatiques
- Répartition des indicateurs clés (non additive)
- Mode de distribution (non confirmé)

**MAPPING DÉTAILLÉ PAR PAGE :**

### PAGE : ACCUEIL (Vue d'ensemble)
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Volume affaires en M€ | Volume affaires produites | #,##0.00 "M€" | Neutre |
| KPI 1 variation | vs N-1 % | Variation vs N-1 Volume Affaires (%) | +0.0% ; -0.0% | Vert si >0, Rouge si <0 |
| KPI 2 | Volume affaires en nombre | Nombre affaires produites | #,##0 | Neutre |
| KPI 3 | Volume affaires commissionnées | Volume affaires commissionnées | #,##0.00 "M€" | Neutre |
| KPI 4 | Montant moyen rétro | Montant moyen de rétrocommission | #,##0 "K€" | Neutre |
| KPI 5 | RDV actifs | Nombre rendez-vous prévus | #,##0 | Neutre |
| KPI 6 | RDV réalisés | Nombre rendez-vous réalisés | #,##0 | Neutre |
| KPI 7 | Taux réalisation RDV | Taux réalisation de rendez-vous | 0.0% | Vert si >60%, Orange si 40-60%, Rouge si <40% |
| KPI 8 | Mandataires actifs | Nombre mandataires actifs | #,##0 | Neutre |
| KPI 9 | Mandataires productifs | Nombre mandataires productifs | #,##0 | Neutre |
| Graphique 1 | Évolution volumes d'affaires | Volume affaires produites / mois | Courbe mensuelle | Ligne BP #051E73 |
| Graphique 2 | Performance par agence | Volume affaires produites / agence | Barres horizontales | Dégradé BP→B6 |
| Graphique 3 | Répartition par typologies produit | Volume / dim_produit | Barres empilées | Palette produit |
| Alerte | Alertes commerciales prioritaires | Priorité Alerte Maximale | Tableau | Couleur Alerte selon niveau |

### PAGE : PERFORMANCE COMMERCIALE
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Volume affaires en M€ | Volume affaires produites | #,##0.00 "M€" | Variation vs N-1 |
| KPI 1 var | variation % vs N-1 | Variation vs N-1 Volume Affaires (%) | +0% | Vert/Rouge |
| KPI 2 | Montant rétrocommission | Montant rétrocommission | #,##0.00 "M€" | Neutre |
| KPI 3 | Volume affaires commissionnées | Volume affaires commissionnées | #,##0.00 "M€" | Neutre |
| KPI 4 | Taux atteinte budget | Taux atteinte Budget N Volume | 0.0% | Vert si ≥100%, Orange 80-100%, Rouge <80% |
| Graphique 1 | Évolution volumes d'affaires | Volume mensuel | Courbe | Ligne BP |
| Graphique 2 | Performance par agence | Volume / agence | Barres horizontales | Ordre décroissant |
| Graphique 3 | KPI-Budget vs réalisé | Volume réalisé + Budget | Barres groupées + ligne | Bleu réalisé, Pointillé budget |
| Tableau | Détail performance | Multi-mesures par agence | Grille | Alternance B2/WH |

### PAGE : SUIVI DES AFFAIRES
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Nombre affaires produites | Nombre affaires produites | #,##0 "K" | Neutre |
| KPI 1 var | variation | Variation vs N-1 | % | Vert/Rouge |
| KPI 2 | Nombre affaires commissionnées | Nombre affaires commissionnées | #,##0 "K" | Neutre |
| KPI 3 | Nombre affaires en instance | Nombre affaires en instance | #,##0 "K" | Neutre |
| KPI 4 | Nombre cross-sell | À identifier dans BIM | #,##0 "K" | Neutre |
| KPI 5 | Volume affaires produites | Volume affaires produites | #,##0.00 "M€" | Neutre |
| KPI 6 | Volume en instance | Volume affaires en instance | #,##0.00 "M€" | Neutre |
| Tableau | Détail affaires | Multi-colonnes par mandataire | Grille détaillée | Cond. format taux budget |

### PAGE : RÉSEAU MIA ET GÉOGRAPHIE
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Nombre de MIA actifs | Nombre mandataires actifs | #,##0 "K" | Neutre |
| KPI 2 | Nombre de MIA actifs productifs | Nombre mandataires productifs | #,##0 | Neutre |
| KPI 3 | Nombre de MIA productifs (sous-réseau) | Nombre MIA oriasés | #,##0 | Neutre |
| KPI 4 | Nombre de MIA non productifs | Nombre mandataires non productifs | #,##0 | Rouge si élevé |
| KPI 5 | Montant rétrocommissions | Montant rétrocommission | #,##0 "K€" | Neutre |
| Carte | Répartition mandataires par agence | Nombre mandataires / dim_agence | Carte France (ArcGIS/Shape) | Dégradé bleu |
| Graphique 1 | Répartition MIA par CSP | Nombre / catégorie | Barres | BP |
| Graphique 2 | MIA productifs par agence | Nombre productifs / agence | Barres | BP→B6 |
| Tableau | Détail MIA | Multi-mesures par agence/RTC | Grille | Alternance |

### PAGE : SUIVI DES RENDEZ-VOUS
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Nombre RDV prévus | Nombre rendez-vous prévus | #,##0 "K" | Neutre |
| KPI 2 | Nombre RDV réalisés | Nombre rendez-vous réalisés | #,##0 "K" | Neutre |
| KPI 3 | Taux de réalisation | Taux réalisation de rendez-vous | 0.0% | Vert/Orange/Rouge |
| KPI 4 | RDV domicile | Nombre rendez-vous réalisés à domicile | #,##0 "K" | Neutre |
| Graphique 1 | Répartition par type (donut) | Nombre / dim_type_rendez_vous_client | Anneau | Palette B6/B8/BP |
| Graphique 2 | RDV réalisés par mois | Nombre réalisés mensuel | Barres groupées | BP |
| Tableau | Total RDV par agence | Multi-mesures | Grille | Alternance |
| Encadré | Taux de réalisation final | Taux réalisation de rendez-vous | Grand nombre | Vert si ≥62% |

### PAGE : MANDATAIRES
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Mandataires | Nombre mandataires actifs | #,##0 | Neutre |
| KPI 2 | Mandataires actifs | Nombre mandataires actifs | #,##0 | Neutre |
| KPI 3 | Mandataires productifs | Nombre mandataires productifs | #,##0 | Neutre |
| KPI 4 | Mandataires non productifs | Nombre mandataires non productifs | #,##0 | Rouge si élevé |
| KPI 5 | Taux mandataires actifs (%) | Taux mandataires actifs | 0.0% | Vert/Rouge |
| KPI 6 | Mandataires non productifs total | Nombre mandataires non productifs | #,##0 | Rouge |
| KPI 7 | Montant production | Volume affaires produites | #,##0.00 "M€" | Neutre |
| KPI 8 | Montant rétro | Montant rétrocommission | #,##0.00 "M€" | Neutre |
| Tableau | Détail mandataires | Multi-mesures par agence/RTC | Grille hiérarchique | Cond. format productivité |

### PAGE : ALERTES COMMERCIALES
| Zone | KPI Affiché | Mesure DAX | Format | Mise en forme cond. |
|------|-------------|------------|--------|---------------------|
| KPI 1 | Alertes actives | Nombre Alertes Ouvertes | #,##0 | Rouge si >0 |
| KPI 2 | Alertes critiques | Nombre Alertes Critiques | #,##0 | Rouge vif |
| KPI 3 | Alertes hautes | Nombre Alertes Hautes | #,##0 | Orange |
| KPI 4 | Alertes moyennes | Nombre Alertes Moyennes | #,##0 | Jaune |
| KPI 5 | Opportunités | À définir | #,##0 | Vert |
| KPI 6 | Total alertes ouvertes | Nombre Alertes Ouvertes | #,##0 | Rouge |
| Tableau | Tableau actionnable alertes | Multi-colonnes fact_alertes | Grille | Couleur Alerte selon niveau |
| Encadré | Logique d'action | Recommandation Alerte Volume / RDV | Texte | Selon niveau |

### PAGE : GLOSSAIRE DES INDICATEURS
| Zone | Élément | Source | Format |
|------|---------|--------|--------|
| Tableau | Indicateur | glossaire_indicateurs.indicateur | Texte |
| Tableau | Définition | glossaire_indicateurs.definition | Texte |
| Tableau | Règle de calcul | glossaire_indicateurs.regle_calcul | Texte |
| Tableau | Comment l'utiliser | glossaire_indicateurs.comment_utiliser | Texte |
| Tableau | Disponible | glossaire_indicateurs.disponible | Texte + badge couleur |
| Tableau | Commentaires | glossaire_indicateurs.commentaires | Texte italic |
| KPI compteur | KPI documentés | Nombre lignes glossaire | #,##0 |

---


---
# PHASE 2 — MODÈLE SÉMANTIQUE (model.bim)

## ✅ CHECKLIST DE VALIDATION
```
□ Toutes les tables gold sont en mode Import (schemaName: "gold")
□ Toutes les mesures manquantes identifiées en Phase 1 sont créées
□ Les relations sont complètes et sans ambiguïté
□ Aucune mesure ne génère d'erreur dans Power BI Desktop
□ Les tables de paramètre (FP_*, Période_Affichage) sont correctement structurées
□ Les partitions M utilisent #table(...) avec données fictives cohérentes
□ Le BIM se charge en < 30 secondes
```

## PROMPT 2A — VÉRIFICATION ET COMPLÉTION DU BIM

**POINT DE DÉPART :** `PCL/Pilotage_Commercial.SemanticModel/model.bim` du ZIP fourni

**TÂCHE :**
1. Lire le BIM actuel et identifier les mesures manquantes par rapport au mapping Phase 1
2. Créer les mesures DAX manquantes dans la table `_Indicateurs` :

```dax
// Exemple de structure pour mesures à créer
Taux d'Avancement Collecte = 
    DIVIDE([Volume affaires produites], [Budget affaires en euro], 0)

Taux d'Avancement Contrats = 
    DIVIDE([Nombre affaires produites], [Budget affaires en nombre], 0)

Taux d'Avancement CAA = 
    DIVIDE([Volume affaires commissionnées], [Budget affaires en euro], 0)
```

3. Vérifier la cohérence des relations :
   - fact_affaire → dim_date (clé: date_affaire → date_id)
   - fact_affaire → dim_agence (clé: agence_id)
   - fact_affaire → dim_mandataire (clé: mandataire_id)
   - fact_affaire → dim_produit (clé: produit_id)
   - fact_rendez_vous_client → dim_mandataire
   - fact_activite_mandataire → dim_mandataire
   - fact_alertes → dim_agence

4. Ajouter les mesures de mise en forme conditionnelle si absentes :
```dax
Couleur KPI Taux Budget = 
    IF([Taux atteinte Budget N Volume] >= 1, "#00B050",
       IF([Taux atteinte Budget N Volume] >= 0.8, "#F59E0B", "#F05062"))
```

**VALIDATION POST-EXÉCUTION :**
- Ouvrir Power BI Desktop → Actualiser le modèle
- Vérifier 0 erreurs dans le volet Erreurs
- Vérifier que chaque mesure ajoutée retourne une valeur non nulle sur données fictives

---

## PROMPT 2B — TABLE GLOSSAIRE COMPLÈTE

**TÂCHE :**
Vérifier et compléter la table `glossaire_indicateurs` avec au minimum 12 indicateurs :

```
indicateur | definition | regle_calcul | comment_utiliser | disponible | commentaires
```

| Indicateur | Définition |
|------------|-----------|
| Volume affaires produites | Somme des montants d'affaires signées sur la période |
| Nombre affaires produites | Nombre de contrats signés |
| Volume affaires commissionnées | Montant des affaires ayant généré une rétrocommission |
| Nombre mandataires actifs | Mandataires ayant au moins une activité sur la période |
| Nombre mandataires productifs | Mandataires ayant produit au moins une affaire |
| Taux réalisation RDV | Ratio RDV réalisés / RDV prévus |
| Montant rétrocommission | Montant total versé en rétrocommission |
| Nombre Alertes Ouvertes | Alertes non résolues à date |
| Taux atteinte Budget N Volume | Réalisé vs Budget en volume d'affaires |
| Nombre MIA oriasés | Mandataires inscrits à l'ORIAS |
| Variation vs N-1 | Évolution en % par rapport à la même période N-1 |
| Taux mandataires actifs | % de mandataires actifs sur l'effectif total |

---


---
# PHASE 3 — CONSTRUCTION VISUELLE PAGE PAR PAGE

## RÈGLES TRANSVERSALES (valables pour TOUTES les pages)

```
RÈGLE 1 — Nommage : TOUS les visuels doivent avoir un nom selon convention PAGE_GROUPE_ELEMENT
RÈGLE 2 — Groupement : TOUS les visuels (sauf CONTENT_BG) doivent être dans un GRP_*
RÈGLE 3 — Position : x/y/z/width/height du VC = layouts[0].position (identiques)
RÈGLE 4 — Pas de visuel hors canvas (x+w ≤ 1440, y+h ≤ 900)
RÈGLE 5 — Pas de visuel superposé à un autre sauf si z-index différent intentionnel
RÈGLE 6 — Header et sidebar identiques sur toutes les pages
RÈGLE 7 — Vérification hauteur : regarder la page entière avant de valider
RÈGLE 8 — Titres en MAJUSCULES dans les visuels (convention maquette)
```

## STRUCTURE KPI TILE (composant réutilisable)

```
Dimensions : w=285, h=130
Composition :
  {PG}_KPI{n}_BG     : shape fond blanc, bordure GR #E5E7EB 1px, radius 4px
  {PG}_KPI{n}_ACCENT : shape barre colorée gauche, w=6, h=130, fill=BP #051E73
  {PG}_KPI{n}_ICON   : textbox icône Unicode (optionnel), 16pt, BP, x+=20
  {PG}_KPI{n}_LBL    : textbox label, 9pt Regular TM, x+=30
  {PG}_KPI{n}_VAL    : card valeur principale, 22pt Bold BP, x+=24, y+=40
  {PG}_KPI{n}_VAR    : card variation, 10pt SemiBold, couleur conditionnelle, y+=90

Espacement entre tiles : 14px
4 tiles sur une ligne → x positions : 235, 534, 833, 1132
```

## STRUCTURE HEADER (GRP_HDR)

```
HDR_BG        : shape x=220 y=0 w=1220 h=65 fill=BP #051E73
HDR_TITLE     : textbox "{TITRE PAGE}" 18pt SemiBold White x=235 y=12 w=400 h=28
HDR_SUBTITLE  : textbox "{sous-titre}" 10pt Regular #C8D4F0 x=235 y=38 w=500 h=18
HDR_SLC_ANNEE : slicer "Période" x=640 y=8 w=90 h=48 dropdown
HDR_SLC_EXERCICE: slicer "Exercice" x=740 y=8 w=90 h=48 dropdown
HDR_SLC_AGENCE  : slicer "Agence" x=840 y=8 w=110 h=48 dropdown
HDR_SLC_CENTRE  : slicer "Centre d'affaires" x=960 y=8 w=130 h=48 dropdown
HDR_SLC_MANDAT  : slicer "Mandataires" x=1100 y=8 w=110 h=48 dropdown
HDR_SLC_PRODUIT : slicer "Source produit" x=1220 y=8 w=110 h=48 dropdown
HDR_BTN_SELECT  : button "SÉLECTIONS ▼" x=1340 y=12 w=80 h=40 fill=B8 #3C41BE
```

## STRUCTURE SIDEBAR (GRP_NAV)

```
NAV_BG       : shape x=0 y=0 w=220 h=900 fill=BP #051E73
NAV_LOGO     : textbox "GROUPE
Premium.
CAPFINANCES" 
               x=15 y=16 w=190 h=50 White SemiBold 10pt
NAV_SUBTITLE : textbox logo subtitle x=15 y=44 10px
NAV_SEP      : shape séparateur x=15 y=64 w=190 h=1 fill=#3C41BE
NAV_BTN_*    : actionButton h=44 w=200 x=10 navigation par page
               → texte White 10pt, icône Unicode devant le label
               → page active : fond B8 #3C41BE + barre gauche 4px White
Nav buttons :
  NAV_BTN_ACC  y=78  → "⌂ Accueil"
  NAV_BTN_PERF y=130 → "📊 Performance"
  NAV_BTN_AFF  y=182 → "📁 Affaires"
  NAV_BTN_RES  y=234 → "🗺 Réseau MIA"
  NAV_BTN_RDV  y=286 → "📅 Rendez-vous"
  NAV_BTN_MAN  y=338 → "👥 Mandataires"
  NAV_BTN_ALT  y=390 → "🔔 Alertes"
  NAV_BTN_GLO  y=442 → "📖 Glossaire"
NAV_VERSION : textbox "PBIP v6 | 2025-06" x=15 y=878 8pt TL
```

---


---
## PROMPT 3.ACC — PAGE ACCUEIL

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ 9 KPI tiles visibles dans GRP_ACC_KPI

□ 3 graphiques présents (courbe mensuelle, barres agences, barres produit)

□ Section alertes avec tableau fact_alertes

□ Section finance et clients en bas droite

□ Taux réalisation RDV avec mise en forme conditionnelle

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "ACCUEIL" dans maquette_b64.json

**POINT DE DÉPART :** Page "Accueil" du PBIP fourni — modifier les visuels existants,
ne pas créer de nouvelle page.

**MODIFICATIONS À APPORTER :**

### 1. Header (GRP_HDR) — 6 slicers + bouton
- Ajouter les slicers manquants : Période (date range), Exercice, Agence,
  Centre d'affaires, Mandataires, Source produit
- Bouton "SÉLECTIONS ▼" en haut droite x=1340

### 2. Rangée KPI (GRP_ACC_KPI) — y=80, 9 tiles sur 2 rangées
**Rangée 1 (y=80) — 4 tiles w=285 h=130 :**
- ACC_KPI1 : Volume affaires en M€ | mesure: Volume affaires produites | format: #,##0.00 "M€"
  variation: Variation vs N-1 Volume Affaires (%) | icône: 📊
- ACC_KPI2 : Volume affaires en nombre | mesure: Nombre affaires produites | format: #,##0
  variation: Libellé Variation Volume vs N-1
- ACC_KPI3 : Volume affaires commissionnées | mesure: Volume affaires commissionnées | format: #,##0.00 "M€"
- ACC_KPI4 : Montant moyen rétro | mesure: Montant moyen de rétrocommission | format: #,##0 "K€"

**Rangée 2 (y=228) — 5 tiles w=222 h=110 :**
- ACC_KPI5 : RDV actifs | mesure: Nombre rendez-vous prévus | icône: 📅
- ACC_KPI6 : RDV réalisés | mesure: Nombre rendez-vous réalisés | icône: ✅
  Taux variation: Taux réalisation de rendez-vous (couleur conditionnelle)
- ACC_KPI7 : Taux réalisation RDV | mesure: Taux réalisation de rendez-vous | format: 0.0%
  → Couleur fond conditionnelle : vert ≥60%, orange 40-60%, rouge <40%
- ACC_KPI8 : Mandataires actifs | mesure: Nombre mandataires actifs | icône: 👥
- ACC_KPI9 : Mandataires productifs | mesure: Nombre mandataires productifs

### 3. Section gauche — Évolution volumes (GRP_ACC_SEC1)
- y=358 x=235 w=590 h=265
- ACC_SEC1_TITLE : "ÉVOLUTION DES VOLUMES D'AFFAIRES" 11pt SemiBold BP
- ACC_SEP1 : séparateur h=2 fill=B6
- ACC_CHART_EVOL : lineChart x=240 y=388 w=580 h=225
  Axe X: dim_date[mois_annee], Axe Y: Volume affaires produites
  Couleur ligne: BP #051E73, épaisseur 2px, marqueurs ronds
  Grille horizontale légère GR, fond white

### 4. Section droite — Performance par agence (GRP_ACC_SEC2)
- y=358 x=845 w=590 h=265
- ACC_SEC2_TITLE : "PERFORMANCE PAR AGENCE" 11pt SemiBold BP
- ACC_CHART_AGENCE : barChart horizontal x=850 y=388 w=580 h=225
  Catégorie: dim_agence[nom_agence], Valeur: Volume affaires produites
  Couleur: BP #051E73, tri décroissant, étiquettes valeurs affichées

### 5. Section bas gauche — Répartition produit (GRP_ACC_SEC3)
- y=645 x=235 w=590 h=240
- ACC_SEC3_TITLE : "RÉPARTITION DES AFFAIRES PAR TYPOLOGIES DE PRODUITS"
- ACC_CHART_PRODUIT : clusteredBarChart ou stackedBar
  Catégorie: dim_produit[famille_produit], Valeur: Volume affaires produites

### 6. Section bas droite — Alertes prioritaires (GRP_ACC_ALERT)
- y=645 x=845 w=590 h=240
- ACC_ALERT_TITLE : "ALERTES COMMERCIALES PRIORITAIRES" fond RN #F05062 text White
- ACC_TBL_ALERT : table fact_alertes colonnes: agence, domaine, recommandation, niveau
  Mise en forme cond.: rouge si critique, orange si haut, jaune si moyen

**VALIDATION POST-EXÉCUTION :**


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_ACC_KPI
▼ GRP_ACC_SEC1
▼ GRP_ACC_SEC2
▼ GRP_ACC_SEC3
▼ GRP_ACC_ALERT
▼ GRP_ACC_FINANCE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.PERF — PAGE PERFORMANCE

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ 4 KPI tiles : Volume M€, Rétro M€, Commissionnées M€, Taux budget %

□ KPI 1 affiche variation +/- avec couleur conditionnelle

□ Graphique 1 (gauche) : courbe évolution mensuelle

□ Graphique 2 (droite) : barres horizontales par agence triées

□ Graphique 3 (haut droite) : budget vs réalisé

□ Tableau détail : Agence | Autres | Centre | Affaires | Budget | Réalisé à % | ...

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "PERFORMANCE" dans maquette_b64.json

**POINT DE DÉPART :** Page "Performance" du PBIP fourni

**KPI TILES (y=80, 4 tiles w=285 h=130) :**
- PERF_KPI1 : "VOLUME D'AFFAIRES EN M€"
  Valeur: Volume affaires produites | format: #,##0.00 "M€"
  Variation: Variation vs N-1 Volume Affaires (%) | Sous-label: "Budget M,€DD"
  Couleur variation: GP vert si >0, RN rouge si <0
- PERF_KPI2 : "MONTANT RÉTROCOMMISSION"
  Valeur: Montant rétrocommission | format: #,##0.00 "M€"
  Sous-label: "Budget M€DD" en gris
- PERF_KPI3 : "VOLUME AFFAIRES COMMISSIONNÉES"  
  Valeur: Volume affaires commissionnées | format: #,##0.00 "M€"
  Variation: Évolution mandataires rétro vs N-1 (%)
- PERF_KPI4 : "TAUX D'ATTEINTE BUDGET"
  Valeur: Taux atteinte Budget N Volume | format: 0.0%
  → Fond tile coloré selon seuil: vert ≥100%, orange 80-100%, rouge <80%
  → Afficher "vs N-1" en sous-libellé

**GRAPHIQUES :**
- PERF_CHART_EVOL (GRP_PERF_SEC1) x=235 y=230 w=590 h=265
  Type: lineChart avec zone ombrée
  Axe X: mois_annee, Valeur: Volume affaires produites mensuel
  Style: ligne BP 2px, zone fill B2 transparent 30%, grille légère
  
- PERF_CHART_AGENCE (GRP_PERF_SEC2) x=845 y=230 w=400 h=265
  Type: barChart horizontal
  Cat: dim_agence, Val: Volume affaires produites
  Tri décroissant, étiquettes droite, couleur BP→B6 dégradé
  
- PERF_CHART_BUDGET (GRP_PERF_SEC2) x=1255 y=230 w=170 h=265
  Type: clusteredColumnChart barres + ligne budget
  Cat: dim_date[trimestre], Val: Volume réalisé + Budget affaires en euro
  Couleur réalisé: BP, ligne budget: RN pointillé

**TABLEAU (GRP_PERF_TABLE) y=510 x=235 w=1190 h=375 :**
- PERF_TBL_DETAIL : table avec colonnes:
  Agence | Autres | Centre d'affaires | Affaires produites | Budget | 
  Réalisé à % | Run Rate M€ | vs N-1 | Affaires commis. | Affaires inst. | Rétrocommissions
- En-tête: fond BP #051E73, texte White 9pt SemiBold
- Corps: alternance White / B2 #E6EBFA par ligne
- Colonne "Réalisé à %" : mise en forme cond. couleur fond (vert/orange/rouge)
- Total bas de tableau : fond B8 #3C41BE texte White Bold


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_PERF_KPI
▼ GRP_PERF_SEC1
▼ GRP_PERF_SEC2
▼ GRP_PERF_TABLE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.AFF — PAGE AFFAIRES

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ Filtre comparaison période visible en haut (Choisir période de comparaison)

□ KPI row 1 : 4 tiles Nombre (produites, commissionnées, cross, instance)

□ KPI row 2 : Volumes M€ avec variations

□ Graphique gauche présent

□ Graphique droite : placeholder 'en attente livraison prod' si pas de visuel

□ Tableau avec colonnes Agence/RTC/Mandataires/CA/Affaires/Budget/Moyen...

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "AFFAIRES" dans maquette_b64.json

**POINT DE DÉPART :** Page "Affaires" du PBIP fourni

**FILTRE COMPARAISON (hors GRP_HDR) :**
- AFF_SLC_COMPARE : slicer "Choisir période de comparaison" x=850 y=68 w=200 h=28
  Style chip/dropdown, fond B2, texte BP, label "Choisir période de comparaison : Mars 2025"

**KPI ROW 1 (y=100, 4 tiles w=285 h=105) — Nombre d'affaires :**
- AFF_KPI1 : "NOMBRE AFFAIRES PRODUITES" | Nombre affaires produites | #,##0 "K"
  Variation: Variation vs N-1 couleur GP/RN
- AFF_KPI2 : "NOMBRE AFFAIRES COMMISSIONNÉES" | Nombre affaires commissionnées | #,##0 "K"
  Sous-label: variation %
- AFF_KPI3 : "NOMBRE CROSS-SELL" | mesure cross (à identifier) | #,##0 "K"
- AFF_KPI4 : "NOMBRE EN INSTANCE" | Nombre affaires en instance | #,##0 "K"

**KPI ROW 2 (y=220, 4 tiles w=285 h=105) — Volumes M€ :**
- AFF_KPI5 : "VOLUME AFFAIRES PRODUITES" | Volume affaires produites | #,##0.00 "M€"
  Variation N-1 et vs période comparaison
- AFF_KPI6 : "VOLUME AFFAIRES EN INSTANCE" | Volume affaires en instance | #,##0.00 "M€"  
- AFF_KPI7 : "VOLUME AFFAIRES COMMISSIONNÉES" | Volume affaires commissionnées | #,##0.00 "M€"
- AFF_KPI8 : "NOMBRE DE RÉTROCOMMISSIONS" | Montant rétrocommission | #,##0.00 "M€"

**GRAPHIQUES (y=340) :**
- AFF_CHART_TYPES (GRP_AFF_SEC1) x=235 y=356 w=590 h=240
  Type: clusteredColumnChart
  Cat: dim_produit[famille_produit], Val: Nombre affaires produites par type
  Couleur: palette produit (BP, B6, B8, GP...)

- AFF_CHART_EVOLUTION (GRP_AFF_SEC2) x=845 y=356 w=590 h=240
  Type: lineChart mensuel
  Val: Volume affaires produites + Volume affaires commissionnées (2 séries)
  Légende: Produites (BP), Commissionnées (B6)

**TABLEAU (GRP_AFF_TABLE) y=610 x=235 w=1190 h=275 :**
- AFF_TBL_DETAIL colonnes:
  Agence | RTC | Mandataires | Centre d'affaires | Affaires produites | Budget | 
  Réalisé à % | Budget moyen | Moyen réalisé | Affaires commis. | Affaires inst. | 
  Rétrocommissions
- Mise en forme cond. sur "Réalisé à %" : vert ≥100%, orange 80-100%, rouge <80%
- Ligne totale en bas avec fond B8


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_AFF_KPI
▼ GRP_AFF_KPI2
▼ GRP_AFF_SEC1
▼ GRP_AFF_SEC2
▼ GRP_AFF_TABLE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.RES — PAGE RÉSEAU MIA

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ 5 KPI tiles présents (MIA actifs, actifs productifs, oriasés, non productifs, rétro)

□ Carte France présente avec bulles agences

□ Graphique répartition MIA par CSP (barres)

□ Graphique MIA productifs par agence (barres)

□ Tableau détail MIA avec colonnes agence/RTC/mandataires...

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "RESEAU_MIA" dans maquette_b64.json

**KPI TILES (y=80, 5 tiles w=222 h=110) :**
- RES_KPI1 : "NOMBRE DE MIA ACTIFS" | Nombre mandataires actifs | #,##0 "K"
  Variation vs N-1
- RES_KPI2 : "MIA ACTIFS PRODUCTIFS" | Nombre mandataires productifs | #,##0
  Pourcentage: Taux mandataires actifs
- RES_KPI3 : "MIA ORIASÉS" | Nombre MIA oriasés | #,##0
- RES_KPI4 : "MIA NON PRODUCTIFS" | Nombre mandataires non productifs | #,##0
  Couleur rouge si ratio élevé
- RES_KPI5 : "MONTANT RÉTROCOMMISSIONS" | Montant rétrocommission | #,##0 "K€"

**CARTE FRANCE (GRP_RES_MAP) x=235 y=210 w=420 h=380 :**
- RES_MAP_FRANCE : visuel carte (ArcGIS Maps ou Shape Map)
  Localisation: dim_agence[region/code_postal]
  Taille bulle: Nombre mandataires actifs
  Couleur bulle: dégradé BP → B6 selon densité
  Titre: "RÉPARTITION DES MANDATAIRES PAR AGENCE"
  ⚠ Si ArcGIS non disponible, utiliser un clusteredColumnChart par région

**GRAPHIQUES DROITE :**
- RES_CHART_CSP (GRP_RES_SEC1) x=680 y=210 w=360 h=180
  Type: barChart horizontal
  Cat: dim_candidat[niveau_etude] ou CSP, Val: Nombre mandataires actifs
  Titre: "RÉPARTITION DES MIA PAR CSP"

- RES_CHART_PRODUCTIFS_AGENCE (GRP_RES_SEC2) x=1060 y=210 w=365 h=380
  Type: clusteredColumnChart
  Cat: dim_agence, Val: Nombre mandataires productifs
  Titre: "NOMBRE DE MIA PRODUCTIFS PAR AGENCE"
  Couleur: BP, étiquettes valeurs

**TABLEAU (GRP_RES_TABLE) y=610 x=235 w=1190 h=275 :**
- RES_TBL_MIA colonnes:
  Agence | Actives | Unités | Mandataires | Actifs/Non | Productifs | 
  Montant production | Montant rétro | Montant de rémunération | Taux
- Total bas: fond B8 White Bold


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_RES_KPI
▼ GRP_RES_MAP
▼ GRP_RES_SEC1
▼ GRP_RES_SEC2
▼ GRP_RES_TABLE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.RDV — PAGE RENDEZ-VOUS

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ 4 KPI tiles : RDV prévus, réalisés, taux réalisation, domicile

□ Donut 'répartition par type' présent

□ Barres mensuelles RDV réalisés présent

□ Tableau total RDV par agence présent

□ Encadré bas droite avec taux réalisation grand format + recommandation

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "RDV" dans maquette_b64.json

**KPI TILES (y=80, 4 tiles w=285 h=130) :**
- RDV_KPI1 : "NOMBRE RENDEZ-VOUS PRÉVUS" | Nombre rendez-vous prévus | #,##0 "K"
  Variation vs N-1
- RDV_KPI2 : "NOMBRE RENDEZ-VOUS RÉALISÉS" | Nombre rendez-vous réalisés | #,##0 "K"
  Variation vs N-1
- RDV_KPI3 : "TAUX DE RÉALISATION" | Taux réalisation de rendez-vous | 0.0%
  Grand format 28pt BP, icône jauge
  Mise en forme cond.: fond vert si ≥62%, orange si 40-62%, rouge si <40%
- RDV_KPI4 : "RDV À DOMICILE" | Nombre rendez-vous réalisés à domicile | #,##0 "K"
  Taux: Taux rendez-vous faits à domicile en sous-label

**DONUT (GRP_RDV_DONUT) x=235 y=230 w=380 h=280 :**
- RDV_DONUT_TYPE : donut chart
  Cat: dim_type_rendez_vous_client[type], Val: Nombre rendez-vous réalisés
  Palette: BP, B6, B8, GS, GP
  Légende intégrée dans la zone
  Centre du donut: Total réalisés (valeur + label)
  Titre: "RÉPARTITION DES RDV RÉALISÉS PAR TYPE"

**BARRES MENSUELLES (GRP_RDV_SEC1) x=640 y=230 w=780 h=280 :**
- RDV_CHART_MOIS : clusteredColumnChart ou groupedBar
  Cat: dim_date[mois_annee], Val: Nombre rendez-vous réalisés + Nombre rendez-vous prévus
  Couleur réalisés: BP, couleur prévus: B2 contour BP
  Titre: "NOMBRE DES RENDEZ-VOUS RÉALISÉS PAR MOIS"

**TABLEAU (GRP_RDV_TABLE) y=530 x=235 w=840 h=355 :**
- RDV_TBL_AGENCE : table matricielle
  Lignes: dim_agence, Colonnes: dim_type_rendez_vous_client
  Valeur: Nombre RDV réalisés + Total
  En-tête BP White, alternance B2/White

**ENCADRÉ DROITE (GRP_RDV_ENCADRE) x=1095 y=530 w=325 h=355 :**
- RDV_ENCADRE_BG : shape fond GS #F6F7FB bordure GR
- RDV_ENCADRE_TITLE : "TAUX DE RÉALISATION RDV" 10pt SemiBold BP
- RDV_CARD_TAUX : card 40pt Bold couleur cond. (vert/orange/rouge)
  Mesure: Taux réalisation de rendez-vous
- RDV_CARD_RECO : card ou textbox recommandation
  Mesure: Recommandation Alerte RDV
- RDV_ENCADRE_SEUIL : textbox "SEUIL : 62,0%" 10pt TM


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_RDV_KPI
▼ GRP_RDV_DONUT
▼ GRP_RDV_SEC1
▼ GRP_RDV_TABLE
▼ GRP_RDV_ENCADRE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.MAN — PAGE MANDATAIRES

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ KPI row 1 : 4 tiles (Mandataires, actifs, productifs, non productifs) avec icônes personnes

□ KPI row 2 : 4 tiles (taux actifs %, non productifs, montant production, montant rétro)

□ Tableau hiérarchique Agence > RTC > Mandataires avec colonnes détaillées

□ Icônes personne sur les KPI tiles (SVG ou Unicode)

□ Légende 'En affaires toutes France' en bas droite

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "MANDATAIRES" dans maquette_b64.json

**KPI ROW 1 (y=80, 4 tiles w=285 h=110) — effectifs avec icônes :**
- MAN_KPI1 : "MANDATAIRES" | Nombre mandataires actifs | #,##0
  Icône personne BP, variation vs N-1 (↑/↓)
- MAN_KPI2 : "MANDATAIRES ACTIFS" | Nombre mandataires actifs | #,##0
  Sous-label: Taux mandataires actifs en %
  Icône personne GP vert
- MAN_KPI3 : "MANDATAIRES PRODUCTIFS" | Nombre mandataires productifs | #,##0
  Icône personne B8
  Sous-label: % sur total
- MAN_KPI4 : "MANDATAIRES NON PRODUCTIFS" | Nombre mandataires non productifs | #,##0
  Icône personne RN rouge
  Sous-label: % sur total

**KPI ROW 2 (y=205, 4 tiles w=285 h=110) — métriques :**
- MAN_KPI5 : "TAUX MANDATAIRES ACTIFS" | Taux mandataires actifs | 0.0%
  Couleur conditionnelle fond tile
- MAN_KPI6 : "MANDATAIRES NON PRODUCTIFS" | Nombre mandataires non productifs | #,##0
  Doublé avec variation
- MAN_KPI7 : "MONTANT DE LA PRODUCTION" | Volume affaires produites | #,##0.00 "M€"
  Budget en sous-label
- MAN_KPI8 : "MONTANT RÉTROCOMMISSIONS" | Montant rétrocommission | #,##0.00 "M€"
  Budget en sous-label

**TABLEAU HIÉRARCHIQUE (GRP_MAN_TABLE) y=335 x=235 w=1190 h=550 :**
- MAN_TBL_DETAIL : table avec expansion hiérarchique Agence > RTC > Mandataires
  Colonnes:
  Agence | RTC | Mandataires | Actifs (nb/%) | Productifs (nb/%) |
  Montant production | Montant de la rétro commission | Indicateurs relatifs 
  (Montant / taux) | Directeur
  
- En-tête: BP White SemiBold 9pt
- Alternance lignes: White / B2
- Lignes totaux agence: fond B8 White Bold
- Mise en forme cond. sur % actifs: vert ≥80%, orange 60-80%, rouge <60%
- Colonne "Actifs" : icônes vert/rouge selon seuil
- Note bas: "En affaires toutes France" en italique TL

**FILTRE DIRECTION (en-tête droite) :**
- MAN_SLC_DIRECTION : slicer "Direction commerciale" x=1100 y=3 w=200 h=30
  Style chip horizontal, fond B2


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_MAN_KPI
▼ GRP_MAN_KPI2
▼ GRP_MAN_TABLE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.ALT — PAGE ALERTES

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ 6 KPI tiles : Alertes actives, critiques, hautes, moyennes, opportunités, total ouvertes

□ Icônes d'alerte colorées sur les KPI (rouge, orange, jaune, vert)

□ Tableau actionnable des alertes avec 8+ colonnes

□ Panneau droite 'Logique d'action et différencier' avec 5 boutons d'action

□ Mise en forme cond. tableau : rouge=critique, orange=haute, jaune=moyenne

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "ALERTES" dans maquette_b64.json

**KPI TILES (y=80, 6 tiles w=190 h=120) avec icônes colorées :**
- ALT_KPI1 : "ALERTES ACTIVES" | Nombre Alertes Ouvertes | #,##0
  Icône: ⚠ rouge | Sous-label: variation
- ALT_KPI2 : "ALERTES CRITIQUES" | Nombre Alertes Critiques | #,##0
  Tile fond RN #F05062 light, icône 🔴
  Sous-label: variation %
- ALT_KPI3 : "ALERTES HAUTES" | Nombre Alertes Hautes | #,##0
  Icône 🟠 orange
- ALT_KPI4 : "ALERTES MOYENNES" | Nombre Alertes Moyennes | #,##0
  Icône 🟡 jaune
- ALT_KPI5 : "OPPORTUNITÉS" | À définir (mesure fact_alertes type=Opportunité) | #,##0
  Icône 🟢 vert GP
- ALT_KPI6 : "TOTAL ALERTES OUVERTES" | Nombre Alertes Ouvertes | #,##0
  Tile fond BP White — valeur grand format 28pt

**TABLEAU ACTIONNABLE (GRP_ALT_TABLE) x=235 y=225 w=870 h=660 :**
- ALT_TBL_ALERTES : table fact_alertes
  Colonnes: Agent | Centre d'affaires | Mandataires | Domaine |
  Recommandation | Statut alertes | 3 mois | 6 mois | 12 mois | Opportunité
  
- Mise en forme cond. sur colonne "Statut alertes" :
  🔴 Alerte critique → fond RN light
  🟠 Alerte haute → fond orange light  
  🟡 Alerte moyenne → fond jaune light
  🟢 Opportunité → fond vert light
- Boutons filtre au-dessus du tableau: TOUT | CRITIQUE | HAUTE | MOYENNE

**PANNEAU ACTIONS DROITE (GRP_ALT_ACTIONS) x=1120 y=225 w=305 h=660 :**
- ALT_PANEL_BG : shape fond GS #F6F7FB bordure GR
- ALT_PANEL_TITLE : "LOGIQUE D'ACTION ET DIFFÉRENCIER" 10pt SemiBold BP
- 5 boutons d'action avec icônes:
  ALT_BTN_AUTOMATE : "Power Automate" icône ⚡ fond B2 text BP
  ALT_BTN_EMAIL    : "Messagerie e-mail" icône 📧
  ALT_BTN_EXPORT   : "Export du table" icône 📥
  ALT_BTN_MODIF    : "Modification figée" icône 📌
  ALT_BTN_AUTRES   : "Autres options" icône ⋯
- Chaque bouton: h=60 w=285 bordure GR radius=6 fond White hover B2


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_ALT_KPI
▼ GRP_ALT_TABLE
▼ GRP_ALT_ACTIONS
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
## PROMPT 3.GLO — PAGE GLOSSAIRE

### ✅ CHECKLIST VALIDATION AVANT LIVRAISON
```

□ Compteur KPI documentés (12+) visible en haut droite

□ Compteur KPI présents (2+) visible

□ Tableau avec 6 colonnes : Indicateur, Définition, Règle de calcul, Comment l'utiliser, Disponible, Commentaires

□ Colonne 'Disponible' avec badge couleur (vert=disponible, rouge=non disponible)

□ Mini badges icônes en haut droite (🖨 📋)

□ 0 visuel sans nom dans le volet Sélection
□ Tous les visuels dans un GRP_* correspondant
□ Header et sidebar identiques aux autres pages
□ Aucun visuel hors canvas (x+w≤1440, y+h≤900)
□ Aucun visuel superposé involontairement
□ Rendu visuel comparé pixel à pixel avec l'image de maquette
```


**IMAGE MAQUETTE :** Voir base64 key "GLOSSAIRE" dans maquette_b64.json

**COMPTEURS HAUT DROITE :**
- GLO_KPI_COMPTE : card compteur "12 KPI documentés" | Nombre lignes glossaire
  x=1200 y=10 w=140 h=45 | format: #,##0 | 14pt Bold BP
- GLO_KPI_PRESENTS : card compteur "2 en attente" 
  x=1350 y=10 w=80 h=45 | 12pt BP
- GLO_BTN_PRINT : button "🖨" icône x=1390 y=8 w=30 h=30 fond GS
- GLO_BTN_COPY  : button "📋" icône x=1425 y=8 w=30 h=30 fond GS

**TABLEAU GLOSSAIRE (GRP_GLO_TABLE) x=235 y=85 w=1190 h=800 :**
- GLO_TBL_INDICATEURS : table glossaire_indicateurs
  Colonnes avec largeurs:
  Indicateur (200px) | Définition (280px) | Règle de calcul (200px) | 
  Comment l'utiliser (180px) | Disponible (100px) | Commentaires (230px)

- En-tête: fond BP White SemiBold 9pt, hauteur 36px
- Corps: taille 9pt Regular, hauteur ligne 40px, wrap text activé
- Alternance lignes: White / B2 #E6EBFA
- Colonne "Disponible":
  Valeur "Disponible" → badge fond GP light #D1FAE5, texte GP #00B050 Bold
  Valeur "Non disponible" → badge fond RN light, texte RN
  Valeur "Partielle" → badge fond orange light
- Séparateur vertical léger GR entre colonnes
- Barre de recherche/filtre au-dessus du tableau (slicer texte sur indicateur)


### GROUPES ET HIÉRARCHIE VOLET SÉLECTION

```
▼ GRP_GLO_KPI
▼ GRP_GLO_TABLE
▼ GRP_HDR
▼ GRP_NAV
CONTENT_BG (non groupé)
```


---
# PHASE 4 — MISE EN FORME CONDITIONNELLE GLOBALE

## ✅ CHECKLIST DE VALIDATION
```
□ Toutes les variations positives s'affichent en vert #00B050
□ Toutes les variations négatives s'affichent en rouge #F05062
□ Les taux de budget <80% sont rouges, 80-100% orange, ≥100% verts
□ Le taux de réalisation RDV applique la règle des 62%
□ Les niveaux d'alerte ont leur couleur respective dans les tableaux
□ Les couleurs conditionnelles fonctionnent avec les filtres slicers
□ Pas de #N/A ou [Blank] visible dans les visuels avec données fictives
```

## PROMPT 4 — IMPLÉMENTATION DES RÈGLES DE COULEUR

### Mesures DAX de mise en forme conditionnelle (à créer dans _Indicateurs) :

```dax
// ── VARIATIONS ──────────────────────────────────────────────────────────
CF Couleur Variation Volume = 
    IF([Variation vs N-1 Volume Affaires (%)] > 0, "#00B050",
       IF([Variation vs N-1 Volume Affaires (%)] < 0, "#F05062", "#374151"))

CF Couleur Variation Générale [val] = 
    IF([val] > 0, "#00B050", IF([val] < 0, "#F05062", "#374151"))

// ── TAUX BUDGET ──────────────────────────────────────────────────────────
CF Couleur Taux Budget = 
    IF([Taux atteinte Budget N Volume] >= 1, "#00B050",
       IF([Taux atteinte Budget N Volume] >= 0.8, "#F59E0B", "#F05062"))

CF Fond Tile Taux Budget = 
    IF([Taux atteinte Budget N Volume] >= 1, "#D1FAE5",
       IF([Taux atteinte Budget N Volume] >= 0.8, "#FEF3C7", "#FEE2E2"))

// ── TAUX RDV ──────────────────────────────────────────────────────────────
CF Couleur Taux RDV = 
    IF([Taux réalisation de rendez-vous] >= 0.62, "#00B050",
       IF([Taux réalisation de rendez-vous] >= 0.40, "#F59E0B", "#F05062"))

CF Fond Tile Taux RDV = 
    IF([Taux réalisation de rendez-vous] >= 0.62, "#D1FAE5",
       IF([Taux réalisation de rendez-vous] >= 0.40, "#FEF3C7", "#FEE2E2"))

// ── ALERTES ────────────────────────────────────────────────────────────────
CF Couleur Alerte Ligne = 
    SWITCH(SELECTEDVALUE(fact_alertes[niveau_alerte]),
        "Critique",   "#FEE2E2",
        "Haute",      "#FEF3C7",
        "Moyenne",    "#FEFCE8",
        "Opportunité","#D1FAE5",
        "#FFFFFF")

// ── MANDATAIRES ────────────────────────────────────────────────────────────
CF Couleur Taux Actifs = 
    IF([Taux mandataires actifs] >= 0.80, "#00B050",
       IF([Taux mandataires actifs] >= 0.60, "#F59E0B", "#F05062"))
```

### Application dans les visuels :
Pour chaque card/visual utilisant une couleur conditionnelle :
1. Format → Éléments visuels → Couleur de données → Mise en forme conditionnelle
2. Sélectionner "Valeur de champ" → choisir la mesure CF correspondante
3. Vérifier le rendu avec les données fictives du BIM

---


---
# PHASE 5 — VALIDATION GLOBALE ET LIVRAISON

## ✅ CHECKLIST FINALE OBLIGATOIRE AVANT LIVRAISON
```
STRUCTURE
□ 8 pages présentes : Accueil, Performance, Affaires, Réseau MIA,
  Rendez-vous, Mandataires, Alertes, Glossaire
□ Canvas 1440×900 sur toutes les pages
□ Volet Sélection : 0 visuel sans nom sur chaque page
□ Volet Sélection : hiérarchie GRP_* complète sur chaque page

DONNÉES & MESURES
□ 0 mesure affiche [Erreur] ou #N/A
□ 0 KPI inventé — tout mappé dans MAPPING_KPI_FINAL.csv
□ Filtres slicers fonctionnels (testés avec 2-3 valeurs différentes)
□ Les mesures de variation s'affichent correctement (+/-)

DESIGN
□ Couleurs respectent la palette Capfinances (BP #051E73, RN #F05062, GP #00B050)
□ Police Segoe UI sur tous les éléments texte
□ Sidebar identique sur les 8 pages
□ Header identique sur les 8 pages (6 slicers + bouton)
□ KPI tiles avec barre accent gauche 6px BP
□ Tableaux : en-tête BP, alternance White/B2

MISE EN FORME CONDITIONNELLE
□ Variations positives = vert #00B050
□ Variations négatives = rouge #F05062
□ Taux budget : vert ≥100%, orange 80-100%, rouge <80%
□ Taux RDV : vert ≥62%, orange 40-62%, rouge <40%
□ Alertes : rouge critique, orange haute, jaune moyen, vert opportunité

GROUPEMENT
□ 0 visuel orphelin (sans parentGroupName, hors CONTENT_BG)
□ Groupes nommés selon convention GRP_{PAGE}_{ZONE}
□ CONTENT_BG seul non groupé sur chaque page

QUALITÉ BIG FOUR
□ Rendu comparé aux 8 images de maquette — ressemblance ≥ 90%
□ Pas de texte tronqué visible
□ Pas de visuel se chevauchant involontairement
□ Titres en MAJUSCULES dans les visuels
□ Valeurs KPI lisibles (pas trop petites)
□ Espacement cohérent entre les éléments (padding 15px minimum)
```

## PROMPT 5 — VALIDATION ET PACKAGING

**TÂCHE :**
1. Parcourir les 8 pages et cocher chaque item de la checklist finale
2. Corriger tout écart identifié
3. Prendre des screenshots de chaque page et comparer avec les images base64 de référence
4. Créer le ZIP final :
```
PC_LOCAL_FINAL.zip/
├── PCL/
│   ├── Pilotage_Commercial.pbip
│   ├── Pilotage_Commercial.Report/
│   │   ├── report.json
│   │   ├── definition.pbir
│   │   └── definition.pbireport
│   ├── Pilotage_Commercial.SemanticModel/
│   │   ├── model.bim        (NB: pas model_local.bim)
│   │   └── definition.pbism
│   └── VALIDATION/
│       ├── MAPPING_KPI_FINAL.csv
│       ├── AUDIT_ECART_MAQUETTE.md
│       ├── CHECKLIST_FINALE.md
│       └── SCREENSHOTS/
│           ├── ACCUEIL.png
│           ├── PERFORMANCE.png
│           ├── AFFAIRES.png
│           ├── RESEAU_MIA.png
│           ├── RDV.png
│           ├── MANDATAIRES.png
│           ├── ALERTES.png
│           └── GLOSSAIRE.png
```

5. Vérifier que le ZIP s'ouvre et que le PBIP charge sans erreur dans Power BI Desktop

---

# ANNEXE — RÈGLES DE DÉVELOPPEMENT POWER BI

## A1. Format report.json — Structure d'un visualContainer

```json
{
  "x": 235, "y": 80, "z": 10, "width": 285, "height": 130,
  "config": "{
    \"name\": \"PERF_KPI1_BG\",
    \"layouts\": [{\"id\": 0, \"position\": {
      \"x\": 235, \"y\": 80, \"z\": 10,
      \"width\": 285, \"height\": 130, \"tabOrder\": 10
    }}],
    \"singleVisual\": {
      \"visualType\": \"shape\",
      \"projections\": {},
      \"prototypeQuery\": {},
      \"objects\": {
        \"general\": [{\"properties\": {\"fill\": {\"solid\": {\"color\": {\"expr\": {
          \"Literal\": {\"Value\": \"'#FFFFFF'\"}
        }}}}}}]
      }
    },
    \"parentGroupName\": \"GRP_PERF_KPI\"
  }",
  "filters": "[]"
}
```

## A2. Structure d'un groupe (singleVisualGroup)

```json
{
  "x": 235, "y": 80, "z": 9, "width": 1190, "height": 130,
  "config": "{
    \"name\": \"GRP_PERF_KPI\",
    \"layouts\": [{\"id\": 0, \"position\": {
      \"x\": 235, \"y\": 80, \"z\": 9,
      \"width\": 1190, \"height\": 130, \"tabOrder\": 9
    }}],
    \"singleVisualGroup\": {}
  }",
  "filters": "[]"
}
```

## A3. Navigation entre pages (actionButton)

```json
"singleVisual": {
  "visualType": "actionButton",
  "objects": {
    "action": [{
      "properties": {
        "actionType": {"expr": {"Literal": {"Value": "'PAGE_NAVIGATION'"}}},
        "navigationSection": {
          "expr": {"Section": {"SourceRef": {"Section": "ReportSectionPERF"}}}
        }
      }
    }]
  }
}
```

## A4. IDs des pages

| Page | ID Section |
|------|------------|
| Accueil | ReportSectionACC |
| Performance | ReportSectionPERF |
| Affaires | ReportSectionAFF |
| Réseau MIA | ReportSectionRES |
| Rendez-vous | ReportSectionRDV |
| Mandataires | ReportSectionMAN |
| Alertes | ReportSectionALT |
| Glossaire | ReportSectionGLO |

## A5. Types de visuels Power BI valides

| Type JSON | Visuel affiché |
|-----------|---------------|
| `card` | Carte KPI (valeur unique) |
| `shape` | Forme/rectangle |
| `textbox` | Zone de texte |
| `actionButton` | Bouton avec action |
| `slicer` | Segment/filtre |
| `barChart` | Barres verticales |
| `clusteredBarChart` | Barres horizontales groupées |
| `lineChart` | Courbe |
| `donutChart` | Anneau |
| `pieChart` | Camembert |
| `clusteredColumnChart` | Colonnes groupées |
| `tableEx` | Tableau |
| `matrix` | Matrice |
| `map` ou `arcGisMap` | Carte géographique |
| `filledMap` | Carte choroplèthe |

---
*Document généré le 2026-06-06 — Capfinances Pilotage Commercial COMEX*
*Référence: PC_LOCAL_v6.zip | Charte: Capfinances_charte_V1.pdf*
