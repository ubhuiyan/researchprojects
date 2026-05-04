# Mutation Effect Distribution Across Disease Ontology Classes

## Overview
This project analyzes mutation datasets from GlyGen to quantify the distribution of mutation effects across disease categories. It integrates germline, somatic, and cancer-associated mutation data, 
maps disease ontology identifiers (DOID) to standardized terms, and categorizes diseases into biologically meaningful groups for downstream aggregation and visualization.

## Data Sources
- Germline mutation dataset (glycoeffect annotations)
- Somatic mutation dataset (glycoeffect annotations)
- Cancer mutation dataset (glycoeffect annotations)
- Disease Ontology mapping file (HumanDO)

## Methods 

### 1. Data Integration 
- Combined multiple mutation datasets into a unified structure
- standardized key biological fields:
    - UniProtKB accession
    - amino acid position
    - reference/altered amino acid
    - disease ontology IDs (DOID_
    - functional glycosylation effect annotations

### 2. Data Cleaning 
- Removed missing values
- Converted DOID identifiers into integer format
- Removed duplicate mutation entries

### 3. Disease Ontology Mapping 
- Mapped DOID identifiers to disease ontology labels using HumanDO TSV mapping file
- Created unified disease annotation field for downstream analysis

### 4. Disease Categorization 

Diseases were grouped into biologically meaningful classes using rule-based text classification: 
- Cancer
- Neurological
- Cardiovascular
- Metabolic
- Immune
- Developmental
- Musculoskeletal
- Renal
- Sensory
- Hematological
- Hereditary

### 5. Aggregation Analysis 
- Computed mutation effect distributions across disease categories
- Aggregated counts by:
  - mutation effect type
  - disease category
- Converted counts into normalized porportions for comparative analysis

## Output 
- Cleaned and annotated dataset (diseaseIDName.csv)
- Aggregated porportional distribution table (xxx)
- Ready for visualization (pie charts/bar plots of mutation effects by disease class) 

## Key Insights 
- Cancer-related mutations represent a dominant category in somatic dataset, where hereditary/familial based mutations are dominant in germline dataset.
- Ontology mapping improves interpretability of mutation datasets
- Rule-based disease classification enables rapid stratification of large hetereogenous datasets 

## Tools & Technologies 
- Python
- pandas
- regex
- bash scripting (data retrieval automation)
- Disease Ontology (DOID) resources

## Reproducibility 

Pipeline includes: 
- automated data download script (uberon_download.sh)
- modular python scripts for each transoformation step
- intermediate outputs preserved for tracability 
