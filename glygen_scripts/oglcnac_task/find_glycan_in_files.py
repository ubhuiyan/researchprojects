import glob
import csv
import os

target = "G49108TO"

# directory containing the files
directory = "/data/shared/glygen/releases/data/current/reviewed"

# pattern for the files you want to search
pattern = os.path.join(directory, "*_proteoform_glycosylation_sites_*.csv")

files = glob.glob(pattern)

matches = []

for file in files:
    with open(file, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row.get("saccharide") == target:
                matches.append(file)
                break

print(f"\nFiles containing {target}:\n")
for m in matches:
    print(os.path.basename(m))
