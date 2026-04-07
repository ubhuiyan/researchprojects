#!/usr/bin/env python3
"""
This script was written to determine how many mutation entries within the GlyGen glycoeffect datasets 
(having a glycosylation effect annotation) are documented to have either a gain/loss of n-glycosylation
or a loss of o-glycosylation. 
"""

import csv
import os

DATA_DIR = "/data/shared/glygen/releases/data/current/reviewed"
CATEGORIES = ['cancer', 'germline', 'somatic']
EFFECTS = ['n-glyco-sequon-gain', 'n-glyco-sequon-loss', 'o-glyco-site-loss']

# These are the unique denominators we calculated previously
BASELINES = {
    'cancer': 3647974,
    'germline': 10778683,
    'somatic': 2435852
}

def get_unique_by_effect(filename):
    """Returns a dictionary mapping effect names to sets of unique mutations."""
    effect_map = {eff: set() for eff in EFFECTS}
    
    if not os.path.exists(filename):
        return effect_map

    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            effect = row.get('effect')
            if effect in effect_map:
                mutation = (
                    row['uniprotkb_canonical_ac'],
                    row['aa_pos'],
                    row['ref_aa'],
                    row['alt_aa']
                )
                effect_map[effect].add(mutation)
    return effect_map

def main():
    print(f"{'Dataset':<10} | {'Glycoeffect':<20} | {'Unique Count':>12} | {'Prevalence %'}")
    print("-" * 65)

    for cat in CATEGORIES:
        glyco_file = os.path.join(DATA_DIR, f"human_protein_mutation_{cat}_glycoeffect.csv")
        unique_counts = get_unique_by_effect(glyco_file)
        denom = BASELINES[cat]

        for effect, mut_set in unique_counts.items():
            count = len(mut_set)
            ratio = (count / denom * 100) if denom > 0 else 0
            print(f"{cat.capitalize():<10} | {effect:<20} | {count:>12,} | {ratio:>11.4f}%")

if __name__ == "__main__":
    main()
