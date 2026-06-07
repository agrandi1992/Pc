# reconstruction visuelle V5 — conformité maquette

## Objectif V5
Transformer la V3 en version plus proche des maquettes Capfinances : rendu premium, ombres, cartes plus lisibles, map réseau MIA en fallback visuel, waterfall budget, badges d’alertes, bloc finance/prod plus clair.

## Corrections apportées
- Ajout d’ombres légères sur les cards et panels.
- Renforcement du menu latéral et des logos.
- Page performance : remplacement du graphique budget brut par un waterfall stylisé proche maquette.
- Page réseau MIA : ajout d’une carte France stylisée avec bulles agences et valeurs, plus barres CSP lisibles.
- Page rendez-vous : ajout d’un header de matrice R1/R2 et bloc “À retenir”.
- Page alertes : ajout de badges d’état et amélioration du panneau workflow/diffusion.
- Page glossaire : ajout des badges disponibilité.
- Page affaires : ajout du bloc de période de comparaison et de l’encart “En attente travaux prod”.
- Modèle : ajout de colonnes calculées latitude/longitude agence pour permettre une vraie carte native ultérieure si Desktop le permet.

## Limite assumée
Le rendu a été contrôlé structurellement côté fichiers PBIR/JSON. L’ouverture Power BI Desktop et l’ajustement pixel-perfect final doivent être validés sur poste Windows.
