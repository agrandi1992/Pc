# reconstruction visuelle V5 — conformité maquette

## Objectif V5
Porter la V4 de pré-recette visuelle vers une version plus proche du rendu maquette : canvas 1536x961, filtres non-statiques quand le modèle le permet, tables plus premium, renforcement des pages Réseau MIA / Alertes / Glossaire / Mandataires.

## Corrections V5
- Canvas passé à 1536 x 961 pour coller au format des maquettes fournies.
- Recalage proportionnel de tous les visuels V4 sur le nouveau canvas.
- Ajout de slicers réels V5 sur les filtres auparavant placeholders : assureur, centre d'affaires, ancienneté, client/prospect, présentiel/visio.
- Ajout au modèle de tables/colonnes support pour ces filtres : `dim_assureur_v5`, `dim_centre_affaires_v5`, `dim_client_prospect_v5`, `anciennete_mandataire_v5`, `rdv_modalite_v5`.
- Renforcement du style des tables : en-têtes bleu profond, lignes bandées, grilles plus légères.
- Renforcement de la page Réseau MIA : légende carte et indication géographique.
- Renforcement de la page Alertes : séparateurs du panneau workflow et rappel recalcul nocturne.
- Renforcement de la page Glossaire : compteurs KPI documentés / KPI en attente.
- Renforcement de la page Mandataires : profil utilisateur Direction.

## Limites restantes
- La carte Réseau MIA reste une carte stylisée en PBIR, pas une validation Power BI Desktop d'une carte native avec géocodage.
- Le pixel-perfect final doit être contrôlé dans Power BI Desktop.
- Certains filtres V5 sont déconnectés si la donnée source n'existe pas encore dans la couche Gold ; ils ne sont plus statiques visuellement mais devront être reliés au modèle cible lors de l'intégration Fabric.

## Validation fichier
- Génération : 2026-06-07T12:40:42
- Contrôle JSON : à la génération du zip.
