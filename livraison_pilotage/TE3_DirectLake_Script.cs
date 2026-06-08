// ═══════════════════════════════════════════════════════════════════════════
// TABULAR EDITOR 3 — ADVANCED SCRIPT
// Conversion Direct Lake — Pilotage Commercial
// 
// PRÉREQUIS : Ouvrir dans TE3 via XMLA :
//   File > Open > Model from URL
//   URL : powerbi://api.powerbi.com/v1.0/myorg/faw-partners-smart-data-dev
//   Sélectionner : Pilotage_Commercial
//
// EXÉCUTION : Ctrl+Shift+M (Advanced Scripting) → coller → Run (F5)
// SAUVEGARDER : Ctrl+S (PAS "Deploy workspace database")
// ═══════════════════════════════════════════════════════════════════════════

var goldTables = new System.Collections.Generic.HashSet<string> {
    "fact_affaire",
    "fact_affectation_mandataire",
    "fact_activite_mandataire",
    "fact_rendez_vous_client",
    "fact_parcours_candidat",
    "fact_vigilance",
    "dim_agence",
    "dim_mandataire",
    "dim_produit",
    "dim_candidat",
    "dim_type_rendez_vous_client",
    "dim_niveau_etude",
    "dim_motif_depart_formation",
    "dim_charge_developpement_reseau",
    "dim_type_canal",
    "bridge_rendez_vous_mandataire",
    "glossaire_indicateurs",
    "dim_charge_production",
    "dim_compagnie",
    "dim_dossier",
    "dim_niveau_vigilance"
};

int converted  = 0;
int alreadyDL  = 0;
var log = new System.Text.StringBuilder();
log.AppendLine("=== AUDIT AVANT CONVERSION ===");

foreach (var table in Model.Tables)
{
    if (!goldTables.Contains(table.Name)) continue;

    foreach (var partition in table.Partitions)
    {
        var srcType  = partition.SourceType;
        var srcMode  = partition.Mode;

        // Déjà correctement configuré
        if (srcType == PartitionSourceType.Entity &&
            srcMode  == ModeType.DirectLake)
        {
            alreadyDL++;
            log.AppendLine($"  ✅ {table.Name} — déjà DirectLake/Entity");
            continue;
        }

        log.AppendLine($"  🔄 {table.Name} — {srcMode}/{srcType} → DirectLake/Entity");

        // Créer la source entity
        var entitySrc = new EntityPartitionSource
        {
            EntityName = table.Name
            // SchemaName non requis : Fabric utilise "dbo" par défaut
        };
        partition.Source = entitySrc;
        partition.Mode   = ModeType.DirectLake;
        converted++;
    }
}

log.AppendLine();
log.AppendLine("═══════════════════════════════════════");
log.AppendLine($"  Converties   : {converted}");
log.AppendLine($"  Déjà DL      : {alreadyDL}");
log.AppendLine($"  Total Gold   : {converted + alreadyDL} / {goldTables.Count}");
log.AppendLine("═══════════════════════════════════════");
log.AppendLine();

if (converted > 0)
{
    log.AppendLine("✅ Script terminé — modèle modifié en mémoire.");
    log.AppendLine("⚡ ÉTAPE SUIVANTE : appuyez Ctrl+S pour sauvegarder dans Fabric");
    log.AppendLine("   (NE PAS utiliser 'Deploy workspace database')");
    log.AppendLine("   Puis dans Fabric workspace : déclencher un rafraîchissement.");
}
else
{
    log.AppendLine("ℹ️  Aucune modification — toutes les tables sont déjà en Direct Lake.");
}

Info(log.ToString());
