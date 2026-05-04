# Prediabetes Exercise Response Prediction Using Proteomics Data
## Overview

This project develops and evaluates machine learning models to predict heterogeneous responses to high-intensity exercise in prediabetic individuals using baseline proteomics profiles. The dataset consists of 48 participants (34 responders, 16 non-responders) with 688 protein features derived from a published study (PMID: 36787735).

The workflow explores multiple classification algorithms and data balancing strategies, including SMOTE, ADASYN, and noise injection, to address class imbalance and improve predictive performance in a small-sample, high-dimensional biological dataset.

-----------------------------

## Dataset
- Source: Published proteomics study on exercise response in prediabetes (PMID: 36787735)
- Samples: 48 participants (34 responders and 16 non-responders)
- Features: 688 protein expression measurements

-----------------------------

## Methods
Data Preprocessing
Baseline proteomics expression matrix used as input

Class imbalance addressed using:
- SMOTE (Synthetic Minority Over-sampling Technique)
- ADASYN (Adaptive Synthetic Sampling)
- Gaussian noise injection for synthetic augmentation

---------------------------

## Models Evaluated

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- Gradient Boosting

-----------------------------------------

## Hyperparameter Optimization
Grid search used for tuning Logistic Regression and SVM models
Evaluated key parameters such as:
- Regularization strength (C)
- Penalty type (L1/L2)
- Kernel parameters (SVM)

-----------------------------------------

## Key Results
### Baseline Model Comparison (no resampling)
Models showed high training accuracy (~1.0) but variable test performance
Logistic Regression and SVM demonstrated relatively better generalization compared to ensemble methods in this small dataset setting

-----------------------------------------

## Best Logistic Regression (tuned)
- Test Accuracy: 0.70
- F1 Score: 0.77
- AUC: 0.79

Identified as the most stable model under baseline conditions

------------------------------------------

## Best SVM (tuned)
- Test Accuracy: 0.60
- F1 Score: 0.74
- AUC: 0.58

Showed reduced performance under class imbalance conditions

-------------------------------------------

## Effect of Resampling Techniques

### SMOTE (Logistic Regression)

- Test Accuracy: up to 0.93
- F1 Score: 0.92
- AUC: 0.93

Improved performance but introduced variability across runs

### SMOTE (SVM)

- Test Accuracy: 0.64
- F1 Score: 0.71
- AUC: 0.16

Highlighted instability of SVM under synthetic sampling

### ADASYN (SVM) 

- Test Accuracy: 0.71
- F1 Score: 0.75
- AUC: 0.50

Improved balance but did not consistently outperform SMOTE
Performance varied depending on model and sampling configuration

------------------------------------------

## Noise Injection Augmentation
- Test Accuracy: 0.90
- F1 Score: 0.92
- AUC: 0.92

Produced the most stable results across repeated runs
However, perfect training performance (1.0) suggests residual overfitting

-----------------------------------------

## Key Insights
Small-sample, high-dimensional proteomics data is highly susceptible to overfitting
Resampling techniques improve class balance but can introduce instability depending on model choice
Logistic Regression demonstrated the most consistent performance across experiments
Synthetic augmentation (noise injection) improved stability but did not fully eliminate overfitting risks

---------------------------------------------

## Limitations
Limited sample size (n=48) restricts generalizability
High-dimensional feature space increases risk of overfitting
Performance metrics may be sensitive to resampling strategy and dataset partitioning
External validation on independent cohorts is required for clinical interpretation

----------------------------------------------

## Tools & Libraries
- Python
- scikit-learn
- imbalanced-learn (SMOTE, ADASYN)
- pandas
- numpy
