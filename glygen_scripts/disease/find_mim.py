import pandas as pd
import os
import glob

""""
Script written to determine the unique number of MIM IDs present in GlyGen datasets. 
"""

# Directory containing your datasets
input_dir = "/data/shared/glygen/releases/data/current/reviewed"

# Pattern to match CSV files (adjust if needed)
file_pattern = os.path.join(input_dir, "*.csv")

# Store all mim_id values
all_mim_ids = set()

# Track files with and without mim_id column
files_with_mim_id = []
files_without_mim_id = []

# Iterate through all matching files
for file_path in glob.glob(file_pattern):
    try:
        df = pd.read_csv(file_path, dtype=str)  # read as string to avoid issues
        
        if "mim_id" in df.columns:
            files_with_mim_id.append(os.path.basename(file_path))
            
            # Drop NaNs and add to set
            mim_ids = df["mim_id"].dropna().unique()
            all_mim_ids.update(mim_ids)
        else:
            files_without_mim_id.append(os.path.basename(file_path))
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Results
print(f"Total files scanned: {len(glob.glob(file_pattern))}")
print(f"Files WITH mim_id column: {len(files_with_mim_id)}")
print(f"Files WITHOUT mim_id column: {len(files_without_mim_id)}")
print(f"Total UNIQUE mim_id values: {len(all_mim_ids)}")

# Optional: save unique DOIDs to file
output_file = "unique_mim_ids.txt"
with open(output_file, "w") as f:
    for mim_id in sorted(all_mim_ids):
        f.write(f"{mim_id}\n")

print(f"Unique MIMIDs saved to: {output_file}")
