# Pilotage Commercial — Option A + C v2
## Prompts techniques Power BI : KPI cards fusionnées + DAX + field parameters

Ce document complète le cahier précédent en détaillant la **composition exacte des cards KPI**. Une card ne doit pas être un simple visuel Power BI : elle doit être un **groupe d’objets fusionnés** avec fond, valeur, N-1, MTD-1, sparkline, budget bar et badges source Excel/BIM.

---

## 1. Template universel — Card KPI fusionnée

Créer un composant réutilisable `TPL_CARD_KPI_FUSIONNEE`.

Taille fixe : **286 px x 196 px**.  
Grille de ligne : 5 cartes par ligne sur page 1540 px, marge gauche 22 px, gap 16 px.  
Positions X : **22 / 324 / 626 / 928 / 1230**.

### Objets internes à créer et grouper

| Ordre | Nom objet Selection pane | Type Power BI | X relatif | Y relatif | W | H | Mise en forme |
|---:|---|---|---:|---:|---:|---:|---|
| 01 | `BG_Card` | Shape rounded rectangle | 0 | 0 | 286 | 196 | Fond #FFFFFF, bordure #E1E8F0, rayon 22 px, ombre douce |
| 02 | `TXT_KPI_Label` | Text box | 18 | 14 | 175 | 30 | Inter 10.5 px, uppercase, bold 800, #667085 |
| 03 | `SHAPE_Icon_BG` | Shape rounded rectangle | 224 | 14 | 44 | 44 | Fond #EAF3FF, rayon 14 px |
| 04 | `TXT_Icon` | Text/Icon | 224 | 14 | 44 | 44 | Inter 20 px, bold 900, #0A4E97, centré |
| 05 | `VIS_KPI_Value` | Card / New Card | 18 | 50 | 170 | 42 | Inter 29 px, weight 900, #1C2434, display unit auto |
| 06 | `CHIP_Var_N1_BG` | Shape pill | 18 | 96 | 82 | 24 | Fond conditionnel vert/orange/rouge doux, rayon 999 px |
| 07 | `TXT_Var_N1` | Text measure | 18 | 96 | 82 | 24 | Inter 10.5 px, bold 850, texte conditionnel |
| 08 | `CHIP_Var_MTD_BG` | Shape pill | 106 | 96 | 88 | 24 | Fond conditionnel vert/orange/rouge doux, rayon 999 px |
| 09 | `TXT_Var_MTD` | Text measure | 106 | 96 | 88 | 24 | Inter 10.5 px, bold 850, texte conditionnel |
| 10 | `VIS_Sparkline` | Mini line chart / SVG | 196 | 72 | 73 | 48 | Fond transparent, axes off, grid off, légende off, line 2.5 px |
| 11 | `TXT_Budget_Label` | Text box | 18 | 127 | 251 | 12 | Inter 9.5 px, uppercase, #667085 |
| 12 | `SHAPE_Budget_Track` | Shape rounded rectangle | 18 | 143 | 251 | 8 | Fond #E8EEF5, rayon 999 px |
| 13 | `SHAPE_Budget_Fill` | Shape/bar | 18 | 143 | variable | 8 | Largeur = min(taux budget, 120%) * 251, couleur conditionnelle |
| 14 | `SHAPE_Budget_Target` | Shape marker | 269 | 140 | 3 | 14 | Fond #D71920, repère budget 100% |
| 15 | `BADGE_Excel_KPI` | Badge texte | 18 | 162 | 112 | 22 | Fond #EAF3FF, texte #0A4E97, 8.5 px, bold |
| 16 | `BADGE_BIM_Status` | Badge texte | 136 | 162 | 133 | 22 | Fond conditionnel selon BIM : OK vert, partiel orange, absent rouge |

### Groupement obligatoire

Pour chaque carte, grouper les 16 objets sous le nom :

```text
GRP_CARD_<PAGE>_<NUMERO>_<NOM_KPI_COURT>
```

Exemple :

```text
GRP_CARD_ACCUEIL_01_VOLUME_AFFAIRES_PRODUITES
```

Dans le Selection pane :

```text
GRP_CARD_ACCUEIL_01_VOLUME_AFFAIRES_PRODUITES
 ├─ BG_Card
 ├─ TXT_KPI_Label
 ├─ SHAPE_Icon_BG
 ├─ TXT_Icon
 ├─ VIS_KPI_Value
 ├─ CHIP_Var_N1_BG
 ├─ TXT_Var_N1
 ├─ CHIP_Var_MTD_BG
 ├─ TXT_Var_MTD
 ├─ VIS_Sparkline
 ├─ TXT_Budget_Label
 ├─ SHAPE_Budget_Track
 ├─ SHAPE_Budget_Fill
 ├─ SHAPE_Budget_Target
 ├─ BADGE_Excel_KPI
 └─ BADGE_BIM_Status
```

---

## 2. Règles de mise en forme conditionnelle

### Chips N-1 et MTD-1

| Condition | Fond chip | Texte | Icône / préfixe |
|---|---|---|---|
| Variation >= 0 | #EAF7EF | #198754 | ▲ |
| Variation < 0 et > -10% | #FFF3E8 | #E67E22 | ▼ |
| Variation <= -10% | #FFF1F2 | #D71920 | ▼ |

### Barre Budget

| Condition | Couleur fill | Règle |
|---|---|---|
| Taux budget >= 100% | #198754 | Sur objectif |
| Taux budget >= 80% et < 100% | #E67E22 | Retard modéré |
| Taux budget < 80% | #D71920 | Retard fort |

### Badge BIM

| Statut BIM | Fond | Texte |
|---|---|---|
| BIM OK | #EAF7EF | #198754 |
| BIM partiel | #FFF3E8 | #E67E22 |
| BIM absent | #FFF1F2 | #D71920 |

---

## 3. Répartition des cards dans les pages

### Ligne standard 5 cards

```text
Canvas width : 1540 px
Marge gauche : 22 px
Marge droite : 24 px
Gap : 16 px
Card width : 286 px
Card height : 196 px
X card 1 : 22
X card 2 : 324
X card 3 : 626
X card 4 : 928
X card 5 : 1230
```

### Page Accueil

Cards à placer en Y=330 :

1. Volume d’affaires produites — Excel G.3 — BIM absent — créer `fact_affaires` + `[Volume affaires produites]`
2. Volume d’affaires en instance — Excel à confirmer — BIM absent — créer statut affaires
3. Volume d’affaires commissionnées — Excel à confirmer — BIM absent — créer statut commissionné
4. Montant moyen de rétrocommission — BIM OK — `_Indicateurs[Montant moyen de rétrocommission]`
5. Nombre rendez-vous réalisés — Excel G.15 — BIM OK — `_Indicateurs[Nombre rendez-vous réalisés]`

Chaque carte doit afficher :

```text
Label KPI en haut gauche
Valeur principale sous le label
Chip Vs N-1 à gauche
Chip Vs MTD-1 à côté
Sparkline à droite
Budget bar en bas si budget disponible
Badge Excel + badge BIM tout en bas
```

### Page Performance

Cards à placer en Y=330 :

1. Volume d’affaires produites — G.3 — budget G.5
2. Volume d’affaires en instance — à confirmer
3. Volume d’affaires commissionnées — à confirmer
4. Montant moyen de rétrocommission — BIM OK
5. Taux atteinte Budget N Volume — calcul G.3/G.5

Les 3 premières cartes doivent obligatoirement avoir une barre Budget N visible en bas.

### Page Affaires

Cards top row à placer en Y=330 :

1. Nombre d’affaires produites — G.2
2. Volume d’affaires produites — G.3
3. Volume d’affaires en instance — à confirmer
4. Volume d’affaires commissionnées — à confirmer
5. Montant moyen de rétrocommission — BIM OK

Mini-cards “Comparaison de deux mois” à placer en Y=610 :

- Mois référence : x=38, w=466, h=150
- Mois comparé : x=520, w=466, h=150
- Écart affaires : x=1002, w=466, h=150

### Page Réseau MIA

Cards top row à placer en Y=330 :

1. Nombre de MIA oriasés — à confirmer — BIM partiel
2. Nombre de MIA actifs — G.6 — BIM OK
3. Nombre de MIA productifs — G.8 — BIM absent
4. Nombre total de MIA commissionnés — G.10 — BIM OK
5. Montant moyen de rétrocommission — BIM OK

Mini-cards focus agence dans le panneau carte :

- Nombre de MIA actifs : x=780, y=715, w=205, h=78
- Nombre de MIA productifs : x=1000, y=715, w=205, h=78
- Nombre total de MIA commissionnés : x=780, y=807, w=205, h=78
- Montant moyen rétrocommission : x=1000, y=807, w=205, h=78

### Page Rendez-vous

Cards à placer en Y=330 :

1. Nombre rendez-vous réalisés — G.15 — BIM OK
2. Nombre rendez-vous prévus — G.14 — BIM OK
3. Nombre RDV Confirmés — à formaliser
4. Taux Réalisation RDV — G.13 — BIM OK
5. Taux RDV Visio / Domicile — G.18/G.19 — BIM OK

### Page Alertes

Cards à placer en Y=300 :

1. Nombre Alertes Critiques — fact_alertes à créer
2. Nombre Alertes Hautes — fact_alertes à créer
3. Nombre Alertes Moyennes — fact_alertes à créer
4. Nombre Alertes Ouvertes — fact_alertes à créer
5. Couleur Alerte — règle à créer

---

## 4. Prompt exact à donner à un agent Power BI pour une card

```text
Créer une KPI card fusionnée Power BI, sans utiliser une simple card isolée.
La carte doit être un groupe d’objets nommé GRP_CARD_<PAGE>_<N>_<KPI>.
Créer un fond rounded rectangle blanc #FFFFFF, bordure #E1E8F0, rayon 22 px, taille 286x196.
Position absolue de la carte : X=<X>, Y=<Y>.
À l’intérieur du groupe, créer :
- un label KPI en haut gauche à X+18, Y+14, W=175, H=30, Inter 10.5 px, uppercase, #667085 ;
- une icône dans un carré bleu doux à X+224, Y+14, W=44, H=44 ;
- une valeur principale à X+18, Y+50, W=170, H=42, Inter 29 px, bold 900 ;
- un chip Variation N-1 à X+18, Y+96, W=82, H=24 avec mise en forme conditionnelle ;
- un chip Variation MTD-1 à X+106, Y+96, W=88, H=24 avec mise en forme conditionnelle ;
- une sparkline exercice à X+196, Y+72, W=73, H=48, fond transparent, axes off ;
- une barre Budget N à X+18, Y+143, W=251, H=8, avec repère 100% rouge à X+269 ;
- un badge source Excel à X+18, Y+162, W=112, H=22 ;
- un badge statut BIM à X+136, Y+162, W=133, H=22.
Appliquer les règles de couleur :
- Variation positive : fond #EAF7EF, texte #198754 ;
- Variation négative modérée : fond #FFF3E8, texte #E67E22 ;
- Variation <= -10% : fond #FFF1F2, texte #D71920 ;
- Budget >=100% vert, 80-100% orange, <80% rouge ;
- BIM OK vert, BIM partiel orange, BIM absent rouge.
Masquer axes, titres automatiques, fonds et bordures natives des visuels internes.
Verrouiller le groupe dans le Selection pane.
```

---

## 5. Règles DAX nécessaires pour la card

Créer une mesure de valeur principale, une mesure N-1, une mesure MTD-1, une mesure Budget, une mesure Taux Budget, une mesure couleur variation, une mesure couleur budget et une mesure SVG sparkline si possible.

Les DAX complets sont dans le fichier `.dax` du pack.
