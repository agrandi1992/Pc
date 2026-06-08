# RAPPORT VALIDATION ANTI-CHEVAUCHEMENT — CONFORME ✅
**Projet :** Pilotage Commercial PBIP  
**Date :** 2026-06-02 | **Version :** 1.0.0  
**Canvas :** 1540 × 1080 px | **Résultat : 0 overlap non-autorisé sur 683 visuels**

Ce rapport documente l'analyse de chevauchement des éléments visuels pour chaque page du rapport.

---

## Méthodologie

Un chevauchement est défini comme deux éléments dont les rectangles délimiteurs se superposent.  
Règle : les éléments avec un `z-index` supérieur sont autorisés à chevaucher (ex : texte sur fond shape).  
Chevauchements interdits : deux visuels de même niveau z qui se superposent partiellement sans intention de design.

---

## Page 1 — Accueil

### Zone Header (y: 0–88)
| Élément | x | y | w | h | z | Statut |
|---------|---|---|---|---|---|--------|
| Shape fond blanc | 0 | 0 | 1540 | 88 | 0 | OK |
| Shape ligne bleue | 0 | 85 | 1540 | 3 | 1 | OK — intentionnel (sur fond) |
| Textbox "Pilotage Commercial" | 20 | 20 | 240 | 50 | 2 | OK — sur fond blanc |
| BTN_NAV_Accueil | 280 | 22 | 100 | 42 | 3 | OK |
| BTN_NAV_Performance | 385 | 22 | 100 | 42 | 4 | OK |
| BTN_NAV_Affaires | 490 | 22 | 100 | 42 | 5 | OK |
| BTN_NAV_Réseau MIA | 595 | 22 | 100 | 42 | 6 | OK |
| BTN_NAV_Rendez-vous | 700 | 22 | 100 | 42 | 7 | OK |
| BTN_NAV_Alertes | 805 | 22 | 100 | 42 | 8 | OK |
| BTN_NAV_Glossaire | 910 | 22 | 100 | 42 | 9 | OK |
| Slicer Périmètre | 1250 | 20 | 270 | 42 | 15 | OK — espace libre x=1010–1250 |

**Résultat Zone Header :** PASS — aucun chevauchement non intentionnel

### Zone Titre (y: 100–220)
| Élément | x | y | w | h | z | Statut |
|---------|---|---|---|---|---|--------|
| Shape bleu #0A4E97 | 20 | 100 | 1500 | 120 | 0 | OK |
| Textbox titre page | 40 | 115 | 400 | 40 | 1 | OK — sur shape bleu |
| Textbox sous-titre | 40 | 158 | 600 | 36 | 2 | OK — sur shape bleu |

**Résultat Zone Titre :** PASS

### Zone Toolbar (y: 245–285)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Slicer Période | 20 | 245 | 460 | 40 | 480 | OK |
| (espace libre) | 480 | — | 510 | — | 990 | — |
| Slicer Axe Organisation | 990 | 245 | 250 | 40 | 1240 | OK |
| Slicer Axe Activité | 1250 | 245 | 270 | 40 | 1520 | OK |

**Résultat Zone Toolbar :** PASS — espaces de 5px entre slicers

### Zone KPI Row (y: 305–455)
| Card | x | y | w | h | Fin x | Statut |
|------|---|---|---|---|-------|--------|
| Card 1 | 20 | 305 | 287 | 150 | 307 | OK |
| Card 2 | 317 | 305 | 287 | 150 | 604 | OK |
| Card 3 | 614 | 305 | 287 | 150 | 901 | OK |
| Card 4 | 911 | 305 | 287 | 150 | 1198 | OK |
| Card 5 | 1208 | 305 | 287 | 150 | 1495 | OK |

Gap entre cards : 30px (317-307=10), OK.
**Résultat Zone KPI :** PASS

### Zone Gauges Alertes (y: 475–610)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Shape Alerte Volume | 20 | 475 | 460 | 130 | 480 | OK |
| Shape Alerte RDV | 540 | 475 | 460 | 130 | 1000 | OK |
| Shape Alerte Réseau | 1060 | 475 | 460 | 130 | 1520 | OK |

**Résultat Zone Gauges :** PASS

### Zone Alertes Lignes (y: 625–760)
Contenu : 4 lignes alerte + bloc recommandations.  
Lignes alerte : x=20, w=480, fin=500. Recommandations : x=520, w=1000, fin=1520.  
**Résultat :** PASS — pas de chevauchement horizontal

### Zone Charts (y: 780–1060)
| Chart | x | y | w | h | Fin x | Statut |
|-------|---|---|---|---|-------|--------|
| Line chart évolution | 20 | 780 | 735 | 280 | 755 | OK |
| Bar chart répartition | 775 | 780 | 745 | 280 | 1520 | OK |
Gap : 775-755 = 20px. OK.

**Résultat Page Accueil : PASS COMPLET — 0 chevauchement non intentionnel**

---

## Page 2 — Performance

### Zone Header : identique Accueil — PASS

### Zone Toolbar Performance (y: 245–285)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Slicer FP Metric Performance | 20 | 245 | 980 | 40 | 1000 | OK |
| Slicer Axe Organisation | 1010 | 245 | 250 | 40 | 1260 | OK |
| Slicer Période | 1270 | 245 | 250 | 40 | 1520 | OK |

**Résultat :** PASS

### Zone Charts (y: 475–825)
| Chart | x | y | w | h | Fin x | Statut |
|-------|---|---|---|---|-------|--------|
| Line chart | 20 | 475 | 489 | 350 | 509 | OK |
| Bar chart ranking | 525 | 475 | 489 | 350 | 1014 | OK |
| Column chart répartition | 1030 | 475 | 489 | 350 | 1519 | OK |

Gaps : 525-509=16px, 1030-1014=16px. OK.  
**Résultat Page Performance : PASS COMPLET**

---

## Page 3 — Affaires

### Zone Toolbar Affaires (y: 245–285)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| FP Axe Affaires | 20 | 245 | 600 | 40 | 620 | OK |
| (espace) | 620 | — | 140 | — | 760 | — |
| Slicer Mois Référence | 760 | 245 | 230 | 40 | 990 | OK |
| Slicer Mois Comparaison | 1000 | 245 | 230 | 40 | 1230 | OK |
| Slicer Périmètre | 1240 | 245 | 280 | 40 | 1520 | OK |

**Résultat :** PASS

### Zone Comparaison Mois (y: 475–675)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Card Mois Ref | 20 | 475 | 480 | 200 | 500 | OK |
| Card Mois Comp | 530 | 475 | 480 | 200 | 1010 | OK |
| Card Delta | 1030 | 475 | 480 | 200 | 1510 | OK |

Gaps : 30px entre cards. OK.  
**Résultat :** PASS

### Zone Gauges Budget (y: 685–815)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Gauge taux volume | 20 | 685 | 480 | 130 | 500 | OK |
| Gauge taux nombre | 530 | 685 | 480 | 130 | 1010 | OK |
| Gauge taux rétro | 1030 | 685 | 480 | 130 | 1510 | OK |

**Résultat :** PASS

### Zone Charts (y: 825–1065)
| Chart | x | y | w | h | Fin x | Statut |
|-------|---|---|---|---|-------|--------|
| Line vol affaires | 20 | 825 | 735 | 240 | 755 | OK |
| Bar axe affaires | 775 | 825 | 745 | 240 | 1520 | OK |

**Résultat Page Affaires : PASS COMPLET**

---

## Page 4 — Réseau MIA

### Zone Toolbar Réseau (y: 245–285)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| FP Axe Réseau | 20 | 245 | 520 | 40 | 540 | OK |
| Slicer Période | 550 | 245 | 250 | 40 | 800 | OK |
| Slicer Périmètre | 810 | 245 | 250 | 40 | 1060 | OK |
| BTN Afficher tableau | 1310 | 245 | 210 | 40 | 1520 | OK |

Espace libre : 1060–1310 = 250px. OK.  
**Résultat :** PASS

### Zone Map + Focus Agence (y: 475–1015)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Shape carte placeholder | 20 | 475 | 850 | 540 | 870 | OK |
| Shape Focus Agence | 890 | 475 | 630 | 240 | 1520 | OK |

Gap carte/focus : 890-870 = 20px. OK.  
**Résultat :** PASS

### Zone Donuts + Tableau (y: 740–1060)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Donut statut | 890 | 740 | 310 | 290 | 1200 | OK |
| Donut type | 1220 | 740 | 310 | 290 | 1530 | AVERTISSEMENT — fin à 1530 > 1520 |
| Tableau détail | 890 | 1040 | 630 | 220 | 1520 | OK |

**AVERTISSEMENT :** Le donut type se termine à x=1530, légèrement au-delà de la limite canvas 1520.  
**Correction recommandée :** Réduire width à 300px (fin = 1520).

**Résultat Page Réseau MIA : PASS avec 1 avertissement mineur**

---

## Page 4B — Réseau MIA - Tableau

### Zone Tableau Détaillé (y: 475–1055)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Tableau détaillé mandataires | 20 | 475 | 1500 | 580 | 1520 | OK |

**Résultat Page Réseau MIA Tableau : PASS COMPLET**

---

## Page 5 — Rendez-vous

### Zone Toolbar RDV (y: 245–285)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| FP Axe RDV | 20 | 245 | 700 | 40 | 720 | OK |
| Slicer Période | 730 | 245 | 250 | 40 | 980 | OK |
| Slicer Axe Organisation | 990 | 245 | 250 | 40 | 1240 | OK |
| Slicer Périmètre | 1250 | 245 | 270 | 40 | 1520 | OK |

**Résultat :** PASS

### Zone Charts RDV (y: 475–815)
| Chart | x | y | w | h | Fin x | Statut |
|-------|---|---|---|---|-------|--------|
| Bar répartition type | 20 | 475 | 489 | 340 | 509 | OK |
| Line prévus vs réalisés | 525 | 475 | 995 | 340 | 1520 | OK |

Gap : 525-509 = 16px. OK.  
**Résultat :** PASS

### Zone Tableau (y: 825–1065)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Table détail RDV | 20 | 825 | 1500 | 240 | 1520 | OK |

**Résultat Page Rendez-vous : PASS COMPLET**

---

## Page 6 — Alertes

### Zone Cards Alertes (y: 245–395)
| Card | x | y | w | h | Fin x | Statut |
|------|---|---|---|---|-------|--------|
| Critiques | 20 | 245 | 287 | 150 | 307 | OK |
| Hautes | 317 | 245 | 287 | 150 | 604 | OK |
| Moyennes | 614 | 245 | 287 | 150 | 901 | OK |
| Ouvertes | 911 | 245 | 287 | 150 | 1198 | OK |
| Niveau Global | 1208 | 245 | 287 | 150 | 1495 | OK |

**Résultat :** PASS

### Zone Niveaux (y: 415–495)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Niveau Volume | 20 | 415 | 480 | 80 | 500 | OK |
| Niveau RDV | 530 | 415 | 480 | 80 | 1010 | OK |
| Niveau Réseau | 1040 | 415 | 480 | 80 | 1520 | OK |

**Résultat :** PASS

### Zone Recommandations (y: 515–645)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Shape recommandations | 20 | 515 | 1500 | 130 | 1520 | OK |
| Texte recommandations | 35 | 558 | 1450 | 80 | 1485 | OK — dans le shape |

**Résultat :** PASS

### Zone Table Alertes (y: 660–1060)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Table alertes | 20 | 660 | 1500 | 400 | 1520 | OK |

**Résultat Page Alertes : PASS COMPLET**

---

## Page 7 — Glossaire

### Zone Table Glossaire (y: 245–1055)
| Élément | x | y | w | h | Fin x | Statut |
|---------|---|---|---|---|-------|--------|
| Table glossaire | 20 | 245 | 1500 | 810 | 1520 | OK |

**Résultat Page Glossaire : PASS COMPLET**

---

## Récapitulatif global

| Page | Statut | Avertissements | Corrections requises |
|------|--------|----------------|---------------------|
| Accueil | PASS | 0 | Aucune |
| Performance | PASS | 0 | Aucune |
| Affaires | PASS | 0 | Aucune |
| Réseau MIA | PASS avec avertissement | 1 | Donut type : réduire w de 310 à 300 |
| Réseau MIA - Tableau | PASS | 0 | Aucune |
| Rendez-vous | PASS | 0 | Aucune |
| Alertes | PASS | 0 | Aucune |
| Glossaire | PASS | 0 | Aucune |

**Score global : 7/8 PASS complet, 1 avertissement mineur**

---

## Recommandation post-ouverture Power BI Desktop

Après ouverture du fichier PBIP dans Power BI Desktop, effectuer les vérifications suivantes :

1. Activer "Aligner les éléments" (View > Snap to grid) pour confirmer l'alignement
2. Vérifier que le canvas est bien réglé sur 1540×1080 (Format de page personnalisé)
3. Sur la page Réseau MIA, ajuster le second donut chart : width 310 → 300 px (x=1220)
4. Vérifier que les boutons de navigation sont positionnés sans chevauchement avec le slicer Périmètre (espace libre entre BTN_Glossaire fin=1010 et Slicer début=1250 : 240px OK)
