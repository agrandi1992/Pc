# AUDIT_SELECTION_PANE — Structure Groupes
*Généré le 2025-06-05*

## Groupes définis par page

### Tous les pages (sidebar + header)
| Groupe | Visuels membres | Z-index |
|--------|-----------------|---------|
| GRP_NAV | NAV_BG, NAV_LOGO, NAV_SUBTITLE, NAV_SEP, NAV_BTN_* (×8), NAV_VERSION | 90-95 |
| GRP_HDR | HDR_BG, HDR_TITLE, HDR_SLC_YEAR, HDR_SLC_AGENCE | 80-85 |

### Accueil
| Groupe | Visuels membres |
|--------|-----------------|
| GRP_ACC_KPI | ACC_KPI1_BG/ACCENT/LBL/VAL/VAR (×4) |
| GRP_ACC_NAV | ACC_NAV_BG/TOP/LBL/DESC/BTN (×7 pages) |

### Performance
| Groupe | Visuels membres |
|--------|-----------------|
| GRP_PERF_KPI | PERF_KPI1 à PERF_KPI4 (×4×4 visuels) |

### Affaires
| GRP_AFF_KPI | AFF_KPI1 à AFF_KPI4 |

### Réseau MIA
| GRP_RES_KPI | RES_KPI1 à RES_KPI4 |

### Rendez-vous
| GRP_RDV_KPI | RDV_KPI1 à RDV_KPI4 |

### Mandataires
| GRP_MAN_KPI | MAN_KPI1 à MAN_KPI4 |

### Alertes
| GRP_ALT_KPI | ALT_KPI1 à ALT_KPI4 |

## Z-index stratification
| Couche | Z | Contenu |
|--------|---|---------|
| Fond de page | 1 | CONTENT_BG |
| Arrière-plan sections | 2-4 | *_BG, *_SEP |
| Graphiques/Tableaux | 5-8 | CHART_*, TBL_* |
| KPI Cards | 9-15 | KPI*_BG/ACCENT/LBL/VAL/VAR |
| Header | 80-85 | HDR_* |
| Sidebar | 90-95 | NAV_* |

**Résultat: Aucun chevauchement visuel non souhaité. Hiérarchie Z correcte.**
