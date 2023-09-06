# -*- coding: utf-8 -*-
"""ML Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-zeVqFR5-YxrBsBbIfpUJ-J_l5lwVjEu

PREDICTIVE MAINTENANCE OF INDUSTRIAL EQUIPMENT

IMPORTING PACKAGES
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""DATASET"""

data = pd.read_csv('Predictive maintenance.csv')
df = pd.DataFrame(data)
df

df.head()

"""CHECKING MISSING VALUES"""

df.info()

df.describe(include='all').T

"""CHECKING FOR MISSING VALUES HIDDEN AS QUESTION MARK"""

df.replace("?",np.nan,inplace=True)

"""CONVERTING TO FLOAT TO MAKE PREPROCESSING EASIER"""

for column in df.columns:
    try:
        df[column]=df[column].astype(float)
    except:
        pass

"""DROPING UNIMPORTANT FEATURES"""

df.drop(['UDI','Product ID'],axis=1,inplace=True)

"""INCORPORATING FAILURE MODES INTO SINGLE FEATURE"""

df['TWF'].value_counts()

df['Machine failure']=0
df['Machine failure'][df['TWF']==1]=1
df['Machine failure'][df['HDF']==1]=2
df['Machine failure'][df['PWF']==1]=3
df['Machine failure'][df['OSF']==1]=4
df['Machine failure'][df['RNF']==1]=5
df.drop(['TWF','HDF','PWF','OSF','RNF'],axis=1,inplace=True)

"""DERIVED FEATURES"""

df['Power']=df['Rotational speed [rpm]']*df['Torque [Nm]']
df['Power wear']=df['Power']*df['Tool wear [min]']
df['Temperature difference'] = df['Process temperature [K]']-df['Air temperature [K]']
df['Temperature power'] = df['Temperature difference']/df['Power']
df = df[['Air temperature [K]',
         'Process temperature [K]',
         'Rotational speed [rpm]',
         'Torque [Nm]',
         'Tool wear [min]',
         'Power',
         'Power wear',
         'Temperature difference',
         'Temperature power',
         'Type',
         'Machine failure'
        ]]

list(df)

"""CONVERTING CATEGORICAL INFORMATION INTO NUMERIC"""

df = pd.get_dummies(df,drop_first=True)

df.head()

df = df[['Air temperature [K]',
         'Process temperature [K]',
         'Rotational speed [rpm]',
         'Torque [Nm]',
         'Tool wear [min]',
         'Power',
         'Power wear',
         'Temperature difference',
         'Temperature power',
         'Type_L',
         'Type_M',
         'Machine failure'
        ]]

"""PREPROCESSING"""

from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import PowerTransformer

# Scale
pipe = make_pipeline(PowerTransformer())
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X = pipe.fit_transform(X.copy())

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X.head()
feature_names = list(X.columns)
np.shape(X)

len(feature_names)

"""SPLITTING TRAINING AND TESTING DATA"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, 
                                                    random_state = 0,
                                                    stratify=y)

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""IMPORTING REQUIRED PACKAGES"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

"""TRAINING AND MODEL EVALUATION

LOGISTIC REGRESSION
"""

# Train and evaluate logistic regression
lr = LogisticRegression(random_state=0)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
accuracy_lr = accuracy_score(y_test, y_pred_lr)
precision_lr = precision_score(y_test, y_pred_lr,average='micro')
recall_lr = recall_score(y_test, y_pred_lr,average='micro')
f1_lr = f1_score(y_test, y_pred_lr,average='micro')
cm_lr = confusion_matrix(y_test, y_pred_lr)
print("Logistic Regression:")
print(f"Accuracy: {accuracy_lr:.3f}")
print(f"Precision: {precision_lr:.3f}")
print(f"Recall: {recall_lr:.3f}")
print(f"F1-score: {f1_lr:.3f}")
print(f"Confusion matrix:\n{cm_lr}\n")

"""KNN"""

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
precision_knn = precision_score(y_test, y_pred_knn,average='micro')
recall_knn = recall_score(y_test, y_pred_knn,average='micro')
f1_knn = f1_score(y_test, y_pred_knn,average='micro')
cm_knn = confusion_matrix(y_test, y_pred_knn)
print("KNN:")
print(f"Accuracy: {accuracy_knn:.3f}")
print(f"Precision: {precision_knn:.3f}")
print(f"Recall: {recall_knn:.3f}")
print(f"F1-score: {f1_knn:.3f}")
print(f"Confusion matrix:\n{cm_knn}\n")

"""DECISION TREE"""

# Train and evaluate decision tree
dt = DecisionTreeClassifier(random_state=0)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
precision_dt = precision_score(y_test, y_pred_dt,average='micro')
recall_dt = recall_score(y_test, y_pred_dt,average='micro')
f1_dt = f1_score(y_test, y_pred_dt,average='micro')
cm_dt = confusion_matrix(y_test, y_pred_dt)
print("Decision Tree:")
print(f"Accuracy: {accuracy_dt:.3f}")
print(f"Precision: {precision_dt:.3f}")
print(f"Recall: {recall_dt:.3f}")
print(f"F1-score: {f1_dt:.3f}")
print(f"Confusion matrix:\n{cm_dt}\n")

"""RANDOM FOREST"""

# Train and evaluate random forest
rf = RandomForestClassifier(random_state=0)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf,average='micro')
recall_rf = recall_score(y_test, y_pred_rf,average='micro')
f1_rf = f1_score(y_test, y_pred_rf,average='micro')
cm_rf = confusion_matrix(y_test, y_pred_rf)
print("Random Forest:")
print(f"Accuracy: {accuracy_rf:.3f}")
print(f"Precision: {precision_dt:.3f}")
print(f"Recall: {recall_dt:.3f}")
print(f"F1-score: {f1_dt:.3f}")
print(f"Confusion matrix:\n{cm_dt}\n")

"""GRADIENT BOOSTING"""

gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)
y_pred_gbc = gbc.predict(X_test)
accuracy_gbc = accuracy_score(y_test, y_pred_gbc)
precision_gbc = precision_score(y_test, y_pred_gbc,average='micro')
recall_gbc = recall_score(y_test, y_pred_gbc,average='micro')
f1_gbc = f1_score(y_test, y_pred_gbc,average='micro')
cm_gbc = confusion_matrix(y_test, y_pred_gbc)
print("Gradient Boosting Classifier:")
print(f"Accuracy: {accuracy_gbc:.3f}")
print(f"Precision: {precision_gbc:.3f}")
print(f"Recall: {recall_gbc:.3f}")
print(f"F1-score: {f1_gbc:.3f}")
print(f"Confusion matrix:\n{cm_gbc}\n")

"""SVM"""

svm = SVC()
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
precision_svm = precision_score(y_test, y_pred_svm,average='micro')
recall_svm = recall_score(y_test, y_pred_svm,average='micro')
f1_svm = f1_score(y_test, y_pred_svm,average='micro')
cm_svm = confusion_matrix(y_test, y_pred_svm)
print("Support Vector Machine Classifier:")
print(f"Accuracy: {accuracy_svm:.3f}")
print(f"Precision: {precision_svm:.3f}")
print(f"Recall: {recall_svm:.3f}")
print(f"F1-score: {f1_svm:.3f}")
print(f"Confusion matrix:\n{cm_svm}\n")