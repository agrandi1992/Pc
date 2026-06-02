# Pilotage Commercial — Option A + C
## Option A — Spécification visuelle détaillée page par page
Format de page recommandé : largeur 1540 px, fond #F1F5F9, police Inter, header fixe 88 px.

## 01_Accueil
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  | Créer un rectangle arrondi bleu derrière les textes ; grouper en G01_Title_Zone. |
| G02_Toolbar_Filtres | Période Jour/Semaine/Mois/Trimestre/Année | Segmented buttons | 20 | 260 | 460 | 42 | — · — | — |  | Créer des boutons ou slicer horizontal pour la granularité. |
| G02_Toolbar_Filtres | Slicer Axe Organisation | Slicer dropdown | 980 | 260 | 250 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation |  |
| G02_Toolbar_Filtres | Slicer Axe Activité | Slicer dropdown | 1240 | 260 | 280 | 42 | Axe RDV · Type de rendez-vous | BIM OK | FP_Axe_Activite |  |
| G03_KPI_Row_Top | Volume d’affaires produites | Card KPI | 20 | 330 | 287 | 150 | G.3 · Volume d'affaires produites (en euro) | BIM absent |  | Créer une carte KPI groupée : BG + TXT_Label + TXT_Value + Icon + chips. Afficher source KPI dans tooltip technique pour Volume d’affaires produites. |
| G03_KPI_Row_Top | Volume d’affaires en instance | Card KPI | 323 | 330 | 287 | 150 | À confirmer · Volume d'affaires en instance | BIM absent |  | Créer une carte KPI groupée : BG + TXT_Label + TXT_Value + Icon + chips. Afficher source KPI dans tooltip technique pour Volume d’affaires en instance. |
| G03_KPI_Row_Top | Volume d’affaires commissionnées | Card KPI | 626 | 330 | 287 | 150 | À confirmer · Volume d'affaires commissionnées | BIM absent |  | Créer une carte KPI groupée : BG + TXT_Label + TXT_Value + Icon + chips. Afficher source KPI dans tooltip technique pour Volume d’affaires commissionnées. |
| G03_KPI_Row_Top | Montant moyen de rétrocommission | Card KPI | 929 | 330 | 287 | 150 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK |  | Créer une carte KPI groupée : BG + TXT_Label + TXT_Value + Icon + chips. Afficher source KPI dans tooltip technique pour Montant moyen de rétrocommission. |
| G03_KPI_Row_Top | Nombre rendez-vous réalisés | Card KPI | 1232 | 330 | 287 | 150 | G.15 · Nombre de rendez-vous réalisés | BIM OK |  | Créer une carte KPI groupée : BG + TXT_Label + TXT_Value + Icon + chips. Afficher source KPI dans tooltip technique pour Nombre rendez-vous réalisés. |
| G04_Alert_Gauges | Niveau Alerte Volume | Gauge donut + texte | 20 | 500 | 489 | 132 | G.3 · Recommandation Volume | BIM absent |  | Créer une jauge circulaire ou donut custom. Niveau affiché en texte central. Tooltip : règle d’alerte + KPI source. |
| G04_Alert_Gauges | Niveau Alerte RDV | Gauge donut + texte | 525 | 500 | 489 | 132 | G.13 · Taux de réalisation des rendez-vous | BIM OK |  | Créer une jauge circulaire ou donut custom. Niveau affiché en texte central. Tooltip : règle d’alerte + KPI source. |
| G04_Alert_Gauges | Niveau Alerte Réseau | Gauge donut + texte | 1030 | 500 | 489 | 132 | Calcul G.6/(G.6+G.7) · Taux mandataires actifs | BIM à créer |  | Créer une jauge circulaire ou donut custom. Niveau affiché en texte central. Tooltip : règle d’alerte + KPI source. |
| G05_Alertes_Reco | Nombre Alertes Critiques | Carte liste / ligne alerte | 20 | 650 | 725 | 52 | À créer · Nombre Alertes Critiques | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G05_Alertes_Reco | Nombre Alertes Hautes | Carte liste / ligne alerte | 20 | 708 | 725 | 52 | À créer · Nombre Alertes Hautes | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G05_Alertes_Reco | Nombre Alertes Moyennes | Carte liste / ligne alerte | 20 | 766 | 725 | 52 | À créer · Nombre Alertes Moyennes | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G05_Alertes_Reco | Nombre Alertes Ouvertes | Carte liste / ligne alerte | 20 | 824 | 725 | 52 | À créer · Nombre Alertes Ouvertes | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G05_Alertes_Reco | Recommandation volume - action | Carte liste / ligne alerte | 775 | 650 | 725 | 52 | G.3 · Recommandation Volume | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G05_Alertes_Reco | Recommandation volume - suivi | Carte liste / ligne alerte | 775 | 708 | 725 | 52 | G.3 · Recommandation Volume | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G05_Alertes_Reco | Recommandation volume - conforme | Carte liste / ligne alerte | 775 | 766 | 725 | 52 | G.3 · Recommandation Volume | BIM absent |  | Créer avec une table/matrice stylée ou cartes groupées selon granularité. |
| G06_Bottom_Charts | Évolution du nombre d’affaires | Line chart | 20 | 950 | 735 | 340 | G.2 · Nombre d'affaires produites | BIM absent | FP_Metric_Performance | Line chart avec 3 mesures : produites, instance, commissionnées. Garder hauteur 270 pour zone graphique. |
| G06_Bottom_Charts | Répartition des affaires commissionnées | Bar chart horizontal | 775 | 950 | 745 | 340 | — · — | — |  | Créer après ajout dim_produit/fact_affaires. |

## 02_Performance
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone Performance | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  | Reprendre style Accueil. |
| G02_Performance_Parameters | Boutons mesure performance | Field parameter buttons | 20 | 260 | 980 | 42 | Calcul G.3/G.5 · Taux atteinte Budget N Volume | BIM absent | FP_Metric_Performance | Créer un field parameter de mesures et l’utiliser dans le bar chart Performance. |
| G03_KPI_Row | Volume d’affaires produites | Card KPI + budget gauge | 20 | 330 | 287 | 165 | G.3 · Volume d'affaires produites (en euro) | BIM absent | FP_Metric_Performance | Créer la carte KPI avec source visible en tooltip. |
| G03_KPI_Row | Volume d’affaires en instance | Card KPI + budget gauge | 323 | 330 | 287 | 165 | À confirmer · Volume d'affaires en instance | BIM absent | FP_Metric_Performance | Créer la carte KPI avec source visible en tooltip. |
| G03_KPI_Row | Volume d’affaires commissionnées | Card KPI + budget gauge | 626 | 330 | 287 | 165 | À confirmer · Volume d'affaires commissionnées | BIM absent | FP_Metric_Performance | Créer la carte KPI avec source visible en tooltip. |
| G03_KPI_Row | Montant moyen de rétrocommission | Card KPI + budget gauge | 929 | 330 | 287 | 165 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK | FP_Metric_Performance | Créer la carte KPI avec source visible en tooltip. |
| G03_KPI_Row | Taux atteinte Budget N Volume | Card KPI + budget gauge | 1232 | 330 | 287 | 165 | Calcul G.3/G.5 · Taux atteinte Budget N Volume | BIM absent | FP_Metric_Performance | Créer la carte KPI avec source visible en tooltip. |
| G04_Charts_Row | Évolution du nombre d’affaires | Line chart | 20 | 525 | 489 | 360 | G.2 · Nombre d'affaires produites | BIM absent |  |  |
| G04_Charts_Row | Performance réseau | Bar chart horizontal ranking | 525 | 525 | 489 | 360 | À confirmer · Volume d'affaires commissionnées | BIM absent | FP_Metric_Performance + FP_Axe_Organisation | Ranking par agence/secteur/mandataire. |
| G04_Charts_Row | Répartition des affaires commissionnées | Bar chart horizontal | 1030 | 525 | 489 | 360 | — · — | — |  |  |

## 03_Affaires
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone Affaires | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  |  |
| G02_Toolbar_Affaires | Axe affaires | Field parameter buttons | 20 | 260 | 600 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Affaires |  |
| G02_Toolbar_Affaires | Mois référence | Slicer dropdown | 760 | 260 | 230 | 42 | — · — | — |  |  |
| G02_Toolbar_Affaires | Mois comparé | Slicer dropdown | 1000 | 260 | 230 | 42 | — · — | — |  |  |
| G03_KPI_Row | Nombre d’affaires produites | Card KPI | 20 | 330 | 287 | 150 | G.2 · Nombre d'affaires produites | BIM absent |  |  |
| G03_KPI_Row | Volume d’affaires produites | Card KPI | 323 | 330 | 287 | 150 | G.3 · Volume d'affaires produites (en euro) | BIM absent |  |  |
| G03_KPI_Row | Volume d’affaires en instance | Card KPI | 626 | 330 | 287 | 150 | À confirmer · Volume d'affaires en instance | BIM absent |  |  |
| G03_KPI_Row | Volume d’affaires commissionnées | Card KPI | 929 | 330 | 287 | 150 | À confirmer · Volume d'affaires commissionnées | BIM absent |  |  |
| G03_KPI_Row | Montant moyen de rétrocommission | Card KPI | 1232 | 330 | 287 | 150 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK |  |  |
| G04_Month_Comparison | Comparaison de deux mois | Carte contenant 3 mini cards | 20 | 500 | 1500 | 230 | — · — | — |  | Utiliser 2 slicers déconnectés MoisRef/MoisComp ou calculation group. |
| G04_Month_Comparison | Mois référence | Mini card | 40 | 580 | 470 | 120 | — · — | — |  |  |
| G04_Month_Comparison | Mois comparé | Mini card | 525 | 580 | 470 | 120 | — · — | — |  |  |
| G04_Month_Comparison | Écart affaires | Mini card | 1010 | 580 | 470 | 120 | G.3 · Volume d'affaires produites (en euro) | BIM absent |  |  |
| G05_Budget_Gauges | Taux atteinte Budget N Volume | Gauge donut | 20 | 750 | 489 | 132 | Calcul G.3/G.5 · Taux atteinte Budget N Volume | BIM absent |  |  |
| G05_Budget_Gauges | Budget N Volume Affaires | Gauge donut | 525 | 750 | 489 | 132 | G.5 · Budget affaires en euro | BIM absent |  |  |
| G05_Budget_Gauges | Budget N Rétrocommission | Gauge donut | 1030 | 750 | 489 | 132 | Hors Excel direct · Montant rétrocommission | BIM OK |  | Prévoir colonne budget_retroc_euro. |
| G06_Bottom_Charts | Volume d’affaires — Réalisé vs N-1 vs MTD-1 | Line chart | 20 | 900 | 735 | 340 | G.3 · Volume d'affaires produites (en euro) | BIM absent |  |  |
| G06_Bottom_Charts | Axes d’analyse affaires | Horizontal bars | 775 | 900 | 745 | 340 | G.3 · Volume d'affaires produites (en euro) | BIM absent | FP_Axe_Affaires |  |

## 04_Reseau
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone Réseau | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  |  |
| G02_Toolbar_Reseau | Axe réseau | Field parameter buttons | 20 | 260 | 520 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Reseau |  |
| G02_Toolbar_Reseau | Afficher le tableau | Button bookmark | 1310 | 260 | 210 | 42 | — · — | — |  | Bouton d'affichage table. |
| G03_KPI_Row | Nombre de MIA oriasés | Card KPI | 20 | 330 | 287 | 150 | À confirmer · Nombre MIA oriasés | BIM partiel |  |  |
| G03_KPI_Row | Nombre de MIA actifs | Card KPI | 323 | 330 | 287 | 150 | G.6 · Nombre de mandataire Actif | BIM OK |  |  |
| G03_KPI_Row | Nombre de MIA productifs | Card KPI | 626 | 330 | 287 | 150 | G.8 · Nombre de mandataire Productif | BIM absent |  |  |
| G03_KPI_Row | Nombre total de MIA commissionnés | Card KPI | 929 | 330 | 287 | 150 | G.10 · Nombre de mandataire rétrocommissionés | BIM OK |  |  |
| G03_KPI_Row | Montant moyen de rétrocommission | Card KPI | 1232 | 330 | 287 | 150 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK |  |  |
| G04_Map_Main | Carte de France — Nombre mandataires actifs par Agence | Shape map / Azure map / image + bubbles | 20 | 510 | 850 | 560 | — · — | — | FP_Axe_Reseau | Utiliser Azure Map si lat/long, sinon Shape Map ou image France + points. |
| G04_Map_Main | Focus agence sélectionnée | Card + 4 mini KPI | 900 | 510 | 620 | 260 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Reseau |  |
| G04_Map_Main | Mini KPI MIA actifs | Mini card | 920 | 610 | 285 | 76 | G.6 · Nombre de mandataire Actif | BIM OK |  |  |
| G04_Map_Main | Mini KPI MIA productifs | Mini card | 1215 | 610 | 285 | 76 | G.8 · Nombre de mandataire Productif | BIM absent |  |  |
| G04_Map_Main | Mini KPI MIA commissionnés | Mini card | 920 | 696 | 285 | 76 | G.10 · Nombre de mandataire rétrocommissionés | BIM OK |  |  |
| G04_Map_Main | Mini KPI montant rétro | Mini card | 1215 | 696 | 285 | 76 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK |  |  |
| G05_Right_Analytics | Répartition des RDV par CSP | Donut | 900 | 790 | 300 | 300 | G.15 · Nombre de rendez-vous réalisés | BIM OK |  | À connecter à CSP si la dimension existe. |
| G05_Right_Analytics | Répartition MIA | Donut | 1220 | 790 | 300 | 300 | — · — | — |  |  |
| G05_Right_Analytics | Petit tableau réseau | Table | 900 | 1110 | 620 | 230 | — · — | — |  |  |
| G05_Right_Analytics | Nombre de MIA Productifs | Bar chart | 900 | 1360 | 620 | 300 | G.8 · Nombre de mandataire Productif | BIM absent | FP_Axe_Reseau |  |

## 04B_Reseau_Table
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone Réseau | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  |  |
| G02_Toolbar_Reseau | Axe réseau | Field parameter buttons | 20 | 260 | 520 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Reseau |  |
| G02_Toolbar_Reseau | Afficher le tableau | Button bookmark | 1310 | 260 | 210 | 42 | — · — | — |  | Bouton d'affichage table. |
| G03_KPI_Row | Nombre de MIA oriasés | Card KPI | 20 | 330 | 287 | 150 | À confirmer · Nombre MIA oriasés | BIM partiel |  |  |
| G03_KPI_Row | Nombre de MIA actifs | Card KPI | 323 | 330 | 287 | 150 | G.6 · Nombre de mandataire Actif | BIM OK |  |  |
| G03_KPI_Row | Nombre de MIA productifs | Card KPI | 626 | 330 | 287 | 150 | G.8 · Nombre de mandataire Productif | BIM absent |  |  |
| G03_KPI_Row | Nombre total de MIA commissionnés | Card KPI | 929 | 330 | 287 | 150 | G.10 · Nombre de mandataire rétrocommissionés | BIM OK |  |  |
| G03_KPI_Row | Montant moyen de rétrocommission | Card KPI | 1232 | 330 | 287 | 150 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK |  |  |
| G04_Map_Main | Carte de France — Nombre mandataires actifs par Agence | Shape map / Azure map / image + bubbles | 20 | 510 | 850 | 560 | — · — | — | FP_Axe_Reseau | Utiliser Azure Map si lat/long, sinon Shape Map ou image France + points. |
| G04_Map_Main | Focus agence sélectionnée | Card + 4 mini KPI | 900 | 510 | 620 | 260 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Reseau |  |
| G04_Map_Main | Mini KPI MIA actifs | Mini card | 920 | 610 | 285 | 76 | G.6 · Nombre de mandataire Actif | BIM OK |  |  |
| G04_Map_Main | Mini KPI MIA productifs | Mini card | 1215 | 610 | 285 | 76 | G.8 · Nombre de mandataire Productif | BIM absent |  |  |
| G04_Map_Main | Mini KPI MIA commissionnés | Mini card | 920 | 696 | 285 | 76 | G.10 · Nombre de mandataire rétrocommissionés | BIM OK |  |  |
| G04_Map_Main | Mini KPI montant rétro | Mini card | 1215 | 696 | 285 | 76 | Hors Excel direct · Montant moyen de rétrocommission | BIM OK |  |  |
| G05_Right_Analytics | Répartition des RDV par CSP | Donut | 900 | 790 | 300 | 300 | G.15 · Nombre de rendez-vous réalisés | BIM OK |  | À connecter à CSP si la dimension existe. |
| G05_Right_Analytics | Répartition MIA | Donut | 1220 | 790 | 300 | 300 | — · — | — |  |  |
| G05_Right_Analytics | Petit tableau réseau | Table | 900 | 1110 | 620 | 230 | — · — | — |  |  |
| G05_Right_Analytics | Nombre de MIA Productifs | Bar chart | 900 | 1360 | 620 | 300 | G.8 · Nombre de mandataire Productif | BIM absent | FP_Axe_Reseau |  |
| G06_Table_Detail | Tableau réseau détaillé ouvert | Table détaillée | 20 | 1680 | 1500 | 250 | — · — | — |  | Créer deux bookmarks et masquer/afficher le groupe G06_Table_Detail. |

## 05_RDV
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone RDV | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  |  |
| G02_Toolbar_RDV | Axe rendez-vous | Field parameter buttons | 20 | 260 | 700 | 42 | Axe RDV · Type de rendez-vous | BIM OK | FP_Axe_RDV |  |
| G03_KPI_Row | Nombre rendez-vous réalisés | Card KPI | 20 | 330 | 287 | 150 | G.15 · Nombre de rendez-vous réalisés | BIM OK |  |  |
| G03_KPI_Row | Nombre rendez-vous prévus | Card KPI | 323 | 330 | 287 | 150 | G.14 · Nombre de rendez-vous prévus | BIM OK |  |  |
| G03_KPI_Row | Nombre RDV Confirmés | Card KPI | 626 | 330 | 287 | 150 | G.14 · Nombre de rendez-vous prévus | BIM OK |  |  |
| G03_KPI_Row | Taux Réalisation RDV | Card KPI | 929 | 330 | 287 | 150 | G.13 · Taux de réalisation des rendez-vous | BIM OK |  |  |
| G03_KPI_Row | Taux RDV Visio / Domicile | Card KPI | 1232 | 330 | 287 | 150 | G.18 · Taux de rendez-vous réalisés en visioconférence | BIM OK |  |  |
| G04_Charts_Middle | Répartition des rendez-vous réalisés | Bar chart | 20 | 510 | 489 | 340 | G.15 · Nombre de rendez-vous réalisés | BIM OK | FP_Axe_RDV |  |
| G04_Charts_Middle | Nombre rendez-vous prévus VS réalisés | Line chart | 525 | 510 | 995 | 340 | G.14 · Nombre de rendez-vous prévus | BIM OK |  |  |
| G05_Table_Bottom | Détail rendez-vous | Matrix table | 20 | 880 | 1500 | 260 | G.15 · Nombre de rendez-vous réalisés | BIM OK |  |  |

## 06_Alertes
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone Alertes | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  |  |
| G02_KPI_Row | Nombre Alertes Critiques | Card KPI | 20 | 275 | 287 | 150 | À créer · Nombre Alertes Critiques | BIM absent |  |  |
| G02_KPI_Row | Nombre Alertes Hautes | Card KPI | 323 | 275 | 287 | 150 | À créer · Nombre Alertes Hautes | BIM absent |  |  |
| G02_KPI_Row | Nombre Alertes Moyennes | Card KPI | 626 | 275 | 287 | 150 | À créer · Nombre Alertes Moyennes | BIM absent |  |  |
| G02_KPI_Row | Nombre Alertes Ouvertes | Card KPI | 929 | 275 | 287 | 150 | À créer · Nombre Alertes Ouvertes | BIM absent |  |  |
| G02_KPI_Row | Couleur Alerte | Card KPI | 1232 | 275 | 287 | 150 | À créer · Couleur Alerte | BIM absent |  |  |
| G03_Alert_Levels | Niveau Alerte Volume | Liste alerte/recommandation | 20 | 455 | 725 | 68 | G.3 · Recommandation Volume | BIM absent |  |  |
| G03_Alert_Levels | Niveau Alerte RDV | Liste alerte/recommandation | 20 | 535 | 725 | 68 | G.13 · Taux de réalisation des rendez-vous | BIM OK |  |  |
| G03_Alert_Levels | Niveau Alerte Réseau | Liste alerte/recommandation | 20 | 615 | 725 | 68 | Calcul G.6/(G.6+G.7) · Taux mandataires actifs | BIM à créer |  |  |
| G03_Alert_Levels | Recommandation Volume - action | Liste alerte/recommandation | 775 | 455 | 725 | 68 | G.3 · Recommandation Volume | BIM absent |  |  |
| G03_Alert_Levels | Recommandation Volume - suivi | Liste alerte/recommandation | 775 | 535 | 725 | 68 | G.3 · Recommandation Volume | BIM absent |  |  |
| G03_Alert_Levels | Recommandation Volume - conforme | Liste alerte/recommandation | 775 | 615 | 725 | 68 | G.3 · Recommandation Volume | BIM absent |  |  |
| G05_Alert_Detail_Table | Détail alertes | Table | 20 | 760 | 1500 | 360 | — · — | — |  | Créer une table vide connectée plus tard à fact_alertes. |

## 07_Glossaire
| Groupe | Élément | Type | X | Y | W | H | KPI Excel | Statut BIM | Field parameter | Prompt technique |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| G00_Header_Global | Header global | Shape + groupes boutons | 0 | 0 | 1540 | 88 | — · — | — |  | Utiliser Page Navigator ou boutons avec action Page navigation. Conserver même header sur toutes les pages. |
| G00_Header_Global | Navigation pages | Boutons | 280 | 22 | 820 | 42 | — · — | — |  | Nommer chaque bouton BTN_NAV_<page>. Synchroniser le style actif via boutons séparés par page. |
| G00_Header_Global | Slicer périmètre global | Slicer dropdown | 1250 | 20 | 260 | 42 | Axe organisation · Agence | BIM OK partiel | FP_Axe_Organisation | Connecter aux dimensions organisation disponibles ; prévoir dim_organisation si région/secteur manquants. |
| G01_Title_Zone | Title zone Glossaire | Shape + textes | 20 | 110 | 1500 | 132 | — · — | — |  |  |
| G02_Glossary_Table | Glossaire KPI | Table | 20 | 270 | 1500 | 650 | G.2 · Nombre d'affaires produites | BIM absent |  | Créer une table de glossaire enrichie avec index Excel et statut BIM. |

## Option C — DAX / tables / field parameters
```DAX

/* =====================================================================================
PILOTAGE COMMERCIAL — OPTION C
DAX / FIELD PARAMETERS / TABLES CIBLES
Version générée pour compléter le modèle BIM existant.
À coller de préférence via Tabular Editor, ou à recréer manuellement dans Power BI.
===================================================================================== */

/* -------------------------------------------------------------------------------------
1) TABLES PHYSIQUES À INTÉGRER DANS LA COUCHE GOLD / MODÈLE
--------------------------------------------------------------------------------------
fact_affaires — table à créer dans la couche Gold puis importer dans le modèle :
- affaire_id
- mandataire_id
- agence_id
- produit_id
- assureur_id
- apporteur_id
- evenement_id
- date_affaire
- statut_affaire : Produite / Instance / Commissionnée / Annulée
- montant_affaire
- montant_retroc
- nombre_ventes_partage
- flag_produite
- flag_instance
- flag_commissionnee

budget_affaires — table à intégrer :
- budget_id
- date_budget
- agence_id
- produit_id
- assureur_id
- budget_affaires_nombre
- budget_affaires_euro
- budget_retroc_euro

fact_alertes — table cible :
- alerte_id
- date_analyse
- date_detection
- niveau_priorite : CRITIQUE / HAUTE / MOYENNE / INFO
- categorie_alerte : Volume / RDV / Réseau / Budget
- kpi_concerne
- valeur_actuelle
- seuil_alerte
- ecart
- agence_id
- mandataire_id
- impact_metier
- recommandation
- statut_alerte : Ouverte / En cours / Cloturee
------------------------------------------------------------------------------------- */


/* -------------------------------------------------------------------------------------
2) MESURES AFFAIRES — À CRÉER SUR _Indicateurs OU DANS UN DOSSIER 01. Affaires
------------------------------------------------------------------------------------- */

Nombre ventes =
COALESCE ( SUM ( fact_affaires[nombre_ventes_partage] ), 0 )

Nombre affaires produites =
COALESCE (
    CALCULATE (
        DISTINCTCOUNT ( fact_affaires[affaire_id] ),
        fact_affaires[flag_produite] = TRUE ()
    ),
    0
)

Volume affaires produites =
COALESCE (
    CALCULATE (
        SUM ( fact_affaires[montant_affaire] ),
        fact_affaires[flag_produite] = TRUE ()
    ),
    0
)

Nombre affaires en instance =
COALESCE (
    CALCULATE (
        DISTINCTCOUNT ( fact_affaires[affaire_id] ),
        fact_affaires[flag_instance] = TRUE ()
    ),
    0
)

Volume affaires en instance =
COALESCE (
    CALCULATE (
        SUM ( fact_affaires[montant_affaire] ),
        fact_affaires[flag_instance] = TRUE ()
    ),
    0
)

Nombre affaires commissionnées =
COALESCE (
    CALCULATE (
        DISTINCTCOUNT ( fact_affaires[affaire_id] ),
        fact_affaires[flag_commissionnee] = TRUE ()
    ),
    0
)

Volume affaires commissionnées =
COALESCE (
    CALCULATE (
        SUM ( fact_affaires[montant_affaire] ),
        fact_affaires[flag_commissionnee] = TRUE ()
    ),
    0
)

Budget affaires en nombre =
COALESCE ( SUM ( budget_affaires[budget_affaires_nombre] ), 0 )

Budget affaires en euro =
COALESCE ( SUM ( budget_affaires[budget_affaires_euro] ), 0 )

Budget rétrocommission en euro =
COALESCE ( SUM ( budget_affaires[budget_retroc_euro] ), 0 )

Taux atteinte Budget N Volume =
DIVIDE ( [Volume affaires produites], [Budget affaires en euro], 0 )

Volume affaires produites N-1 =
CALCULATE (
    [Volume affaires produites],
    SAMEPERIODLASTYEAR ( dim_date[Date] )
)

Variation vs N-1 Volume Affaires =
[Volume affaires produites] - [Volume affaires produites N-1]

Variation vs N-1 Volume Affaires (%) =
DIVIDE (
    [Variation vs N-1 Volume Affaires],
    [Volume affaires produites N-1],
    0
)

Volume affaires produites MTD-1 =
CALCULATE (
    [Volume affaires produites],
    DATEADD ( dim_date[Date], -1, MONTH )
)

Variation vs MTD-1 Volume Affaires =
[Volume affaires produites] - [Volume affaires produites MTD-1]

Variation vs MTD-1 Volume Affaires (%) =
DIVIDE (
    [Variation vs MTD-1 Volume Affaires],
    [Volume affaires produites MTD-1],
    0
)


/* -------------------------------------------------------------------------------------
3) MESURES RÉSEAU MIA — À CRÉER / COMPLÉTER
------------------------------------------------------------------------------------- */

Nombre MIA oriasés =
COALESCE (
    CALCULATE (
        DISTINCTCOUNT ( dim_mandataire[mandataire_id] ),
        NOT ISBLANK ( dim_mandataire[numero_orias] )
    ),
    0
)

Nombre MIA productifs =
COALESCE (
    CALCULATE (
        DISTINCTCOUNT ( fact_affaires[mandataire_id] ),
        fact_affaires[flag_produite] = TRUE ()
    ),
    0
)

Nombre MIA non productifs =
MAX ( [Nombre mandataires actifs] - [Nombre MIA productifs], 0 )

Nombre mandataires non rétrocommissionnés =
MAX ( [Nombre mandataires actifs] - [Nombre mandataires rétrocommissionnés], 0 )

Taux mandataires actifs =
DIVIDE (
    [Nombre mandataires actifs],
    [Nombre mandataires actifs] + [Nombre mandataires inactifs],
    0
)

Montant rétrocommission moyen corrigé =
AVERAGEX (
    VALUES ( dim_mandataire[mandataire_id] ),
    [Montant rétrocommission]
)


/* -------------------------------------------------------------------------------------
4) MESURES RDV COMPLÉMENTAIRES
------------------------------------------------------------------------------------- */

Nombre RDV hebdomadaire moyen =
VAR NbSemaines =
    DISTINCTCOUNT ( dim_date[numero_de_la_semaine] )
RETURN
DIVIDE ( [Nombre rendez-vous réalisés], NbSemaines, 0 )

Nombre RDV confirmés =
CALCULATE (
    [Nombre rendez-vous prévus],
    -- Adapter ce filtre si une colonne statut_rdv existe dans la source
    KEEPFILTERS ( fact_rendez_vous_client[flag_rendez_vous_realise] IN { TRUE (), FALSE () } )
)

Taux RDV Visio / Domicile =
VAR Visio = [Taux rendez vous réalisés en visioconférence]
VAR Domicile = [Taux rendez-vous faits à domicile]
RETURN
FORMAT ( Visio, "0.0%" ) & " / " & FORMAT ( Domicile, "0.0%" )


/* -------------------------------------------------------------------------------------
5) ALERTES ET RECOMMANDATIONS
------------------------------------------------------------------------------------- */

Niveau Alerte Volume =
VAR VarPct = [Variation vs N-1 Volume Affaires (%)]
RETURN
SWITCH (
    TRUE (),
    ISBLANK ( VarPct ), "NON DISPONIBLE",
    VarPct < -0.20, "CRITIQUE",
    VarPct < -0.10, "HAUTE",
    VarPct < 0, "MOYENNE",
    "CONFORME"
)

Couleur Alerte Volume =
SWITCH (
    [Niveau Alerte Volume],
    "CRITIQUE", "#D71920",
    "HAUTE", "#E67E22",
    "MOYENNE", "#F1C40F",
    "CONFORME", "#198754",
    "#667085"
)

Niveau Alerte RDV =
VAR Taux = [Taux réalisation de rendez-vous]
RETURN
SWITCH (
    TRUE (),
    ISBLANK ( Taux ), "NON DISPONIBLE",
    Taux < 0.50, "CRITIQUE",
    Taux < 0.70, "HAUTE",
    Taux < 0.85, "MOYENNE",
    "CONFORME"
)

Couleur Alerte RDV =
SWITCH (
    [Niveau Alerte RDV],
    "CRITIQUE", "#D71920",
    "HAUTE", "#E67E22",
    "MOYENNE", "#F1C40F",
    "CONFORME", "#198754",
    "#667085"
)

Niveau Alerte Réseau =
VAR Taux = [Taux mandataires actifs]
RETURN
SWITCH (
    TRUE (),
    ISBLANK ( Taux ), "NON DISPONIBLE",
    Taux < 0.60, "CRITIQUE",
    Taux < 0.80, "HAUTE",
    Taux < 0.90, "MOYENNE",
    "CONFORME"
)

Couleur Alerte Réseau =
SWITCH (
    [Niveau Alerte Réseau],
    "CRITIQUE", "#D71920",
    "HAUTE", "#E67E22",
    "MOYENNE", "#F1C40F",
    "CONFORME", "#198754",
    "#667085"
)

Recommandation Volume =
VAR VarPct = [Variation vs N-1 Volume Affaires (%)]
RETURN
SWITCH (
    TRUE (),
    ISBLANK ( VarPct ), "Donnée volume affaires indisponible : intégrer fact_affaires.",
    VarPct < -0.10, "Identifier les agences contributrices au recul et déclencher un plan de relance.",
    VarPct < 0, "Surveiller la trajectoire et challenger les zones en retrait.",
    "Sécuriser l’atterrissage."
)

Nombre Alertes Critiques =
COALESCE (
    CALCULATE (
        COUNTROWS ( fact_alertes ),
        fact_alertes[niveau_priorite] = "CRITIQUE",
        fact_alertes[statut_alerte] <> "Cloturee"
    ),
    0
)

Nombre Alertes Hautes =
COALESCE (
    CALCULATE (
        COUNTROWS ( fact_alertes ),
        fact_alertes[niveau_priorite] = "HAUTE",
        fact_alertes[statut_alerte] <> "Cloturee"
    ),
    0
)

Nombre Alertes Moyennes =
COALESCE (
    CALCULATE (
        COUNTROWS ( fact_alertes ),
        fact_alertes[niveau_priorite] = "MOYENNE",
        fact_alertes[statut_alerte] <> "Cloturee"
    ),
    0
)

Nombre Alertes Ouvertes =
COALESCE (
    CALCULATE (
        COUNTROWS ( fact_alertes ),
        fact_alertes[statut_alerte] <> "Cloturee"
    ),
    0
)


/* -------------------------------------------------------------------------------------
6) TABLES DÉCONNECTÉES POUR COMPARAISON DE MOIS
------------------------------------------------------------------------------------- */

Mois Référence =
SELECTCOLUMNS (
    dim_date,
    "Date", dim_date[Date],
    "Année Mois", dim_date[annee_mois],
    "Mois", dim_date[nom_du_mois]
)

Mois Comparé =
SELECTCOLUMNS (
    dim_date,
    "Date", dim_date[Date],
    "Année Mois", dim_date[annee_mois],
    "Mois", dim_date[nom_du_mois]
)

Volume affaires mois référence =
VAR MoisRef =
    SELECTEDVALUE ( 'Mois Référence'[Année Mois] )
RETURN
CALCULATE (
    [Volume affaires produites],
    TREATAS ( { MoisRef }, dim_date[annee_mois] )
)

Volume affaires mois comparé =
VAR MoisComp =
    SELECTEDVALUE ( 'Mois Comparé'[Année Mois] )
RETURN
CALCULATE (
    [Volume affaires produites],
    TREATAS ( { MoisComp }, dim_date[annee_mois] )
)

Écart affaires mois comparé vs référence =
[Volume affaires mois comparé] - [Volume affaires mois référence]

Écart affaires mois comparé vs référence (%) =
DIVIDE (
    [Écart affaires mois comparé vs référence],
    [Volume affaires mois référence],
    0
)


/* -------------------------------------------------------------------------------------
7) FIELD PARAMETERS — VERSION CIBLE
Attention : les colonnes Région / Secteur / Centre d'affaires doivent exister.
Si elles ne sont pas dans dim_agence aujourd’hui, créer dim_organisation ou enrichir dim_agence.
------------------------------------------------------------------------------------- */

FP_Axe_Organisation =
{
    ( "Agence", NAMEOF ( dim_agence[raison_sociale] ), 0 ),
    ( "Ville agence", NAMEOF ( dim_agence[ville_agence] ), 1 ),
    ( "Mandataire", NAMEOF ( dim_mandataire[mandataire_id] ), 2 )
    -- Ajouter après enrichissement :
    -- ( "Région", NAMEOF ( dim_organisation[region] ), 3 ),
    -- ( "Centre d'affaires", NAMEOF ( dim_organisation[centre_affaires] ), 4 ),
    -- ( "Secteur", NAMEOF ( dim_organisation[secteur] ), 5 )
}

FP_Axe_RDV =
{
    ( "Type de rendez-vous", NAMEOF ( dim_type_rendez_vous_client[libelle_type_rendez_vous] ), 0 ),
    ( "Canal de rendez-vous", NAMEOF ( dim_type_canal[libelle_type_canal] ), 1 )
    -- Ajouter si disponible :
    -- ( "Statut rendez-vous", NAMEOF ( dim_statut_rendez_vous[libelle_statut] ), 2 ),
    -- ( "Motif rendez-vous", NAMEOF ( dim_motif_rendez_vous[libelle_motif] ), 3 )
}

FP_Axe_Reseau =
{
    ( "Agence", NAMEOF ( dim_agence[raison_sociale] ), 0 ),
    ( "Ville agence", NAMEOF ( dim_agence[ville_agence] ), 1 ),
    ( "Mandataire", NAMEOF ( dim_mandataire[mandataire_id] ), 2 )
}

FP_Metric_Performance =
{
    ( "Volume d’affaires produites", NAMEOF ( _Indicateurs[Volume affaires produites] ), 0 ),
    ( "Volume d’affaires en instance", NAMEOF ( _Indicateurs[Volume affaires en instance] ), 1 ),
    ( "Volume d’affaires commissionnées", NAMEOF ( _Indicateurs[Volume affaires commissionnées] ), 2 ),
    ( "Montant moyen de rétrocommission", NAMEOF ( _Indicateurs[Montant moyen de rétrocommission] ), 3 ),
    ( "Taux atteinte Budget N Volume", NAMEOF ( _Indicateurs[Taux atteinte Budget N Volume] ), 4 )
}

```
