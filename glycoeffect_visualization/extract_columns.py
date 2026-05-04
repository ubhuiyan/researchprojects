#%%
"""
This script aims to extract the UniProtKB accession, amino acid poisition, reference amino acid, 
altered amino acid, Disease Ontology ID, and the glycosylation effect from the following 
datasets. 
"""

import pandas as pd 

df1 = pd.read_csv("human_protein_mutation_germline_glycoeffect.csv")
df2 = pd.read_csv("human_protein_mutation_somatic_glycoeffect.csv")
df3 = pd.read_csv("human_protein_mutation_cancer_glycoeffect.csv")

#%%
df1 = df1[["uniprotkb_canonical_ac","aa_pos","ref_aa","alt_aa","do_id","effect"]]
df2 = df2[["uniprotkb_canonical_ac","aa_pos","ref_aa","alt_aa","do_id","effect"]]
df3 = df3[["uniprotkb_canonical_ac","aa_pos","ref_aa","alt_aa","do_id","effect"]]

result = pd.concat([df1, df2, df3], ignore_index=True) 
result = result.dropna()
result['do_id'] = result['do_id'].astype(int)
result = result.drop_duplicates()
#%%
result.to_csv('concat_data.csv', index=False)
