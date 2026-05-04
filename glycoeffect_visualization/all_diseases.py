#%%
import pandas as pd 
import re

df = pd.read_csv("diseaseIDName.csv")
df["do_name"] = df["do_name"].fillna("").astype(str)

invalid_terms = [
    ""
]
df = df[~df["do_name"].str.lower().isin(invalid_terms)]
#%%
# categorization of cancer vs. other
def categorize_disease(text):
    text = text.lower()

    if re.search(r"cancer|carcinoma|tumor|neoplasm|leukemia|lymphoma|sarcoma", text):
        return "Cancer"
    elif re.search(r"neuro|alzheimer|parkinson|epilepsy|ataxia|dementia|sclerosis|migraine|CMT|charcot", text):
        return "Neurological"
    elif re.search(r"cardio|heart|cardiomyopathy|arrhythmia|aortic|atrial|vascular|artery|hypertension|thromb|sinoatrial", text):
        return "Cardiovascular"
    elif re.search(r"diabetes|metabolic|glycogen|lipid|cholesterol|endocrin|thyroid|metabolic", text):
        return "Metabolic"
    elif re.search(r"immune|autoimmune|inflammatory|immunodeficiency|lupus", text):
        return "Immune"
    elif re.search(r"syndrome|congenital|developmental|intellectual|microcephaly|dysplasia|cranio|acro|syndactyly", text):
        return "Developmental"
    elif re.search(r"muscular|dystrophy|myopathy|skeletal|bone|osteoporosis", text):
        return "Musculoskeletal"
    elif re.search(r"kidney|renal|hypogonadism|spermatogenic|nephro", text):
        return "Renal"
    elif re.search(r"deafness|hearing|macular|vision|retina|blindness", text):
        return "Sensory"
    elif re.search(r"anemia|spherocytosis|hemoglob|sickle|protein S|protein C", text):
        return "Hematological"
    elif re.search(r"hereditary|familial|", text):
        return "Hereditary"
    else:
        return "Uncategorized"

df["disease_category"] = df["do_name"].apply(categorize_disease)
# %%
counts = (
    df.groupby(["effect", "disease_category"])
    .size()
    .unstack(fill_value=0)
)

# Optional: filter out very small totals (reduces noise)
counts = counts.loc[counts.sum(axis=1) >= 5]
#%%
# Normalize to proportions
proportions = counts.div(counts.sum(axis=1), axis=0)
proportions.to_excel("new_proportions.xlsx", index=False)
# %%
