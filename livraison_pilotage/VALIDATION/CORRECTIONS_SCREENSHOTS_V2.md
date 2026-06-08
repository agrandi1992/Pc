# Corrections V2 après ouverture Power BI Desktop

Constats issus des captures transmises :

- le projet s'ouvre bien dans Power BI Desktop ;
- la structure PBIR est bien lue par Desktop ;
- le rendu n'était pas conforme à la maquette : menu latéral peu lisible, titres trop faibles, pages trop techniques ;
- plusieurs KPI réseau/alertes étaient vides ou en erreur ;
- le montant de rétrocommission utilisait le montant réalisé au lieu de la commission réalisée ;
- les mesures réseau s'appuyaient sur une logique de connexion glissante fragile avec `TODAY()` au lieu d'un comptage métier des mandataires.

Corrections appliquées :

1. Menu latéral reconstruit avec formes + libellés visibles.
2. Titres passés en minuscules et alignés sur la charte Capfinances.
3. Header renforcé et slicers repositionnés.
4. Pages métier renommées selon le périmètre attendu.
5. Corrections DAX sur mandataires actifs, inactifs, MIA oriasés, rétrocommissionnés et montant rétrocommission.
6. Mesures budget / commissionné remplacées par des proxys documentés tant que la table budget métier n'est pas disponible.
7. Cartes d'alertes textuelles transformées pour éviter les erreurs visuelles Desktop.
8. Page d'accueil renforcée avec blocs exécutifs alertes et recommandations.

Limite maintenue : cette version reste validée structurellement hors Power BI Desktop. L'ouverture Desktop doit être refaite côté poste utilisateur.
