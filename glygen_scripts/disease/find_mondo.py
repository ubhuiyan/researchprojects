import pandas as pd
import os
import glob

""""
The script was written to determine the total amount of MONDO IDs that were referenced in GlyGen datasets. 
""""

# Directory containing your datasets
input_dir = "/data/shared/glygen/releases/data/current/reviewed"

# Pattern to match CSV files (adjust if needed)
file_pattern = os.path.join(input_dir, "*.csv")

# Store all mondo_id values
all_mondo_ids = set()

# Track files with and without mondo_id column
files_with_mondo_id = []
files_without_mondo_id = []

# Iterate through all matching files
for file_path in glob.glob(file_pattern):
    try:
        df = pd.read_csv(file_path, dtype=str)  # read as string to avoid issues
        
        if "mondo_id" in df.columns:
            files_with_mondo_id.append(os.path.basename(file_path))
            
            # Drop NaNs and add to set
            mondo_ids = df["mondo_id"].dropna().unique()
            all_mondo_ids.update(mondo_ids)
        else:
            files_without_mondo_id.append(os.path.basename(file_path))
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Results
print(f"Total files scanned: {len(glob.glob(file_pattern))}")
print(f"Files WITH do_id column: {len(files_with_mondo_id)}")
print(f"Files WITHOUT mondo_id column: {len(files_without_mondo_id)}")
print(f"Total UNIQUE mondo_id values: {len(all_mondo_ids)}")

# Optional: save unique DOIDs to file
output_file = "unique_mondo_ids.txt"
with open(output_file, "w") as f:
    for mondo_id in sorted(all_mondo_ids):
        f.write(f"{mondo_id}\n")

print(f"Unique MONDOIDs saved to: {output_file}")
