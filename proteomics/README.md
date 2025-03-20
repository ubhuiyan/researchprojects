## Prediabetes Proteomics Model 

The following files contain scripts and data used to develop a rainforest classification model for a dataset sourced from a publication focused on identifying heterogeneous responses to high-intensity exercise in the treatment of pre-diabetes among medication-naive participants [PMID: 36787735]. Descriptions for each file is provided below. 

-----------------
### proteomics_baseline.csv 
This file contains the baseline proteomics expression profiles for all participants in the corresponding study. 

Metadata:
- 48 particpants
- 34 responders | 16 non-responders
- 688 genes 

### SMOTE.py
This script was used to address class imbalance by resampling the minority class in the dataset.

### resampled_dataset.csv 
This is the resulting dataset from the SMOTE.py script. This dataset was used for modeling. 

Metadata: 
- 68 observations
- 34 responders | 34 non-responders
- 688 genes

### model_pickling.py
This script was used to generate a Random Forest Classification model. 

Performance Metrics:

Accuracy: 0.90

F1 Score: 0.90

### single_patient_data.csv
A single patient unknown sample was created to test the model's prediction. 

### model_predict.py
The single patient data is run through this script to generate a txt file with the model's prediction of Responder or Non-responder. 

### model_bco.json
This file contains the BioCompute Object for this model. 
