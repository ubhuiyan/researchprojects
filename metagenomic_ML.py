#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from sklearn import tree
from sklearn import metrics
print("Ready to Go")
#%%
train_table = pd.read_csv("final_train_table.csv")
#%%
train_table = train_table.iloc[10:29,:]
print("Table Loaded")
#%%
#Establish X and y variables for Decision Tree Model 
X = train_table.drop(["Status", "Reference"], axis=1)
y = train_table["Status"]
print("Table Ready to Go")
#%%
#Split dataset into train and test datasets 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.25 ,random_state=1)
print("Model Ready to Go")
# %%
#Train Decision Tree Model 
DTF = DecisionTreeClassifier()
DTF.fit(X_train,y_train)
print(f'DecisionTreeClassifier train score: {DTF.score(X_train,y_train)}')
print(f'DecisionTreeClassifier test score:  {DTF.score(X_test,y_test)}')
print(confusion_matrix(y_test, DTF.predict(X_test)))
print(classification_report(y_test, DTF.predict(X_test)))
#%%
RF = RandomForestClassifier(random_state=123)
RF.fit(X_train,y_train)
print(f'RandomForestClassifier train score: {RF.score(X_train,y_train)}')
print(f'RandomForestClassifier test score:  {RF.score(X_test,y_test)}')
print(confusion_matrix(y_test, RF.predict(X_test)))
print(classification_report(y_test, RF.predict(X_test)))
#%%
#Create AUC score
y_test_proba = DTF.predict_proba(X_test)
auc = metrics.roc_auc_score(y_test, y_test_proba[:,1])
print(f'DecisionTreeClassifier AUC score: {auc}')
#Create ROC curve 
fpr, tpr, _ = metrics.roc_curve(y_test, y_test_proba[:,1], pos_label=DTF.classes_[1])
plt.clf()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
#%%
y_test_proba = RF.predict_proba(X_test)
auc = metrics.roc_auc_score(y_test, y_test_proba[:,1])
print(f'Random Forest Tree AUC score: {auc}')
#Create ROC curve 
fpr, tpr, _ = metrics.roc_curve(y_test, y_test_proba[:,1], pos_label=RF.classes_[1])
plt.clf()
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
#%%
#Create Confusion Matrix Heatmap  
c_matrix = confusion_matrix(y_test, DTF.predict(X_test))
plt.figure(figsize=(10,8))
fontsize=15
ax = plt.subplot()
sns.heatmap(c_matrix, annot=True,  cmap="BuPu", ax=ax)
ax.xaxis.set_ticklabels(['NR', 'R']); ax.yaxis.set_ticklabels(['NR', 'R'])
plt.title("Confusion Matrix for Decision Tree Classifier", fontsize=(fontsize+3))
plt.xlabel("Predicted Label", fontsize=fontsize)
plt.ylabel("True Label", fontsize=fontsize)
plt.show()
#%%
c_matrix = confusion_matrix(y_test, RF.predict(X_test))
plt.figure(figsize=(10,8))
fontsize=15
ax = plt.subplot()
sns.heatmap(c_matrix/np.sum(c_matrix), annot=True, fmt=".2%", cmap="BuPu", ax=ax)
ax.xaxis.set_ticklabels(['NR', 'R']); ax.yaxis.set_ticklabels(['NR', 'R'])
plt.title("Confusion Matrix for Decision Tree Classifier", fontsize=(fontsize+3))
plt.xlabel("Predicted Label", fontsize=fontsize)
plt.ylabel("True Label", fontsize=fontsize)
plt.show()
#%%
#Decision Tree Visualization 
feature_names = train_table.columns.drop(["Reference", "Status"])
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(DTF,   
                   feature_names=feature_names,
                   class_names=DTF.classes_,
                   filled=True)
fontsize=35
plt.title("Classification Tree Diagram for Metagenomic Data", fontsize=fontsize)
plt.show()
#%%
#Determine top ten features for RF
features = feature_names
importances = DTF.feature_importances_
indices = np.argsort(importances)
num_features = 5
plt.figure(figsize=(16,14))
plt.title('Feature Importances')

# only plot the customized number of features
plt.barh(range(num_features), importances[indices[-num_features:]], color='lightblue', align='center')
plt.yticks(range(num_features), [features[i] for i in indices[-num_features:]])
fontsize = 25
plt.title("Feature Importance of Decision Tree Model", fontsize=fontsize)
plt.xlabel('Relative Importance', fontsize=fontsize)
plt.ylabel("Features (Bacteria)", fontsize=fontsize) 
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.show()
#There appears to only be one feature that is the most significant in predicting R/NR status 
# %%
