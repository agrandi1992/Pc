# Checklist 100 contrôles — avant et après build PBIP

## A. Audit sources
1. Le fichier Excel KPI est ouvert et lu.
2. L’onglet KPI Pilotage Commercial est identifié.
3. Les KPI G.1 à G.21 utiles sont listés.
4. Les KPI P1 sont distingués des P2.
5. Les règles d’alerte Excel sont reprises.
6. Les axes d’analyse Excel sont repris.
7. Le modèle BIM est ouvert.
8. Les tables BIM sont listées.
9. Les mesures BIM sont listées.
10. Les relations BIM sont listées.
11. Les mesures RDV existantes sont identifiées.
12. Les mesures réseau existantes sont identifiées.
13. Les mesures rétrocommission existantes sont identifiées.
14. L’absence de fact_affaires est confirmée.
15. L’absence de budget_affaires est confirmée.
16. L’absence de fact_alertes est confirmée.
17. La maquette HTML correcte est utilisée.
18. Les images annotées Excel+BIM sont ouvertes.
19. Les anciennes maquettes COMEX sont ignorées.
20. Le périmètre Pilotage Commercial est confirmé.

## B. Modèle sémantique
21. Ne pas supprimer les tables existantes utiles.
22. Ne pas casser les relations existantes.
23. Créer seulement les mesures nécessaires.
24. Créer les tables cibles absentes en structure claire.
25. Documenter les tables absentes.
26. Réutiliser les mesures BIM OK.
27. Éviter les doublons de mesures.
28. Nommer les mesures métier clairement.
29. Ranger les mesures dans folders métier.
30. Ajouter descriptions de mesures.
31. Créer field parameters organisation.
32. Créer field parameters affaires.
33. Créer field parameters réseau.
34. Créer field parameters RDV.
35. Créer field parameter performance.
36. Créer tables mois ref / mois comparé.
37. Créer tables période si nécessaire.
38. Créer mesures couleurs conditionnelles.
39. Créer mesures d’alerte.
40. Créer mesures de recommandation.

## C. Pages
41. Page Accueil créée.
42. Page Performance créée.
43. Page Affaires créée.
44. Page Réseau MIA créée.
45. Page Réseau tableau ouvert créée ou bookmark équivalent.
46. Page Rendez-vous créée.
47. Page Alertes créée.
48. Page Glossaire créée.
49. Ordre des pages correct.
50. Nom des pages correct.

## D. Navigation
51. Header global présent.
52. Titre Pilotage Commercial présent.
53. Sous-titre présent.
54. Boutons de navigation présents.
55. Bouton actif rouge.
56. Boutons inactifs blancs bordés.
57. Navigation fonctionne.
58. Slicer périmètre à droite.
59. Header aligné.
60. Aucun chevauchement header.

## E. Slicers / field parameters
61. Slicer période présent.
62. Slicer axe organisation présent.
63. Slicer axe activité présent.
64. Field parameter performance présent.
65. Field parameter affaires présent.
66. Field parameter réseau présent.
67. Field parameter RDV présent.
68. Mois référence présent.
69. Mois comparé présent.
70. Tous les slicers stylés en pills/dropdowns.

## F. Cards fusionnées
71. Chaque card a une forme de fond.
72. Chaque card a un label KPI.
73. Chaque card a une valeur KPI.
74. Chaque card a un badge Excel.
75. Chaque card a un badge BIM.
76. Chaque card a chip Vs N-1 si applicable.
77. Chaque card a chip Vs MTD-1 si applicable.
78. Chaque card a sparkline si demandé.
79. Chaque card a barre budget si applicable.
80. Chaque card est groupée.
81. Le groupement Selection Pane est nommé.
82. Les couleurs conditionnelles fonctionnent.
83. Les icônes sont alignées.
84. Les éléments internes ne débordent pas.
85. Les tailles de cartes sont homogènes.

## G. Visuels métier
86. Line charts créés.
87. Bar charts créés.
88. Donuts créés.
89. Carte de France créée.
90. Tableaux créés.
91. Jauges alertes créées.
92. Légendes visibles.
93. Axes lisibles.
94. Titres des visuels corporate.
95. Types de visuels conformes à la spec.

## H. Alertes
96. Page alertes complète.
97. Sources alertes documentées.
98. fact_alertes cible documentée.
99. Recommandations visibles.
100. KPI d’alerte liés aux KPI Excel et statut BIM.

## I. Validation finale
101. Script overlap exécuté.
102. Aucun chevauchement non autorisé.
103. Captures finales générées.
104. Changelog créé.
105. KPI_STATUS_FINAL créé.
106. PBIP s’ouvre sans erreur.
107. Mesures DAX sans erreur.
108. Navigation testée.
109. Bookmarks testés.
110. Rapport prêt à livrer.
