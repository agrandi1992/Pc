# Reconstruction V5 — conformité visuelle maquettes

Objectif : remplacer la baseline technique ouvrable par une reconstruction visuelle proche des maquettes Capfinances/Groupe Premium.

Travaux appliqués :

- Reconstruction complète des 8 pages en PBIR enhanced.
- Suppression des anciens visuels non conformes.
- Template commun : menu gauche Premium Blue, header, sous-titre, bouton SÉLECTIONS, rangée de filtres.
- Recréation des KPI cards blanches avec valeur dynamique Power BI, barre de progression et libellé de budget/source.
- Recréation des blocs graphiques : line chart, bar chart, clustered column chart, donut chart et tables dynamiques.
- Page Alertes reconstruite avec cards de priorisation, table actionnable et panneau logique d'envoi / diffusion.
- Page Glossaire enrichie avec définition, règle de calcul, lecture, disponibilité et commentaire.
- Mise en forme alignée charte : #051E73, #3C41BE, #8096FF, #E6EBFA, #F05062, #FFF4F2, #F6F7FB.

Limites connues :

- Certains filtres absents du modèle sémantique (Assureur, Centre d'affaires, Client/Prospect) sont affichés en placeholders propres pour éviter un KPI ou champ inventé.
- La carte géographique est reproduite en panneau visuel statique car le modèle local ne contient pas de table géographique complète agence/coordonnées.
- Validation Power BI Desktop native à exécuter côté poste utilisateur.
