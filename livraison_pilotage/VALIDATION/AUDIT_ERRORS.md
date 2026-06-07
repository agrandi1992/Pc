# AUDIT_ERRORS — Journal des corrections
*Généré le 2025-06-05*

## Historique des erreurs résolues (v1→v5)

| Version | Erreur | Cause | Résolution | Statut |
|---------|--------|-------|------------|--------|
| v1 | Chemin trop long Windows (>260 car) | Racine ZIP trop profonde | Racine renommée `PCL/` | ✅ Résolu |
| v2 | Réseau MIA: "Désolé, erreur lors de la récupération" | 6 mesures manquantes dans dim_agence | Ajout mesures dans `_Indicateurs`, mise à jour prototypeQuery | ✅ Résolu |
| v2 | KPI cards vides après actualisation | layout.y=355 vs vc.y=328 (décalage 27px) | Synchronisation positions VC/layout, hauteur card 42→68px | ✅ Résolu |
| v3 | "Measure du même nom existe déjà" | 6 mesures en doublon entre dim_agence et _Indicateurs | Suppression doublons, redirection prototypeQuery | ✅ Résolu |
| v3 | fact_alertes manquante | Table non créée | Ajout fact_alertes avec 8 lignes fictives | ✅ Résolu |
| v3 | Pas de relation fact_affaire→dim_agence | Column agence_id manquante | Ajout agence_id + relation BIM | ✅ Résolu |
| v5 | dim_mandataire.statut_mandataire manquant | Colonne absente du schéma fictif | Ajout colonne M expression + définition BIM | ✅ Résolu |
| v5 | glossaire_indicateurs.nom_indicateur incorrect | Nom de colonne inexact | Correction → `indicateur` / `perimetre` | ✅ Résolu |

## État v5 — Zéro erreur connue

| Critère | Résultat |
|---------|----------|
| JSON valide | ✅ |
| Toutes mesures référencées existent | ✅ |
| Toutes colonnes référencées existent | ✅ |
| Aucun nom de mesure en doublon | ✅ |
| Z-index cohérents | ✅ |
| Pages non vides | ✅ (8/8) |
| Visuels dynamiques liés | ✅ (66 visuels) |
| Schéma BIM cohérent | ✅ |
