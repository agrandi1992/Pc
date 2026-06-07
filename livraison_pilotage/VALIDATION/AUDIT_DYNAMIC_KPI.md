# AUDIT_DYNAMIC_KPI — Validation des KPIs Dynamiques
*Généré le 2025-06-05*

## Règles de validation
Un KPI est considéré dynamique si :
1. Le visuel est de type `card`, `barChart`, `lineChart`, `donutChart`, `tableEx` ou `slicer`
2. Il possède un `prototypeQuery` avec au moins une entrée `Select`
3. La mesure/colonne référencée existe dans le modèle BIM

## Résultats par page

### Accueil (5 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| ACC_KPI1_VAL | card | Volume affaires produites | ✅ OK |
| ACC_KPI1_VAR | card | Variation vs N-1 Volume Affaires (%) | ✅ OK |
| ACC_KPI2_VAL | card | Taux réalisation de rendez-vous | ✅ OK |
| ACC_KPI3_VAL | card | Nombre mandataires actifs | ✅ OK |
| ACC_KPI4_VAL | card | Nombre Alertes Ouvertes | ✅ OK |

### Performance (10 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| PERF_KPI1_VAL | card | Volume affaires produites | ✅ OK |
| PERF_KPI1_VAR | card | Variation vs N-1 Volume Affaires (%) | ✅ OK |
| PERF_KPI2_VAL | card | Nombre affaires produites | ✅ OK |
| PERF_KPI3_VAL | card | Taux atteinte Budget N Volume | ✅ OK |
| PERF_KPI4_VAL | card | Variation vs MTD-1 Volume Affaires (%) | ✅ OK |
| PERF_CHART_VOL_AGENCE | barChart | Volume affaires produites | ✅ OK |
| PERF_CHART_EVOL | lineChart | Volume affaires produites | ✅ OK |
| PERF_CHART_PRODUIT | clusteredColumnChart | Volume affaires produites | ✅ OK |

### Affaires (10 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| AFF_KPI1_VAL | card | Nombre affaires produites | ✅ OK |
| AFF_KPI2_VAL | card | Volume affaires produites | ✅ OK |
| AFF_KPI2_VAR | card | Variation vs N-1 Volume Affaires (%) | ✅ OK |
| AFF_KPI3_VAL | card | Nombre affaires en instance | ✅ OK |
| AFF_KPI4_VAL | card | Nombre affaires commissionnées | ✅ OK |
| AFF_CHART_PRODUIT | barChart | Volume affaires produites | ✅ OK |
| AFF_CHART_BUDGET | clusteredColumnChart | Taux atteinte Budget N Volume | ✅ OK |
| AFF_TBL_AFFAIRES | tableEx | Nombre affaires produites, Volume affaires produites... | ✅ OK |

### Réseau MIA (10 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| RES_KPI1_VAL | card | Nombre mandataires actifs | ✅ OK |
| RES_KPI2_VAL | card | Nombre mandataires rétrocommissionnés | ✅ OK |
| RES_KPI3_VAL | card | Nombre MIA oriasés | ✅ OK |
| RES_KPI4_VAL | card | Taux mandataires actifs | ✅ OK |
| RES_CHART_ACTIFS | barChart | Nombre mandataires actifs | ✅ OK |
| RES_DONUT_STATUT | donutChart | Nombre mandataires actifs | ✅ OK |
| RES_CHART_RETRO | clusteredColumnChart | Montant rétrocommission | ✅ OK |
| RES_TBL_MAND | tableEx | Nombre rendez-vous réalisés, Montant rétrocommission | ✅ OK |

### Rendez-vous (9 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| RDV_KPI1_VAL | card | Nombre rendez-vous prévus | ✅ OK |
| RDV_KPI2_VAL | card | Nombre rendez-vous réalisés | ✅ OK |
| RDV_KPI3_VAL | card | Taux réalisation de rendez-vous | ✅ OK |
| RDV_KPI4_VAL | card | Nombre RDV hebdomadaire moyen | ✅ OK |
| RDV_CHART_TYPE | barChart | Nombre rendez-vous réalisés | ✅ OK |
| RDV_CHART_EVOL | lineChart | Nombre rendez-vous réalisés | ✅ OK |
| RDV_TBL_DETAIL | tableEx | Nombre rendez-vous prévus, Nombre rendez-vous réalisés... | ✅ OK |

### Mandataires (9 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| MAN_KPI1_VAL | card | Nombre mandataires actifs | ✅ OK |
| MAN_KPI2_VAL | card | Nombre mandataires productifs | ✅ OK |
| MAN_KPI3_VAL | card | Nombre mandataires non productifs | ✅ OK |
| MAN_KPI4_VAL | card | Nombre mandataires rétrocommissionnés | ✅ OK |
| MAN_CHART_ANCIENNETE | clusteredColumnChart | Année présence mandataire dans le groupe | ✅ OK |
| MAN_CHART_TAUX_RDV | barChart | Taux réalisation de rendez-vous | ✅ OK |
| MAN_TBL_PERF | tableEx | Nombre rendez-vous réalisés, Taux réalisation de rendez-vous... | ✅ OK |

### Alertes (10 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| ALT_KPI1_VAL | card | Nombre Alertes Critiques | ✅ OK |
| ALT_KPI2_VAL | card | Nombre Alertes Hautes | ✅ OK |
| ALT_KPI3_VAL | card | Nombre Alertes Moyennes | ✅ OK |
| ALT_KPI4_VAL | card | Nombre Alertes Ouvertes | ✅ OK |
| ALT_CARD_VOL_VAL | card | Niveau Alerte Volume | ✅ OK |
| ALT_CARD_RDV_VAL | card | Niveau Alerte RDV | ✅ OK |
| ALT_CARD_RES_VAL | card | Niveau Alerte Réseau | ✅ OK |
| ALT_TBL_ALERTES | tableEx | colonne | ✅ OK |

### Glossaire (3 visuels dynamiques)
| Visuel | Type | Mesures liées | Statut |
|--------|------|---------------|--------|
| HDR_SLC_YEAR | slicer | colonne | ✅ OK |
| HDR_SLC_AGENCE | slicer | colonne | ✅ OK |
| GLO_TBL_INDICATEURS | tableEx | colonne | ✅ OK |

**Total visuels dynamiques: 66**

**Conclusion: Tous les KPIs référencent des mesures valides dans le BIM ✅**
