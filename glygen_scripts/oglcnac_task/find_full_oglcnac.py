import csv
import os

data_dir = "/data/shared/glygen/releases/data/current/reviewed"
dataset_file = "OGlcNAc_data.txt"

target_glycan = "G49108TO"

unique_entries = set()

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

            # Require all three fields to contain values
            if protein and site and sac:

                if sac == target_glycan:
                    unique_entries.add((protein, site, sac))

print(f"\nTotal unique entries (all fields present): {len(unique_entries)}\n")

# for entry in sorted(unique_entries):
#     print(entry)
