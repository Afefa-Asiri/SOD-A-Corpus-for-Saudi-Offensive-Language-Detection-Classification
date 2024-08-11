SOD: A Corpus for Saudi Offensive Language Detection Classification
This repository contains the code and resources used in the research paper titled "A Corpus for Saudi Offensive Language Detection Classification" by Afefa Asiri and Mostafa Saleh.

Overview
This study introduces the Saudi Offensive Dialectal dataset (SOD), consisting of over 24,000 tweets annotated across three levels: offensive or non-offensive, with offensive tweets further categorized as general insults, hate speech, or sarcasm. The dataset includes deeper analysis subtypes related to sports, religion, politics, race, and violence.

The research demonstrates the effectiveness of using a specialized dialectal dataset for offensive language detection, achieving an F1-Score of 84% with traditional models and up to 91% with data augmentation techniques.

Repository Contents
This repository, named SOD-A-Corpus-for-Saudi-Offensive-Language-Detection-Classification, includes all the codes required to replicate the data collection, annotation, and analysis processes described in the paper. The main components are:

Data Collection Scripts:

Scripts for scraping data from X (formerly Twitter) using the snscrape Python package. These scripts were used to collect over 24,000 tweets in the Saudi dialect.
Data Annotation Guidelines:

A guide detailing the hierarchical annotation process, including classification into offensive and non-offensive categories, further categorization, and the exploration of specific hate speech subtypes.
Exploratory Data Analysis (EDA) Scripts:

Scripts used to perform EDA, including token analysis, unigram, bigram, and trigram analysis, and emoji sentiment analysis.
Machine Learning and Deep Learning Models:

Implementation of various machine learning, deep learning, and transformer models (including AraBERT) used in the study, along with code for training, evaluation, and result analysis.
Data Augmentation Techniques:

Code implementing different data augmentation strategies to address the issue of dataset imbalance, which improved the model performance.
Usage
Data Collection:

To replicate the data collection process, navigate to the data_collection/ directory and run the provided scripts using the snscrape package.
Data Annotation:

Refer to the annotation_guidelines/ directory for detailed instructions and examples of the annotation process.
Model Training and Evaluation:

The models/ directory contains scripts for training the machine learning, deep learning, and transformer models. Follow the instructions in the script comments to train and evaluate the models on your local machine or a cloud platform.
Data Augmentation:

Use the scripts in the data_augmentation/ directory to apply augmentation techniques to your dataset.
License
This project is licensed under the MIT License.

Contact
For any questions or issues, please contact the authors at:

Afefa Asiri: aasiri0410@stu.kau.edu.sa
