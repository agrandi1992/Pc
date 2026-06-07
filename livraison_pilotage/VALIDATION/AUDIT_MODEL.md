# AUDIT_MODEL — Pilotage Commercial v5
*Généré le 2025-06-05 — Modèle Import (local test)*

## Synthèse
| Élément       | Valeur |
|---------------|--------|
| Tables        | 27 |
| Relations     | 22 |
| Mesures       | 77 |
| Mode          | Import (données fictives) |
| Canvas rapport| 1440×900 |
| Pages         | 8 |

## Tables gold
| Table | Colonnes | Mesures | Mode |
|-------|----------|---------|------|
| dim_date | 12 | 0 | import |
| DateTableTemplate_40f8e67e-c9f0-4e13-ad4f-6e840fdbf357 | 7 | 0 | import |
| LocalDateTable_608a5c4d-d6d2-474e-a494-6c6b82f0fc3c | 7 | 0 | import |
| fact_affectation_mandataire | 4 | 0 | import |
| glossaire_indicateurs | 3 | 0 | import |
| dim_type_rendez_vous_client | 2 | 0 | import |
| dim_niveau_etude | 3 | 0 | import |
| dim_motif_depart_formation | 2 | 0 | import |
| dim_charge_developpement_reseau | 3 | 0 | import |
| dim_type_canal | 2 | 0 | import |
| dim_candidat | 17 | 0 | import |
| dim_agence | 6 | 0 | import |
| fact_parcours_candidat | 5 | 0 | import |
| fact_activite_mandataire | 4 | 1 | import |
| _Indicateurs | 1 | 75 | import |
| bridge_rendez_vous_mandataire | 3 | 0 | import |
| fact_rendez_vous_client | 12 | 1 | import |
| dim_mandataire | 9 | 0 | import |
| Periode_Affichage | 2 | 0 | ? |
| FP_Axe_Organisation | 3 | 0 | ? |
| FP_Axe_Reseau | 3 | 0 | ? |
| FP_Axe_RDV | 3 | 0 | ? |
| Mois_Reference | 3 | 0 | ? |
| Mois_Compare | 3 | 0 | ? |
| fact_affaire | 13 | 0 | import |
| dim_produit | 3 | 0 | import |
| fact_alertes | 8 | 0 | import |

## Relations
| De | Vers | Active |
|----|------|--------|
| dim_date[Date] | LocalDateTable_608a5c4d-d6d2-474e-a494-6c6b82f0fc3c[Date] | Oui |
| fact_parcours_candidat[candidat_id] | dim_candidat[candidat_id] | Oui |
| dim_candidat[charge_developpement_id] | dim_charge_developpement_reseau[charge_developpement_id] | Oui |
| dim_candidat[niveau_etude_id] | dim_niveau_etude[niveau_etude_id] | Oui |
| dim_candidat[type_canal_id] | dim_type_canal[type_canal_id] | Oui |
| fact_affectation_mandataire[mandataire_id] | dim_charge_developpement_reseau[charge_developpement_id] | Oui |
| fact_affectation_mandataire[agence_id] | dim_agence[agence_id] | Oui |
| fact_parcours_candidat[date_etape_parcours] | dim_date[Date] | Oui |
| fact_affectation_mandataire[date_entree] | dim_date[Date] | Oui |
| fact_parcours_candidat[motif_depart_formation_id] | dim_motif_depart_formation[motif_depart_formation_id] | Oui |
| fact_activite_mandataire[agence_id] | dim_agence[agence_id] | Oui |
| fact_activite_mandataire[date_connexion] | dim_date[Date] | Oui |
| dim_candidat[agence_id] | dim_agence[agence_id] | Oui |
| fact_rendez_vous_client[date_rendez_vous_client] | dim_date[Date] | Oui |
| fact_rendez_vous_client[type_rendez_vous_id] | dim_type_rendez_vous_client[type_rendez_vous_client_id] | Oui |
| bridge_rendez_vous_mandataire[mandataire_id] | dim_mandataire[mandataire_id] | Oui |
| bridge_rendez_vous_mandataire[rendez_vous_id] | fact_rendez_vous_client[rendez_vous_id] | Oui |
| fact_activite_mandataire[mandataire_id] | dim_mandataire[mandataire_id] | Oui |
| fact_affaire[date_saisie_administrative] | dim_date[Date] | Oui |
| fact_affaire[produit_id] | dim_produit[produit_id] | Oui |
| fact_alertes[mandataire_id] | dim_mandataire[mandataire_id] | Oui |
| fact_affaire[agence_id] | dim_agence[agence_id] | Oui |

## Mesures
| Table | Mesure |
|-------|--------|
| fact_activite_mandataire | Flag mandataire actif |
| _Indicateurs | Nombre rendez-vous prévus |
| _Indicateurs | Nombre rendez-vous réalisés |
| _Indicateurs | Taux réalisation de rendez-vous |
| _Indicateurs | Nombre mandataires actifs |
| _Indicateurs | Nombre mandataires inactifs |
| _Indicateurs | Nombre entretiens réalisés |
| _Indicateurs | Nombre journées découverte réalisées |
| _Indicateurs | Nombre inscrits formation initiale |
| _Indicateurs | Nombre mandataires ayant passé l'examen |
| _Indicateurs | Nombre mandataires ayant réussi l'examen |
| _Indicateurs | Année présence mandataire dans le groupe |
| _Indicateurs | Année présence mandataire dans agence |
| _Indicateurs | Nombre mandataires rétrocommissionnés |
| _Indicateurs | Montant moyen de rétrocommission |
| _Indicateurs | Moyenne Taux Réalisation de rendez-vous |
| _Indicateurs | Ecart Taux Réalisation |
| _Indicateurs | Couleur Ecart Taux Réalisation |
| _Indicateurs | Moyenne année présence mandataire dans le groupe |
| _Indicateurs | Nombre candidats |
| _Indicateurs | Nombre candidats intégrés |
| _Indicateurs | Taux intégration candidats |
| _Indicateurs | Moyenne age candidats |
| _Indicateurs | Taux de succès à l'examen (%) |
| _Indicateurs | Nombre rendez-vous réalisés en visioconférence |
| _Indicateurs | Nombre rendez-vous réalisés à domicile |
| _Indicateurs | Taux rendez vous réalisés en visioconférence |
| _Indicateurs | Taux rendez-vous faits à domicile |
| _Indicateurs | Nombre RDV prévus (par type mandataire) |
| _Indicateurs | Nombre RDV réalisés (par type mandataire) |
| _Indicateurs | Taux réalisation RDV (par type mandataire) |
| _Indicateurs | Nombre RDV prévus (agence) |
| _Indicateurs | Nombre RDV réalisés (agence) |
| _Indicateurs | Nombre mandataires rétrocommissionnés N-1 |
| _Indicateurs | Évolution mandataires rétro vs N-1 (%) |
| _Indicateurs | Montant rétrocommission |
| _Indicateurs | Nombre MIA oriasés |
| _Indicateurs | Nombre mandataires non rétrocommissionnés |
| _Indicateurs | Taux mandataires actifs |
| _Indicateurs | Nombre RDV hebdomadaire moyen |
| _Indicateurs | Niveau Alerte Volume |
| _Indicateurs | Couleur Alerte Volume |
| _Indicateurs | Niveau Alerte RDV |
| _Indicateurs | Couleur Alerte RDV |
| _Indicateurs | Niveau Alerte Réseau |
| _Indicateurs | Couleur Alerte Réseau |
| _Indicateurs | Nombre RDV confirmés |
| _Indicateurs | Taux RDV confirmés |
| _Indicateurs | Priorité Alerte Maximale |
| _Indicateurs | Nombre Alertes Critiques |
| _Indicateurs | Nombre Alertes Hautes |
| _Indicateurs | Nombre Alertes Moyennes |
| _Indicateurs | Nombre Alertes Ouvertes |
| _Indicateurs | Recommandation Alerte RDV |
| _Indicateurs | Recommandation Alerte Volume |
| _Indicateurs | Nombre ventes |
| _Indicateurs | Nombre affaires produites |
| _Indicateurs | Volume affaires produites |
| _Indicateurs | Nombre affaires en instance |
| _Indicateurs | Volume affaires en instance |
| _Indicateurs | Nombre affaires commissionnées |
| _Indicateurs | Volume affaires commissionnées |
| _Indicateurs | Budget affaires en nombre |
| _Indicateurs | Budget affaires en euro |
| _Indicateurs | Taux atteinte Budget N Volume |
| _Indicateurs | Volume affaires produites N-1 |
| _Indicateurs | Variation vs N-1 Volume Affaires (%) |
| _Indicateurs | Volume affaires produites MTD-1 |
| _Indicateurs | Variation vs MTD-1 Volume Affaires (%) |
| _Indicateurs | Nombre mandataires productifs |
| _Indicateurs | Nombre mandataires non productifs |
| _Indicateurs | CF Variation Texte Volume |
| _Indicateurs | CF Budget Fill Volume |
| _Indicateurs | Libellé Variation Volume vs N-1 |
| _Indicateurs | Libellé Variation Volume vs MTD-1 |
| _Indicateurs | Recommandation Volume |
| fact_rendez_vous_client | Flag rétrocommissionné |
