#!/usr/bin/env python3

"""
This script is meant to comb through all of the human protein mutation datasets (cancer, germline, and somatic) 
and determine the total unique entries in each of the datasets. 
It is also meant to output the total unique entries among all three datasets as well. The goal of this script is to highlight
the amount of data that is currently available per dataset. 
"""
import csv
import glob
import os
import sys

DATA_DIR = "/data/shared/glygen/releases/data/current/reviewed"
FILE_PATTERN = "human_protein_mutation_*_all.csv"

def main():
    search_path = os.path.join(DATA_DIR, FILE_PATTERN)
    files = sorted(glob.glob(search_path))
    
    if not files:
        print(f"Error: No files found in {search_path}", file=sys.stderr)
        return

    global_uniques = set()

    print(f"{'File Name':<45} | {'Raw Rows':>12} | {'Unique (File)':>12}")
    print("-" * 75)

    for filename in files:
        file_uniques = set()
        raw_count = 0
        
        with open(filename, mode='r', encoding='utf-8') as f:
            # DictReader handles headers and basic CSV parsing
            reader = csv.DictReader(f)
            for row in reader:
                raw_count += 1
                try:
                    # Isolate the four specific columns
                    mutation = (
                        row['uniprotkb_canonical_ac'],
                        row['aa_pos'],
                        row['ref_aa'],
                        row['alt_aa']
                    )
                    file_uniques.add(mutation)
                    global_uniques.add(mutation)
                except KeyError:
                    continue
        
        fname = os.path.basename(filename)
        print(f"{fname:<45} | {raw_count:>12,} | {len(file_uniques):>12,}")

    print("-" * 75)
    print(f"{'GRAND TOTAL UNIQUE (across all files):':<58} {len(global_uniques):>12,}")

if __name__ == "__main__":
    main()
