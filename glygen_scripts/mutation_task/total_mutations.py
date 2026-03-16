#!/usr/bin/env python3
"""
This script extracts mutation datasets containing the columns for UniProtKB accession, amino acid position, 
reference amino acid, and altered amino acid to identify unique mutation records. 
The script operates at the species level and aggregates mutations across all relevant datasets to determine 
the total number of unique amino acid substitutions available in a given GlyGen release. 
"""

import pandas as pd
import glob
import os
import argparse

COLUMNS = [
    "uniprotkb_canonical_ac",
    "aa_pos",
    "ref_aa",
    "alt_aa"
]

def main(species):

    base_path = "/data/shared/glygen/releases/data/current/reviewed"
    pattern = os.path.join(base_path, f"{species}_protein_mutation_*.csv")

    files = glob.glob(pattern)

    if not files:
        print(f"No files found for species: {species}")
        return

    print(f"Found {len(files)} files")

    dfs = []

    for file in files:
        try:
            df = pd.read_csv(file, usecols=COLUMNS, dtype=str)
            dfs.append(df)
        except ValueError:
            print(f"Skipping {file} (missing required columns)")

    if not dfs:
        print("No usable files found.")
        return

    combined = pd.concat(dfs, ignore_index=True)

    print(f"\nTotal rows before deduplication: {len(combined)}")

    unique_mutations = combined.drop_duplicates(subset=COLUMNS)

    print(f"Total unique mutations: {len(unique_mutations)}")
    print(f"Duplicates removed: {len(combined) - len(unique_mutations)}")

    # Optional export
    output_file = f"{species}_unique_mutations.csv"
    unique_mutations.to_csv(output_file, index=False)

    print(f"\nUnique mutation list written to: {output_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Count unique amino acid mutations for a species")
    parser.add_argument("species", help="Species prefix (e.g. human, mouse)")

    args = parser.parse_args()

    main(args.species)
