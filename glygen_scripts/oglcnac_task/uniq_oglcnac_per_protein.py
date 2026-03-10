import csv
import os
from collections import defaultdict

data_dir = "/data/shared/glygen/releases/data/current/reviewed"
dataset_file = "OGlcNAc_data.txt"
output_file = "OGlcNAc_protein_site_counts.txt"

target_glycan = "G49108TO"

# store unique protein-site pairs
protein_sites = set()

with open(dataset_file) as f:
    datasets = [line.strip() for line in f if line.strip()]

for dataset in datasets:
    path = os.path.join(data_dir, dataset)

    if not os.path.exists(path):
        print(f"Warning: {dataset} not found")
        continue

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            protein = row.get("uniprotkb_canonical_ac", "").strip()
            site = row.get("glycosylation_site_uniprotkb", "").strip()
            sac = row.get("saccharide", "").strip()

            # require protein + site + correct glycan
            if protein and site and sac == target_glycan:
                protein_sites.add((protein, site))

# group sites by protein
site_counts = defaultdict(set)

for protein, site in protein_sites:
    site_counts[protein].add(site)

# write results to file
with open(output_file, "w") as out:
    out.write("protein\tO-GlcNAc_site_count\n")

    for protein in sorted(site_counts):
        out.write(f"{protein}\t{len(site_counts[protein])}\n")

print(f"\nResults written to: {output_file}")

print("\nSummary")
print("Unique proteins:", len(site_counts))
print("Total unique sites:", sum(len(v) for v in site_counts.values()))
