# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 04:12:39 2023

@author: aafef
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


# Load the CSV file
df = pd.read_csv('SDHSTypes.csv')

# Drop rows with missing values for simplicity
df.dropna(inplace=True)

# Split the data into training and testing sets (80% train, 20% test)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Convert the "Tweet" column to numerical data using TF-IDF

n = 3  # Using bigrams as an example

vectorizer = TfidfVectorizer(min_df=0.0001, max_df=0.95, analyzer='word', lowercase=False, ngram_range=(1, n))
X_train = vectorizer.fit_transform(train_df['Tweet'])
X_test = vectorizer.transform(test_df['Tweet'])

y_train = train_df['HSTypes']
y_test = test_df['HSTypes']

X_train.shape, X_test.shape


# Define classifiers
classifiers = {
    'SVM': SVC(),
    'Gaussian Naive Bayes': GaussianNB(),
    'Multinomial Naive Bayes': MultinomialNB(),
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(),
    'K-Nearest Neighbors': KNeighborsClassifier()
}

# Store results
results = []

# ...

# Train and evaluate each classifier
for name, clf in classifiers.items():
    # Handle GaussianNB (which requires dense input)
    if name == "Gaussian Naive Bayes":
        clf.fit(X_train.toarray(), y_train)
        y_pred = clf.predict(X_test.toarray())
    else:
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1_weighted = f1_score(y_test, y_pred, average='weighted')
    f1_macro = f1_score(y_test, y_pred, average='macro')
    f1_micro = f1_score(y_test, y_pred, average='micro')
    recall = recall_score(y_test, y_pred, average='weighted')
    precision = precision_score(y_test, y_pred, average='weighted')
    
    results.append((name, accuracy, precision, recall, f1_weighted, f1_macro, f1_micro))
    
    
    # Constructing the results dataframe
    results_data = {
    "Classifier": [res[0] for res in results],
    "Accuracy": [res[1] for res in results],
    "Precision": [res[2] for res in results],
    "Recall": [res[3] for res in results],
    "F1-Score (Weighted)": [res[4] for res in results],
    "F1-Score (Macro)": [res[5] for res in results],
    "F1-Score (Micro)": [res[6] for res in results]
}

results_df = pd.DataFrame(results_data)

# Printing the results in a column manner
print(results_df.to_string(index=False))


# Plotting results
labels = [res[0] for res in results]
accuracies = [res[1] for res in results]
precisions = [res[2] for res in results]
recalls = [res[3] for res in results]
f1_scores = [res[4] for res in results]


# Extract results for new metrics
f1_scores_macro = [res[5] for res in results]
f1_scores_micro = [res[6] for res in results]

# Separate bar plots for each metric
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score (Weighted)', 'F1-Score (Macro)', 'F1-Score (Micro)']
values = [accuracies, precisions, recalls, f1_scores, f1_scores_macro, f1_scores_micro]

plt.figure(figsize=(20, 15))

for i, metric in enumerate(metrics):
    plt.subplot(3, 2, i + 1)  # 3 rows, 2 columns
    plt.barh(labels, values[i], color=['blue', 'green', 'red', 'cyan', 'magenta', 'yellow'])
    plt.xlabel(metric)
    plt.ylabel('Classifiers')
    plt.title(f'{metric} of Different Classifiers')
    plt.xlim(0, 1)  # Since all the metrics are in the range [0, 1]
    plt.tight_layout()

plt.show()
