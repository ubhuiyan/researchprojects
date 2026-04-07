import pandas as pd
import os
import glob

"""
Script written to identify the unique DOIDs available within the GlyGen datasets. 
"""

  
# Directory containing your datasets
input_dir = "/data/shared/glygen/releases/data/current/reviewed"

# Pattern to match CSV files (adjust if needed)
file_pattern = os.path.join(input_dir, "*.csv")

# Store all do_id values
all_do_ids = set()

# Track files with and without do_id column
files_with_do_id = []
files_without_do_id = []

# Iterate through all matching files
for file_path in glob.glob(file_pattern):
    try:
        df = pd.read_csv(file_path, dtype=str)  # read as string to avoid issues
        
        if "do_id" in df.columns:
            files_with_do_id.append(os.path.basename(file_path))
            
            # Drop NaNs and add to set
            do_ids = df["do_id"].dropna().unique()
            all_do_ids.update(do_ids)
        else:
            files_without_do_id.append(os.path.basename(file_path))
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Results
print(f"Total files scanned: {len(glob.glob(file_pattern))}")
print(f"Files WITH do_id column: {len(files_with_do_id)}")
print(f"Files WITHOUT do_id column: {len(files_without_do_id)}")
print(f"Total UNIQUE do_id values: {len(all_do_ids)}")

# Optional: save unique DOIDs to file
output_file = "unique_do_ids.txt"
with open(output_file, "w") as f:
    for do_id in sorted(all_do_ids):
        f.write(f"{do_id}\n")

print(f"Unique DOIDs saved to: {output_file}")
