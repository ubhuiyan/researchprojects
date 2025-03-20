import pandas as pd
from imblearn.over_sampling import SMOTE

# Load your dataset
df = pd.read_csv('proteomics_baseline.csv')

# Separate features and target variable
target_column = 'response'  # Adjust as needed

# Apply SMOTE
smote = SMOTE(random_state=42)
df_resampled, y_resampled = smote.fit_resample(df.drop(target_column, axis=1), df[target_column])

df_resampled[target_column] = y_resampled  # Reintegrate the target column

# Save the upsampled dataset to a new file
df_resampled.to_csv('resampled_dataset.csv', index=False)

# Check class distribution before and after SMOTE
print("Before SMOTE:", df[target_column].value_counts())
print("After SMOTE:", df_resampled[target_column].value_counts())