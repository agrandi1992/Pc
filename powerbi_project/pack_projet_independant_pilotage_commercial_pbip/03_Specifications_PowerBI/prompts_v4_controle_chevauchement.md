# Ajout v4 — Contrôle de chevauchement Power BI

## Objectif
Inclure une étape obligatoire de vérification des chevauchements entre tous les éléments du rapport Power BI : header, navigation, slicers, field parameters, cards fusionnées, graphiques, tableaux, jauges, boutons et objets internes de chaque card.

Le développeur doit considérer chaque objet comme un rectangle défini par :

- Page
- Groupe
- Nom objet
- Type objet / type de visuel
- X
- Y
- Largeur W
- Hauteur H
- Right = X + W
- Bottom = Y + H
- ZIndex
- Politique d'overlap

## Règle de contrôle
Deux objets A et B se chevauchent si :

```text
OverlapWidth  = MAX(0, MIN(RightA, RightB) - MAX(XA, XB))
OverlapHeight = MAX(0, MIN(BottomA, BottomB) - MAX(YA, YB))
OverlapArea   = OverlapWidth * OverlapHeight
```

Si `OverlapArea > 0`, alors il y a chevauchement.

## Exceptions autorisées
Le chevauchement est autorisé uniquement si l’objet est explicitement prévu pour être superposé :

1. Fond de carte / background derrière ses enfants.
2. Marqueur Budget positionné sur la barre BudgetTrack.
3. Tooltip invisible ou overlay volontaire.
4. Objet masqué par bookmark dans un état exclusif.

Tout autre chevauchement doit être corrigé.

## Marge minimale
Même sans chevauchement, imposer une marge minimale de 8 px entre :

- deux cards voisines ;
- une card et un graphique ;
- une zone de filtre et une zone KPI ;
- un tableau et un graphique ;
- un bouton et un slicer.

Si l’écart est inférieur à 8 px, signaler un avertissement : `WARNING marge insuffisante`.

## Contrôle des cards fusionnées
Chaque card KPI doit être contrôlée comme un groupe composé d’objets internes :

1. BG_Card
2. TXT_Label
3. TXT_Value
4. ICON_Background
5. ICON_Text
6. CHIP_Vs_N1
7. CHIP_Vs_MTD1
8. SPARKLINE_Exercice
9. BADGE_Excel_Source
10. BADGE_BIM_Status
11. TXT_Budget_Label
12. BAR_Budget_Track
13. BAR_Budget_Fill
14. MARKER_Budget
15. Tooltip invisible éventuel
16. Groupe parent Card_KPI_xx

Le fond peut couvrir toute la card. Les autres objets ne doivent pas se chevaucher entre eux.

## Prompt technique à ajouter au cahier de build

```text
Avant livraison, contrôler toutes les coordonnées X/Y/W/H des visuels Power BI. Reporter les objets dans l’onglet 08_Controle_Overlap du fichier de spécification. L’onglet 09_Check_Overlap doit retourner uniquement “OK aucun chevauchement”. Toute ligne “ERREUR chevauchement” doit être corrigée par déplacement, réduction de taille, masquage par bookmark, ou changement de ZIndex si l’overlay est volontaire et documenté.

Pour les cards fusionnées, vérifier séparément le groupe parent et les objets internes : fond, valeur KPI, chips N-1/MTD-1, sparkline, barre budget, badges source Excel/BIM. Le budget marker peut chevaucher la barre budget ; tous les autres croisements sont interdits.

Les slicers, field parameters et boutons de navigation doivent avoir des zones réservées fixes. Aucun slicer ne doit recouvrir le title zone, les KPI cards ou les autres slicers. Le menu de navigation doit rester dans le header global avec une marge minimale de 8 px entre chaque bouton.
```

## Utilisation PBIP / PBIR
Si le rapport existe en format PBIP/PBIR, exécuter le script `check_powerbi_overlap.py` sur le dossier du rapport :

```bash
python check_powerbi_overlap.py /chemin/vers/rapport.pbip
```

Le script parcourt les JSON du rapport et remonte les chevauchements détectés à partir des propriétés `x`, `y`, `width`, `height`.
