import csv
import os

# location of datasets
data_dir = "/data/shared/glygen/releases/data/current/reviewed"

# file listing datasets to check
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
            if row.get("saccharide") == target_glycan:

                protein = row.get("uniprotkb_canonical_ac", "").strip()
                site = row.get("glycosylation_site_uniprotkb", "").strip()
                sac = row.get("saccharide", "").strip()

                # store unique triple
                unique_entries.add((protein, site, sac))

# results
print(f"Total unique entries found: {len(unique_entries)}")

# print("\nUnique entries:")
# for entry in sorted(unique_entries):
#     print(entry)
