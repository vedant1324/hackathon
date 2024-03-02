import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys

# Read Data
df = pd.read_csv('Crop_recommendation.csv')

# Splitting Data
x = df.drop('label', axis=1)
y = df['label']

# Split test and train data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, random_state=1)

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# Accuracy of Model
from sklearn.metrics import accuracy_score
logistic_acc = accuracy_score(y_test, y_pred)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
model_2 = DecisionTreeClassifier(criterion='entropy', max_depth=6, random_state=2)
model_2.fit(x_train, y_train)
y_pred_2 = model_2.predict(x_test)

# Accuracy
decision_acc = accuracy_score(y_test, y_pred_2)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
model_3 = GaussianNB()
model_3.fit(x_train, y_train)
y_pred_3 = model_3.predict(x_test)

# Accuracy
naive_bayes_acc = accuracy_score(y_test, y_pred_3)

# Random Forest
from sklearn.ensemble import RandomForestClassifier
model_4 = RandomForestClassifier(n_estimators=25, random_state=2)
model_4.fit(x_train, y_train)
y_pred_4 = model_4.predict(x_test)

# Accuracy
random_fore_acc = accuracy_score(y_test, y_pred_4)

# Our Data
if len(sys.argv) == 8:  # Check if 7 command-line arguments are provided
    arr = [float(arg) for arg in sys.argv[1:]]  # Extract values starting from index 1
    input_data = [arr]
    acc = model_4.predict(input_data)
    print(acc)
else:
    print("Error: Please provide 7 command-line arguments.")

with open('mlmodel.pkl', 'wb') as f:
    pickle.dump(model_4, f)
