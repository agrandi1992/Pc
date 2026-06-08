// ═══════════════════════════════════════════════════════════════
// TABULAR EDITOR 3 — EXTRACT DATASOURCE
// 
// 1. Ouvrir TE3 connecté via XMLA au modèle QUI MARCHE
//    (le modèle Direct Lake existant — côté droit de la comparaison)
// 2. Advanced Scripting (Ctrl+Shift+M) → coller → F5
// 3. Copier le résultat et me l'envoyer
// ═══════════════════════════════════════════════════════════════

var sb = new System.Text.StringBuilder();
sb.AppendLine("=== DATASOURCES DU MODÈLE ===\n");

foreach (var ds in Model.DataSources)
{
    sb.AppendLine($"Name  : {ds.Name}");
    sb.AppendLine($"Type  : {ds.GetAnnotation("PBI_NavigationStepName") ?? ds.GetType().Name}");
    
    // Lire les propriétés via reflection pour avoir le JSON complet
    var json = Newtonsoft.Json.JsonConvert.SerializeObject(ds, Newtonsoft.Json.Formatting.Indented);
    sb.AppendLine("JSON:");
    sb.AppendLine(json);
    sb.AppendLine("─────────────────────────────────────────────────");
}

sb.AppendLine("\n=== ENTITY PARTITION SAMPLE (dim_mandataire) ===\n");
var tbl = Model.Tables["dim_mandataire"];
if (tbl != null)
{
    foreach (var p in tbl.Partitions)
    {
        sb.AppendLine($"Partition: {p.Name}");
        sb.AppendLine($"  Mode         : {p.Mode}");
        sb.AppendLine($"  SourceType   : {p.SourceType}");
        
        if (p.Source is EntityPartitionSource eps)
        {
            sb.AppendLine($"  EntityName   : {eps.EntityName}");
            sb.AppendLine($"  SchemaName   : {eps.SchemaName}");
            sb.AppendLine($"  ExprSrc      : {eps.ExpressionSource}");
        }
        var psrc = Newtonsoft.Json.JsonConvert.SerializeObject(p.Source, Newtonsoft.Json.Formatting.Indented);
        sb.AppendLine("  Source JSON  :");
        sb.AppendLine(psrc);
    }
}

Info(sb.ToString());
