#!/usr/bin/env python3
"""
This script scans downloaded GlyGen TableMaker datasets to identify which
integrated GlyGen organisms (by NCBI taxonomic ID) are present in each file.
By comparing tax_ids found in TableMaker outputs against the authoritative
GlyGen species list, the script enables tracking of documented organisms and
detection of newly added species that may require creation of new
BioCompute objects for documentation.
"""

import os
import csv
import argparse


def load_glygen_tax_ids(species_info_file):
    """Load known GlyGen tax_ids from the species info CSV."""
    tax_ids = set()
    with open(species_info_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                tax_ids.add(row[0].strip())
    return tax_ids


def extract_tax_ids(file_path, column_index):
    """Extract tax_ids from a CSV file using a 1-based column index."""
    tax_ids = set()
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= column_index:
                tax_id = row[column_index - 1].strip()
                if tax_id:
                    tax_ids.add(tax_id)
    return tax_ids


def process_tablemaker_files(data_path, glygen_tax_ids):
    """Iterate through TableMaker CSV files and report matching GlyGen tax_ids."""
    for filename in os.listdir(data_path):
        if not filename.endswith(".csv"):
            continue

        full_path = os.path.join(data_path, filename)

        if filename.startswith("TG"):
            tax_ids = extract_tax_ids(full_path, 3)
        elif filename.startswith("TP"):
            tax_ids = extract_tax_ids(full_path, 8)
        else:
            continue  # skip unrelated files

        matching_tax_ids = sorted(tax_ids & glygen_tax_ids)

        if matching_tax_ids:
            print(f"{filename}: {', '.join(matching_tax_ids)}")
        else:
            print(f"{filename}: No matching tax_ids found")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Identify GlyGen-integrated organisms (tax_ids) present in "
            "downloaded TableMaker datasets."
        )
    )
    parser.add_argument(
        "tablemaker_directory",
        help="Path to the directory containing TableMaker CSV files"
    )
    parser.add_argument(
        "species_info_file",
        help="Path to glygen_species_info.csv containing known GlyGen tax_ids"
    )

    args = parser.parse_args()

    glygen_tax_ids = load_glygen_tax_ids(args.species_info_file)
    process_tablemaker_files(args.tablemaker_directory, glygen_tax_ids)


if __name__ == "__main__":
    main()
