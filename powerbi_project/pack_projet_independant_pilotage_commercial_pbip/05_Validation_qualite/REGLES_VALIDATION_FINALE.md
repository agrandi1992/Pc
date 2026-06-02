# Règles de validation finale

## Chevauchement
Exécuter `check_powerbi_overlap.py` sur le projet PBIP / PBIR si la structure est accessible.

Tout chevauchement non autorisé doit être corrigé.

Chevauchements autorisés uniquement :
- fond de carte sous les éléments de la carte ;
- marqueur budget sur barre budget ;
- bouton / shape overlay volontaire ;
- état bookmark masqué ;
- tooltip invisible.

## Modèle
- Le rapport doit s’ouvrir sans erreur.
- Toutes les mesures doivent calculer.
- Les mesures absentes doivent être clairement marquées comme à créer.

## Visuel
- Vérifier page par page en capture PNG.
- Comparer aux images de référence du dossier `02_References_visuelles`.
- Vérifier que chaque card affiche source Excel + statut BIM.

## Navigation
- Tester tous les boutons.
- Tester le bookmark tableau réseau ouvert / fermé.

## Slicers
- Tester les field parameters.
- Tester Mois référence / Mois comparé.
