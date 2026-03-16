"""
This script aims to identify datasets that provide a mutation type and glycoeffect (effect) to identify the types of
mutations + glycoeffect they have on a given species in GlyGen datasets. The filtering process is 
conducted using dbSNP (https://www.ncbi.nlm.nih.gov/snp/) identification. It's important to note, not all mutations
housed on GlyGen contain a dbSNP ID, so this is only working on a subset of the total data. 
"""


import pandas as pd
import glob
import os
import argparse

COLUMNS = [
    "uniprotkb_canonical_ac",
    "aa_pos",
    "dbsnp_id",
    "ref_aa",
    "alt_aa",
    "mutation_type",
    "effect"
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
            df = pd.read_csv(file, usecols=COLUMNS)
            dfs.append(df)
        except ValueError:
            print(f"Skipping {file} (missing required columns)")

    combined = pd.concat(dfs, ignore_index=True)

    print(f"\nTotal rows before deduplication: {len(combined)}")

    # Separate rows with and without dbsnp_id
    with_dbsnp = combined.dropna(subset=["dbsnp_id"])
    without_dbsnp = combined[combined["dbsnp_id"].isna()]

    # Deduplicate using dbsnp_id
    dedup_with_dbsnp = with_dbsnp.drop_duplicates(subset=["dbsnp_id"])

    combined_dedup = pd.concat([dedup_with_dbsnp, without_dbsnp], ignore_index=True)

    print(f"Rows after dbSNP deduplication: {len(combined_dedup)}")
    print(f"Duplicates removed: {len(combined) - len(combined_dedup)}")

    # Mutation type counts
    mutation_counts = combined_dedup["mutation_type"].value_counts(dropna=False)

    print("\nMutation Type Counts")
    print("--------------------")
    print(mutation_counts)

    # Export cleaned dataset
    output_file = f"{species}_mutation_deduplicated.csv"
    combined_dedup.to_csv(output_file, index=False)

    print(f"\nCleaned dataset written to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize mutation types by species.")
    parser.add_argument("species", help="Species prefix (e.g., human, mouse)")

    args = parser.parse_args()
    main(args.species)
