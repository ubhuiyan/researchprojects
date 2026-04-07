#!/usr/bin/env python3
"""
This script is meant to identify the number of mutations that have a at least one disease annotation provided. The objective
is to determine the percent composition of mutation entries with disease annotations. Our prediction is that there are 
many mutation entries that likely do not have a disease annotation, and we ran this script to check how many did. 
"""
import csv
import glob
import os
import sys

DATA_DIR = "/data/shared/glygen/releases/data/current/reviewed"

FILE_PATTERNS = ["human_protein_mutation_germline_all.csv", "human_protein_mutation_somatic_all.csv"]

def main():
    print(f"{'File Name':<40} | {'Total Unique':>12} | {'With Disease':>12} | {'Ratio %'}")
    print("-" * 85)

    for pattern in FILE_PATTERNS:
        file_path = os.path.join(DATA_DIR, pattern)
        files = glob.glob(file_path)
        
        if not files:
            continue

        for filename in files:
            all_unique_muts = set()
            disease_unique_muts = set()

            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Identity tuple (Task 1 columns)
                    mutation = (
                        row['uniprotkb_canonical_ac'],
                        row['aa_pos'],
                        row['ref_aa'],
                        row['alt_aa']
                    )
                    
                    # Add to denominator set
                    all_unique_muts.add(mutation)
                    
                    # Add to numerator set ONLY if do_id is present/not empty
                    # We check for both existence of the key and that it's not just whitespace
                    if row.get('do_id') and row['do_id'].strip():
                        disease_unique_muts.add(mutation)

            total = len(all_unique_muts)
            with_disease = len(disease_unique_muts)
            ratio = (with_disease / total * 100) if total > 0 else 0
            
            fname = os.path.basename(filename)
            print(f"{fname:<40} | {total:>12,} | {with_disease:>12,} | {ratio:>6.2f}%")

if __name__ == "__main__":
    main()
