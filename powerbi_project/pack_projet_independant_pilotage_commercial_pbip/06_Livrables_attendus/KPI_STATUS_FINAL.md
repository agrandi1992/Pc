# KPI_STATUS_FINAL — Pilotage Commercial PBIP
**Date :** 2026-06-02 | **Version :** 1.0.0

Audit complet de tous les indicateurs : source Excel, mesure BIM, statut de disponibilité.

---

## Tableau de statut KPI

| KPI | Libellé | Pages | Source Excel | Mesure BIM / Table | Statut | Table requise | Note |
|-----|---------|-------|--------------|-------------------|--------|---------------|------|
| G.1 | Nombre de ventes | Performance | G.1 | `_Indicateurs[Nombre ventes]` | BIM CRÉÉ (placeholder) | `fact_affaires` | Nécessite fact_affaires réelle |
| G.2 | Nombre d'affaires produites | Affaires | G.2 | `_Indicateurs[Nombre affaires produites]` | BIM CRÉÉ (placeholder) | `fact_affaires` | Nécessite fact_affaires réelle |
| G.3 | Volume d'affaires produites | Accueil, Performance, Affaires | G.3 | `_Indicateurs[Volume affaires produites]` | BIM CRÉÉ (placeholder) | `fact_affaires` | Nécessite fact_affaires réelle |
| G.4 | Budget affaires en nombre | Affaires | G.4 | `_Indicateurs[Budget affaires en nombre]` | BIM CRÉÉ (placeholder) | `budget_affaires` | Nécessite budget_affaires réelle |
| G.5 | Budget affaires en euro | Affaires | G.5 | `_Indicateurs[Budget affaires en euro]` | BIM CRÉÉ (placeholder) | `budget_affaires` | Nécessite budget_affaires réelle |
| G.6 | Nombre mandataires actifs | Réseau, Accueil | G.6 | `_Indicateurs[Nombre mandataires actifs]` | **BIM OK** | dim_mandataire | Disponible — mesure originale |
| G.7 | Nombre mandataires inactifs | Réseau | G.7 | `_Indicateurs[Nombre mandataires inactifs]` | **BIM OK** | dim_mandataire | Disponible — mesure originale |
| G.8 | Nombre mandataires productifs | Réseau | G.8 | `_Indicateurs[Nombre mandataires productifs]` | BIM CRÉÉ (placeholder) | `fact_affaires` | Nécessite fact_affaires réelle |
| G.9 | Nombre mandataires non productifs | Réseau | G.9 | `_Indicateurs[Nombre mandataires non productifs]` | BIM CRÉÉ (dérivé) | `fact_affaires` | Dérivable de G.6 - G.8 |
| G.10 | Nombre mandataires rétrocommissionnés | Réseau | G.10 | `_Indicateurs[Nombre mandataires rétrocommissionnés]` | **BIM OK** | fact_activite_mandataire | Disponible — mesure originale |
| G.11 | Nombre mandataires non rétrocommissionnés | Réseau | G.11 | `_Indicateurs[Nombre mandataires non rétrocommissionnés]` | BIM CRÉÉ (dérivé) | dim_mandataire | Dérivable de G.6 - G.10 |
| G.12 | RDV hebdomadaire moyen | RDV | G.12 | `_Indicateurs[Nombre RDV hebdomadaire moyen]` | BIM CRÉÉ | dim_date, fact_rdv | Calculable depuis données existantes |
| G.13 | Taux réalisation RDV | Accueil, RDV, Alertes | G.13 | `_Indicateurs[Taux réalisation de rendez-vous]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.14 | Nombre RDV prévus | RDV | G.14 | `_Indicateurs[Nombre rendez-vous prévus]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.15 | Nombre RDV réalisés | RDV | G.15 | `_Indicateurs[Nombre rendez-vous réalisés]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.16 | Nombre RDV confirmés | RDV | G.16 | À créer | À CRÉER | fact_rendez_vous_client | Dérivable selon statut RDV |
| G.17 | Taux RDV confirmés | RDV | G.17 | À créer | À CRÉER | fact_rendez_vous_client | DIVIDE G.16/G.14 |
| G.18 | Taux RDV visioconférence | RDV | G.18 | `_Indicateurs[Taux rendez vous réalisés en visioconférence]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.19 | Taux RDV domicile | RDV | G.19 | `_Indicateurs[Taux rendez-vous faits à domicile]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.20 | Nombre RDV visio | RDV | G.20 | `_Indicateurs[Nombre rendez-vous réalisés en visioconférence]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.21 | Nombre RDV domicile | RDV | G.21 | `_Indicateurs[Nombre rendez-vous réalisés à domicile]` | **BIM OK** | fact_rendez_vous_client | Disponible — mesure originale |
| G.22 | Montant moyen rétrocommission | Réseau, Accueil | G.22 | `_Indicateurs[Montant moyen de rétrocommission]` | **BIM OK** | fact_activite_mandataire | Disponible — mesure originale |
| G.23 | Montant rétrocommission total | Réseau | G.23 | `_Indicateurs[Montant rétrocommission]` | **BIM OK** | fact_activite_mandataire | Disponible — mesure originale |
| G.24 | Taux atteinte budget volume | Affaires | G.24 | `_Indicateurs[Taux atteinte Budget N Volume]` | BIM CRÉÉ (placeholder) | `fact_affaires`, `budget_affaires` | Nécessite les deux tables |
| G.25 | Variation volume vs N-1 | Accueil, Performance | G.25 | `_Indicateurs[Variation vs N-1 Volume Affaires (%)]` | BIM CRÉÉ (placeholder) | `fact_affaires` | Nécessite fact_affaires réelle |
| G.26 | Variation volume vs MTD-1 | Performance | G.26 | `_Indicateurs[Variation vs MTD-1 Volume Affaires (%)]` | BIM CRÉÉ (placeholder) | `fact_affaires` | Nécessite fact_affaires réelle |
| ALERTE_CRIT | Nombre Alertes Critiques | Alertes | À créer | `_Indicateurs[Nombre Alertes Critiques]` | BIM CRÉÉ (placeholder) | `fact_alertes` | Nécessite fact_alertes réelle |
| ALERTE_HAUT | Nombre Alertes Hautes | Alertes | À créer | `_Indicateurs[Nombre Alertes Hautes]` | BIM CRÉÉ (placeholder) | `fact_alertes` | Nécessite fact_alertes réelle |
| ALERTE_MOY | Nombre Alertes Moyennes | Alertes | À créer | `_Indicateurs[Nombre Alertes Moyennes]` | BIM CRÉÉ (placeholder) | `fact_alertes` | Nécessite fact_alertes réelle |
| ALERTE_OUV | Nombre Alertes Ouvertes | Alertes | À créer | `_Indicateurs[Nombre Alertes Ouvertes]` | BIM CRÉÉ (placeholder) | `fact_alertes` | Nécessite fact_alertes réelle |

---

## Synthèse par statut

| Statut | Nb KPI | Détail |
|--------|--------|--------|
| **BIM OK** (disponible) | 11 | G.6, G.7, G.10, G.13, G.14, G.15, G.18, G.19, G.20, G.21, G.22, G.23 |
| **BIM CRÉÉ placeholder** | 16 | G.1-G.5, G.8-G.9, G.11-G.12, G.24-G.26, ALERTE×4 |
| **À CRÉER** | 2 | G.16, G.17 (statut RDV confirmés) |
| **TOTAL** | 29 | — |

---

## Indicateurs supplémentaires créés (non dans spec Excel initiale)

Ces mesures ont été ajoutées pour enrichir l'analyse et supporter les alertes :

| Mesure | Folder | Description |
|--------|--------|-------------|
| `Niveau Alerte Volume` | Alertes | Qualification CRITIQUE/HAUTE/MOYENNE/CONFORME |
| `Couleur Alerte Volume` | Alertes | Hex couleur pour formatage conditionnel |
| `Niveau Alerte RDV` | Alertes | Qualification basée sur taux réalisation |
| `Couleur Alerte RDV` | Alertes | Hex couleur pour formatage conditionnel |
| `Niveau Alerte Réseau` | Alertes | Qualification basée sur taux actifs |
| `Couleur Alerte Réseau` | Alertes | Hex couleur pour formatage conditionnel |
| `Recommandation Volume` | Alertes | Texte de recommandation adaptatif |
| `CF Variation Texte Volume` | CF | Couleur texte variation N-1 |
| `CF Budget Fill Volume` | CF | Couleur remplissage taux budget |
| `Libellé Variation Volume vs N-1` | Affichage | Texte ▲/▼ formaté |
| `Libellé Variation Volume vs MTD-1` | Affichage | Texte ▲/▼ formaté |
| `Nombre MIA oriasés` | Réseau | Mandataires avec numéro ORIAS |
| `Taux mandataires actifs` | Réseau | % actifs parmi actifs+inactifs |

---

## Tables — Plan d'intégration et cibles de déploiement

### `fact_alertes` — OPÉRATIONNELLE ✅
**Statut :** Table calculée DAX générée à chaque refresh depuis les données existantes.  
**Conditions implémentées :** G.13 (taux RDV < 66% → CRITIQUE), G.14 (prévus/semaine), G.15 (réalisés/semaine), G.18 (taux visio > 33% → HAUTE).  
Aucune action requise — fonctionne avec les données actuelles.

---

### `fact_affaires` — CIBLE : Microsoft Fabric 🔵
**Statut actuel :** DATATABLE vide (structure prête, 13 colonnes).  
**Cible de déploiement :** Fabric Lakehouse (Delta Parquet via OneLake) ou Fabric Warehouse.  
**Développement :** Prévu ultérieurement — la table sera développée et publiée dans un espace de travail Fabric.

**Colonnes :** affaire_id, date_affaire, mandataire_id, agence_id, produit_id, assureur_id, statut_affaire, montant_affaire, montant_retrocommission, nombre_ventes_partage, flag_produite, flag_instance, flag_commissionnee

**Le jour J (connexion Fabric) :**
1. Dans Power BI Desktop → Transform Data → remplacer la table calculée par une source Fabric (OneLake ou SQL Endpoint du Warehouse)
2. Changer `mode` de `calculated` vers `import` (ou `directLake` si le workspace Fabric le supporte)
3. Créer les relations :
   - `fact_affaires[mandataire_id]` → `dim_mandataire[mandataire_id]`
   - `fact_affaires[agence_id]` → `dim_agence[agence_id]`
   - `fact_affaires[date_affaire]` → `dim_date[Date]`
4. Republier vers le workspace Fabric

---

### `budget_affaires` — CIBLE : Excel 📄
**Statut actuel :** DATATABLE vide (structure prête, 8 colonnes).  
**Cible de déploiement :** Fichier Excel — import Power Query.  
**Disponibilité :** Fichier source non disponible à ce jour.

**Colonnes attendues dans l'Excel :** budget_id, date_budget, agence_id, produit_id, assureur_id, budget_affaires_nombre, budget_affaires_euro, budget_retrocommission

**Quand le fichier Excel est disponible :**
1. Dans Power BI Desktop → Get Data → Excel → sélectionner le fichier
2. Mapper les colonnes ci-dessus (renommer si nécessaire via Power Query)
3. Supprimer la table calculée vide et la remplacer par la requête Power Query
4. Créer les relations :
   - `budget_affaires[agence_id]` → `dim_agence[agence_id]`
   - `budget_affaires[date_budget]` → `dim_date[Date]`
5. Republier
