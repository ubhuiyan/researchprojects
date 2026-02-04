#!/usr/bin/env python3
"""
This script was developed to compare a previous version of a GlyGen dataset
with its current dataset(s) in order to support quality control and identify
potential issues in the entries. It also facilitates transparency by
documenting omitted rows, helping to explain any observed declines in dataset
volume.
"""

import argparse


def read_file_to_set(filename):
    """Read a text or CSV file into a set of stripped lines."""
    with open(filename, 'r') as file:
        return set(line.strip() for line in file)


def main():
    parser = argparse.ArgumentParser(
        description="Compare two GlyGen datasets and report unique and shared entries."
    )
    parser.add_argument(
        "reviewed_dataset",
        help="Path to the reviewed (previous or current) dataset file"
    )
    parser.add_argument(
        "unreviewed_dataset",
        help="Path to the unreviewed (comparison) dataset file"
    )

    args = parser.parse_args()

    set1 = read_file_to_set(args.reviewed_dataset)
    set2 = read_file_to_set(args.unreviewed_dataset)

    unique_to_set1 = list(set1 - set2)
    unique_to_set2 = list(set2 - set1)
    common_to_both = list(set1 & set2)

    print("Top 10 unique to reviewed dataset:")
    for item in unique_to_set1[:10]:
        print(item)

    print("\nTop 10 unique to unreviewed dataset:")
    for item in unique_to_set2[:10]:
        print(item)

    print("\nTop 10 common to both datasets:")
    for item in common_to_both[:10]:
        print(item)


if __name__ == "__main__":
    main()
