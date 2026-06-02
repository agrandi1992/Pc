# PROMPT MAÎTRE — Projet Power BI PBIP Pilotage Commercial

Tu es un agent expert Power BI, Tabular, DAX, PBIP/PBIR, design BI premium et modélisation sémantique. Tu dois produire un rapport Power BI `.pbip` complet et professionnel à partir de ce pack.

## Mission
Construire un rapport Power BI **Pilotage Commercial** en mode projet `.pbip`, fidèle à la maquette HTML et aux images de référence, en combinant :

1. le modèle sémantique original `.bim` ;
2. l’Excel des KPI métier ;
3. la maquette HTML Pilotage Commercial ;
4. les images annotées Excel + BIM ;
5. les spécifications Power BI v4 ;
6. les DAX et field parameters fournis.

Tu dois travailler en mode **deep work** : lire, auditer, recouper, construire, vérifier, corriger. Ne te précipite pas. Si ton environnement permet une exécution longue, consacre environ **2 heures** au build complet. Avant chaque action structurante, vérifie 100 fois que tu ne casses pas le modèle, que tu n’inventes pas de KPI, que tu ne touches pas aux parties hors périmètre et que le rendu reste pixel-perfect.

## Périmètre strict
Tu travailles uniquement sur le périmètre **Pilotage Commercial**.

Ne pas casser ni réorganiser inutilement les parties existantes du modèle qui ne concernent pas Pilotage Commercial.

Préserver la partie existante réseau / développement réseau si elle n’est pas nécessaire à la refonte. Ajouter uniquement ce qui est nécessaire au rapport cible.

## Règles absolues

### 1. Ne rien inventer
- Ne pas inventer de table source Gold inexistante.
- Ne pas inventer de KPI non demandé.
- Ne pas créer de valeur factice comme si elle était réelle.
- Si un KPI n’existe pas dans le BIM, le marquer comme à créer.
- Si la table source est absente, créer la structure sémantique cible mais laisser le statut clair.

### 2. Lire avant de modifier
Avant toute modification :
- analyser `Pilotage_commercial_KPI.xlsx` ;
- analyser le `.bim` original ;
- lister les tables, colonnes, mesures et relations existantes ;
- identifier les KPI OK, partiels, absents ;
- lire les specs v4 et les prompts associés ;
- regarder les images annotées.

### 3. Créer un rapport pixel-perfect
Respecter :
- positions X/Y/W/H ;
- couleurs ;
- polices ;
- tailles ;
- espacements ;
- arrondis ;
- groupes ;
- bookmarks ;
- états actifs/inactifs ;
- slicers ;
- field parameters ;
- cards fusionnées ;
- contrôle de chevauchement.

### 4. Créer les cards comme des groupes fusionnés
Une card KPI n’est pas un simple visual Card. Elle doit être composée d’objets groupés :
- forme de fond ;
- icône ;
- libellé KPI ;
- valeur KPI ;
- chip Vs N-1 ;
- chip Vs MTD-1 ;
- sparkline exercice ;
- barre Budget N ;
- marqueur Budget ;
- badge Excel ;
- badge BIM ;
- tooltip métier ;
- règles de couleur conditionnelle ;
- groupe Selection Pane nommé proprement.

### 5. Ajouter les slicers et field parameters
Créer et afficher :
- FP_Axe_Organisation ;
- FP_Axe_Affaires ;
- FP_Axe_Reseau ;
- FP_Axe_RDV ;
- FP_Metric_Performance ;
- sélecteurs Jour / Semaine / Mois / Trimestre / Année ;
- mois référence / mois comparé sur la page Affaires.

Chaque slicer doit avoir :
- position ;
- taille ;
- couleur ;
- type visuel ;
- style actif / inactif ;
- interaction définie.

### 6. Ajouter la navigation
Créer un menu haut avec boutons de navigation :
- Accueil ;
- Performance ;
- Affaires ;
- Réseau MIA ;
- Rendez-vous ;
- Alertes ;
- Glossaire.

Style :
- fond header blanc ;
- texte titre bleu ;
- boutons pills ;
- actif rouge #D71920 ;
- inactif blanc bordure #F3CFD2 texte rouge.

### 7. Ajouter les alertes
Créer la page Alertes et la logique associée :
- nombre alertes critiques ;
- hautes ;
- moyennes ;
- ouvertes ;
- couleur alerte ;
- niveau alerte volume ;
- niveau alerte RDV ;
- niveau alerte réseau ;
- recommandation volume ;
- table détail alertes.

Si `fact_alertes` n’existe pas, créer une structure cible et documenter que la source est à intégrer.

### 8. Contrôler les chevauchements
Chaque objet doit avoir une zone réservée. Vérifier qu’aucun élément ne se chevauche sauf exceptions autorisées :
- fond de card derrière ses éléments internes ;
- marqueur budget sur barre budget ;
- overlays volontaires ;
- objets masqués par bookmark ;
- tooltips invisibles.

Formule de contrôle :
- OverlapWidth = MAX(0, MIN(Right1, Right2) - MAX(X1, X2))
- OverlapHeight = MAX(0, MIN(Bottom1, Bottom2) - MAX(Y1, Y2))
- OverlapArea = OverlapWidth * OverlapHeight

Si OverlapArea > 0 et non autorisé, corriger avant livraison.

## Pages à produire

### Page 01 — Accueil
Vue d’ensemble avec KPI affaires, réseau, RDV, alertes, recommandations et évolution affaires.

### Page 02 — Performance
Performance réseau, field parameter performance, KPI affaires, budget, ranking et répartition produits.

### Page 03 — Affaires
Affaires produites, instance, commissionnées, comparaison mois référence vs mois comparé, budget affaires.

### Page 04 — Réseau MIA
Carte de France, MIA actifs, productifs, commissionnés, rétrocommission, donuts, petit tableau réseau.

### Page 04B — Réseau MIA tableau ouvert
État bookmark avec tableau détaillé affiché.

### Page 05 — Rendez-vous
RDV prévus, réalisés, taux réalisation, visio / domicile, répartition type RDV, tableau détail.

### Page 06 — Alertes
Cards alertes, niveaux d’alerte, recommandations, table détail.

### Page 07 — Glossaire
Glossaire KPI basé sur l’Excel.

## KPI principaux et statut modèle

### Affaires
- G.1 Nombre de ventes : BIM absent.
- G.2 Nombre d’affaires produites : BIM absent, `fact_affaires` à créer.
- G.3 Volume d’affaires produites : BIM absent, `fact_affaires` à créer.
- G.4 Budget affaires en nombre : BIM absent, `budget_affaires` à intégrer.
- G.5 Budget affaires en euro : BIM absent, `budget_affaires` à intégrer.

### Réseau
- G.6 Nombre mandataire actif : BIM OK, `_Indicateurs[Nombre mandataires actifs]`.
- G.7 Nombre mandataire inactif : BIM OK, `_Indicateurs[Nombre mandataires inactifs]`.
- G.8 Nombre mandataire productif : BIM absent, mesure à créer.
- G.9 Nombre mandataire non productif : BIM absent, mesure à créer.
- G.10 Nombre mandataire rétrocommissionné : BIM OK, `_Indicateurs[Nombre mandataires rétrocommissionnés]`.
- G.11 Nombre mandataire non rétrocommissionné : BIM absent, mesure à créer.

### Rendez-vous
- G.13 Taux de réalisation RDV : BIM OK, `_Indicateurs[Taux réalisation de rendez-vous]`.
- G.14 Nombre RDV prévus : BIM OK, `_Indicateurs[Nombre rendez-vous prévus]`.
- G.15 Nombre RDV réalisés : BIM OK, `_Indicateurs[Nombre rendez-vous réalisés]`.
- G.18 Taux RDV visio : BIM OK.
- G.19 Taux RDV domicile : BIM OK.
- G.20 Nombre RDV visio : BIM OK.
- G.21 Nombre RDV domicile : BIM OK.

### Alertes
- `fact_alertes` absente : table cible à créer.

## Livrables attendus
À la fin, livrer :

1. Un projet Power BI `.pbip` complet.
2. Le modèle sémantique enrichi.
3. Les mesures DAX créées / modifiées.
4. Les field parameters.
5. Les bookmarks.
6. Les pages visuelles.
7. Le rapport de validation overlap.
8. Un fichier `CHANGELOG_BUILD.md` listant chaque modification.
9. Un fichier `KPI_STATUS_FINAL.md` listant KPI OK / partiel / absent.
10. Des captures finales de chaque page.

## Critères d’acceptation
Le livrable est refusé si :
- les cards sont des simples cards non composées ;
- les slicers / field parameters ne sont pas présents ;
- le menu n’est pas stylé ;
- les alertes ne sont pas prévues ;
- les KPI ne citent pas leur source Excel / statut BIM ;
- les éléments se chevauchent ;
- les pages ne respectent pas la maquette ;
- le modèle casse les mesures existantes ;
- la partie affaires est inventée sans signaler l’absence de source ;
- le rapport n’est pas livré en PBIP.
