#!/usr/bin/env python3
"""
This script scans all GlyGen proteoform glycosylation site datasets within a
user-specified directory to identify and report all unique carbohydrate
(`carb_name`) values documented to date. It is intended to support dataset
auditing, harmonization, and transparency by providing a consolidated view of
carbohydrate nomenclature across GlyGen releases.
"""

import os
import glob
import argparse
import pandas as pd


def collect_unique_carb_names(base_directory):
    pattern = os.path.join(
        base_directory,
        '*_proteoform_glycosylation_sites_*.csv'
    )
    files = glob.glob(pattern)

    if not files:
        print(f"No matching files found in directory: {base_directory}")
        return

    unique_values = set()

    for f in files:
        try:
            df = pd.read_csv(f, dtype=str)  # read all columns as strings
        except Exception as e:
            print(f"Could not read file {f}: {e}")
            continue

        if 'carb_name' not in df.columns:
            print(f"'carb_name' column not found in: {f}")
            continue

        for v in df['carb_name'].dropna().unique():
            unique_values.add(v.strip())

    print("\nUnique carb_name values across all files:")
    for value in sorted(unique_values):
        print(value)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Collect all unique carbohydrate (carb_name) values from GlyGen "
            "proteoform glycosylation site datasets in a specified directory."
        )
    )
    parser.add_argument(
        "directory",
        help="Path to the directory containing GlyGen reviewed glycosylation site CSV files"
    )

    args = parser.parse_args()
    collect_unique_carb_names(args.directory)


if __name__ == "__main__":
    main()
