
# Prompts techniques Power BI v3 — Navigation, slicers, field parameters, types de visuels et cards fusionnées

## Principe général

Construire le rapport Power BI **Pilotage Commercial** comme une maquette pixel-perfect en composants groupés.  
Chaque élément de page doit être nommé dans le panneau de sélection, dimensionné avec des coordonnées fixes et rattaché à son KPI Excel + statut BIM.

Canvas de référence : **1540 px de largeur**.  
Fond global : `#F1F5F9`.  
Police : `Inter`, fallback `Segoe UI`.

---

## 1. Menu de navigation global

### Prompt Power BI

Créer un header global présent sur toutes les pages.

- Position : `x=0, y=0, w=1540, h=88`
- Type : rectangle blanc + boutons Power BI
- Fond : `#FFFFFF`
- Bordure basse : `#E1E8F0`, 1 px
- Ombre douce : équivalent `0 8px 22px rgba(15,23,42,.05)`
- Groupe Selection pane : `G00_Header_Global`

### Éléments internes

| Objet | X | Y | W | H | Type | Style |
|---|---:|---:|---:|---:|---|---|
| Brand titre | 24 | 18 | 250 | 24 | Text box | Inter 20 bold, `#073B73` |
| Brand sous-titre | 24 | 48 | 310 | 18 | Text box | Inter 12, `#667085` |
| Container menu | 360 | 18 | 760 | 46 | Group | Boutons pills |
| Slicer global périmètre | 1220 | 18 | 290 | 40 | Dropdown slicer | Radius 999, border `#E1E8F0` |

### Boutons de navigation

Chaque bouton est un bouton Power BI action page navigation.

| Bouton | X | Y | W | H | Action |
|---|---:|---:|---:|---:|---|
| Accueil | 360 | 20 | 78 | 36 | Page Accueil |
| Performance | 446 | 20 | 112 | 36 | Page Performance |
| Affaires | 566 | 20 | 88 | 36 | Page Affaires |
| Réseau MIA | 662 | 20 | 116 | 36 | Page Réseau MIA |
| Rendez-vous | 786 | 20 | 122 | 36 | Page Rendez-vous |
| Alertes | 916 | 20 | 86 | 36 | Page Alertes |
| Glossaire | 1010 | 20 | 98 | 36 | Page Glossaire |

### Mise en forme des boutons

- Bouton actif :
  - Fill : `#D71920`
  - Border : `#D71920`
  - Texte : `#FFFFFF`
  - Font : Inter 11, bold
  - Radius : 999
- Bouton inactif :
  - Fill : `#FFFFFF`
  - Border : `#F3CFD2`
  - Texte : `#D71920`
  - Hover : fill `#D71920`, texte blanc
- Nommer les groupes :
  - `NAV_Accueil`
  - `NAV_Performance`
  - `NAV_Affaires`
  - `NAV_Reseau`
  - `NAV_RDV`
  - `NAV_Alertes`
  - `NAV_Glossaire`

---

## 2. Slicers et field parameters

### Slicer global de périmètre

- Position : `x=1220, y=18, w=290, h=40`
- Type : slicer dropdown single-select
- Style :
  - fond blanc
  - border `#E1E8F0`
  - radius 999
  - texte Inter 12, `#1C2434`
- Valeurs :
  - France entière
  - Région
  - Agence
  - Centre d'affaires
  - Secteur
  - Mandataire
- Groupe : `SLICER_Global_Perimetre`
- Interaction : filtre toutes les pages.

### Field parameter FP_Axe_Organisation

Créer un field parameter pour les axes organisationnels.

Valeurs :
- Agence
- Centre d'affaires
- Région
- Secteur
- Mandataire
- Raison sociale

Utilisation :
- Header global si besoin
- Accueil
- Performance
- Affaires
- Réseau MIA

### Field parameter FP_Axe_Activite

Valeurs :
- Type de rendez-vous
- Canal de rendez-vous
- Statut rendez-vous
- Motif rendez-vous

Utilisation :
- Accueil
- Rendez-vous

### Field parameter FP_Metric_Performance

Valeurs :
- Volume d’affaires produites
- Volume d’affaires en instance
- Volume d’affaires commissionnées
- Montant moyen de rétrocommission
- Taux atteinte Budget N Volume

Utilisation :
- Page Performance
- Le ranking principal doit changer de mesure selon ce field parameter.

### Positions des slicers par page

| Page | Objet | X | Y | W | H | Style |
|---|---|---:|---:|---:|---:|---|
| Accueil | Période switch | 20 | 260 | 440 | 40 | Pills Jour/Semaine/Mois/Trimestre/Année |
| Accueil | FP_Axe_Organisation | 1060 | 260 | 210 | 40 | Dropdown / pill |
| Accueil | FP_Axe_Activite | 1290 | 260 | 230 | 40 | Dropdown / pill |
| Performance | FP_Metric_Performance | 20 | 260 | 950 | 40 | Boutons pills |
| Performance | FP_Axe_Organisation | 1240 | 260 | 280 | 40 | Dropdown |
| Affaires | FP_Axe_Affaires | 20 | 260 | 600 | 40 | Boutons pills |
| Affaires | Mois référence | 840 | 260 | 210 | 40 | Dropdown |
| Affaires | Mois comparé | 1060 | 260 | 210 | 40 | Dropdown |
| Affaires | Filtre org | 1280 | 260 | 240 | 40 | Dropdown |
| Réseau MIA | FP_Axe_Reseau | 20 | 260 | 520 | 40 | Boutons pills |
| Réseau MIA | Filtre org réseau | 1040 | 260 | 260 | 40 | Dropdown |
| Réseau MIA | Bouton tableau | 1320 | 260 | 200 | 40 | Bookmark button |
| RDV | FP_Axe_RDV | 20 | 260 | 720 | 40 | Boutons pills |
| RDV | Slicer type/canal/statut | 1240 | 260 | 280 | 40 | Dropdown |
| Alertes | Niveau alerte | 1180 | 260 | 340 | 40 | Chiclet / slicer |
| Glossaire | Recherche KPI | 1180 | 260 | 340 | 40 | Search dropdown |

### Style commun des slicers

- Fond : `#FFFFFF`
- Border : `#E1E8F0`
- Radius : 999
- Texte : Inter 11-12
- Header slicer masqué si possible
- Valeur sélectionnée en rouge `#D71920`
- Fond actif : `#D71920`
- Texte actif : blanc

---

## 3. Template Card KPI fusionnée

Créer chaque KPI card comme un groupe d’objets Power BI, pas comme une simple card native.

### Taille fixe

- Standard : `w=287, h=178`
- Gap entre cards : `16 px`
- Positions X pour une ligne de 5 cards :
  - Card 1 : `x=20`
  - Card 2 : `x=323`
  - Card 3 : `x=626`
  - Card 4 : `x=929`
  - Card 5 : `x=1232`

### Composition interne

| Objet interne | X relatif | Y relatif | W | H | Type |
|---|---:|---:|---:|---:|---|
| Fond carte | 0 | 0 | 287 | 178 | Rectangle shape |
| Label KPI | 18 | 16 | 175 | 30 | Text box |
| Icône | 225 | 16 | 44 | 44 | Shape + icon |
| Valeur KPI | 18 | 52 | 176 | 38 | Card visual |
| Badge Excel KPI | 18 | 92 | 118 | 20 | Shape + text |
| Badge BIM | 142 | 92 | 127 | 20 | Shape + text |
| Chip Vs N-1 | 18 | 118 | 80 | 24 | Shape + card/text |
| Chip Vs MTD-1 | 104 | 118 | 88 | 24 | Shape + card/text |
| Sparkline exercice | 202 | 112 | 67 | 33 | Line chart / sparkline |
| Libellé Budget | 18 | 148 | 251 | 10 | Text box |
| Track Budget | 18 | 162 | 251 | 8 | Rectangle |
| Fill Budget | 18 | 162 | dynamique | 8 | Shape/data bar |
| Marqueur 100% | 269 | 158 | 3 | 16 | Rectangle |
| Tooltip invisible | 0 | 0 | 287 | 178 | Tooltip target |
| Groupe final | 0 | 0 | 287 | 178 | Group |

### Mise en forme interne

- Fond carte :
  - Fill : `#FFFFFF`
  - Border : `#E1E8F0`
  - Radius : 22
  - Shadow : douce
- Label KPI :
  - Inter 11
  - uppercase
  - bold
  - couleur `#667085`
- Valeur KPI :
  - Inter 29
  - black / bold
  - couleur `#1C2434`
- Icône :
  - Shape : carré arrondi 14
  - Fill : `#EAF3FF`
  - Icone : `#0A4E97`
- Badge Excel :
  - Fill : `#EAF3FF`
  - Texte : `#0A4E97`
  - Font : Inter 8 bold
- Badge BIM :
  - BIM OK : fill `#EAF7EF`, texte `#198754`
  - BIM partiel : fill `#FFF3E8`, texte `#E67E22`
  - BIM absent : fill `#FFF1F2`, texte `#D71920`
- Chips :
  - Positif : fill `#EAF7EF`, texte `#198754`
  - Négatif : fill `#FFF1F2`, texte `#D71920`
  - Neutre : fill `#EAF3FF`, texte `#0A4E97`
- Sparkline :
  - aucune légende
  - aucun axe
  - line stroke 2 px
  - couleur conditionnelle selon tendance
- Budget bar :
  - track : `#E8EEF5`
  - fill :
    - >= 100% : `#198754`
    - 85% à 99% : `#E67E22`
    - < 85% : `#D71920`
  - marker 100% : `#D71920`

### Groupement Selection pane

Nommer chaque carte :

`G_KPI_<Page>_<Numero>_<LibelleCourt>`

Exemples :
- `G_KPI_Accueil_01_VolumeAffairesProduites`
- `G_KPI_Accueil_05_RDVRealises`
- `G_KPI_Reseau_02_MIAActifs`

À l’intérieur :
- `BG_Card`
- `TXT_Label`
- `ICON_KPI`
- `VIS_KPI_Value`
- `BADGE_Excel`
- `BADGE_BIM`
- `CHIP_Vs_N1`
- `CHIP_Vs_MTD1`
- `SPARK_KPI`
- `TXT_Budget_Label`
- `BG_Budget_Track`
- `FILL_Budget`
- `MARKER_Budget_100`
- `TOOLTIP_KPI`

---

## 4. Types de visuels et mise en forme

### KPI cards

Type : groupe de shapes + card native + line chart sparkline + bar budget.  
Ne pas utiliser une simple Card Power BI seule.

### Line charts

- Background transparent
- Titre via text box externe, pas titre natif
- Gridlines très légères ou désactivées
- Axe X : Inter 11 `#667085`
- Axe Y : Inter 10 `#667085`
- Légende en bas, Inter 12
- Couleurs :
  - série principale : `#0A4E97`
  - comparaison N-1 : `#D71920`
  - MTD-1 / autre : `#E67E22`

### Bar charts horizontaux

- Fond transparent sur shape card
- Catégorie : Inter 12 bold `#1C2434`
- Valeur : Inter 11 bold
- Couleurs conditionnelles :
  - top / positif : `#0A4E97` ou `#198754`
  - vigilance : `#E67E22`
  - retrait : `#D71920`
- Track gris si construit en composant custom : `#E8EEF5`

### Donut charts

- Taille visuel : 178 à 220 px selon page
- Inner radius : 55-60 %
- Légende externe en 2 colonnes
- Labels internes masqués si surcharge
- Tooltip métier activé

### Tables / matrices

- Header :
  - uppercase
  - Inter 10-11
  - `#667085`
- Rows :
  - fond `#F7F9FC`
  - border `#E1E8F0`
  - texte `#1C2434`
- Désactiver totals sauf besoin métier
- Prévoir table derrière shape arrondie si Power BI ne permet pas le radius.

### Carte France

- Préférer Shape Map ou Azure Map si coordonnées disponibles.
- Sinon utiliser une image France en fond + bulles de sélection par agence.
- Bulles :
  - agence standard : `#0A4E97`
  - agence sélectionnée : `#D71920`
- Interaction :
  - clic agence filtre les mini KPI de focus et les tableaux.

---

## 5. Répartition des cards par page

### Accueil

- KPI row : `x=20, y=330, w=1500, h=178`
- 5 cards :
  1. Volume affaires produites — Excel G.3 — BIM absent
  2. Volume affaires en instance — Excel à confirmer — BIM absent
  3. Volume affaires commissionnées — Excel à confirmer — BIM absent
  4. Montant moyen rétrocommission — BIM OK
  5. Nombre RDV réalisés — Excel G.15 — BIM OK

### Performance

- KPI row : `x=20, y=330, w=1500, h=178`
- 5 cards :
  1. Volume affaires produites — G.3
  2. Volume affaires en instance — à confirmer
  3. Volume affaires commissionnées — à confirmer
  4. Montant moyen rétrocommission — BIM OK
  5. Taux atteinte Budget N Volume — calcul G.3 / G.5

### Affaires

- KPI row : `x=20, y=330, w=1500, h=178`
- 5 cards :
  1. Nombre affaires produites — G.2
  2. Volume affaires produites — G.3
  3. Volume affaires en instance — à confirmer
  4. Volume affaires commissionnées — à confirmer
  5. Montant moyen rétrocommission — BIM OK

### Réseau MIA

- KPI row : `x=20, y=330, w=1500, h=178`
- 5 cards :
  1. Nombre MIA ORIASés — à confirmer
  2. Nombre MIA actifs — G.6 — BIM OK
  3. Nombre MIA productifs — G.8 — BIM absent
  4. Nombre total MIA commissionnés — G.10 — BIM OK
  5. Montant moyen rétrocommission — BIM OK

### Rendez-vous

- KPI row : `x=20, y=330, w=1500, h=178`
- 5 cards :
  1. Nombre RDV réalisés — G.15 — BIM OK
  2. Nombre RDV prévus — G.14 — BIM OK
  3. Nombre RDV confirmés — à formaliser
  4. Taux réalisation RDV — G.13 — BIM OK
  5. Taux RDV Visio / Domicile — G.18/G.19 — BIM OK

### Alertes

- KPI row : `x=20, y=330, w=1500, h=178`
- 5 cards :
  1. Nombre alertes critiques — fact_alertes à créer
  2. Nombre alertes hautes — fact_alertes à créer
  3. Nombre alertes moyennes — fact_alertes à créer
  4. Nombre alertes ouvertes — fact_alertes à créer
  5. Couleur alerte — règle à créer

---

## 6. Bookmarks

Créer les bookmarks :

1. `BM_Reseau_Table_Fermee`
   - Groupe `G06_Table_Detail_Reseau` masqué
   - Bouton texte = “Afficher le tableau”

2. `BM_Reseau_Table_Ouverte`
   - Groupe `G06_Table_Detail_Reseau` visible
   - Bouton texte = “Masquer le tableau”

Créer aussi des boutons de navigation standard pour chaque page.

---

## 7. Tooltips métier

Chaque KPI card doit avoir un tooltip affichant :

- Libellé KPI
- Index Excel
- Définition métier
- Formule / règle de calcul
- Statut BIM
- Mesure Power BI existante ou à créer
- Table source attendue
- Seuil d’alerte si présent

Tooltip recommandé : page tooltip dédiée `Tooltip_KPI`.

---

## 8. Règles conditionnelles

### Couleur variation Vs N-1 et Vs MTD-1

- Variation > 0 :
  - fond `#EAF7EF`
  - texte `#198754`
- Variation = 0 ou blank :
  - fond `#EAF3FF`
  - texte `#0A4E97`
- Variation < 0 :
  - fond `#FFF1F2`
  - texte `#D71920`

### Couleur budget

- Taux >= 100% :
  - `#198754`
- Taux >= 85% et < 100% :
  - `#E67E22`
- Taux < 85% :
  - `#D71920`

### Couleur statut BIM

- BIM OK :
  - `#198754`
- BIM partiel :
  - `#E67E22`
- BIM absent :
  - `#D71920`

