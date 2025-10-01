# Phishing Detection App 🔒

A machine learning-based phishing detection system built with **Scikit-learn** and **Streamlit**.  
The app classifies URLs as **phishing** or **legitimate** using text-based features.

---

## What is Phishing?
Phishing is a type of cyber attack where attackers trick users into revealing sensitive information (like usernames, passwords, or financial details) by pretending to be a trustworthy entity.  
It is commonly carried out through deceptive emails, websites, or messages that mimic legitimate sources.

---

## 🚀 Demo
![Streamlit app GIF](media/demo.gif)

---

## Overview
- **Data Preprocessing**: Tokenized and stemmed URLs to extract features.  
- **Feature Engineering**: Created text sequences and visualized patterns using word clouds.  
- **Model**: `CountVectorizer` + `LogisticRegression` pipeline.  
- **Validation**: Stratified 5-fold cross-validation; metrics include Accuracy, Precision, Recall, F1-score (~91%).  
- **Deployment**: The trained model is saved as a pickled file (`phishing.pkl`) for easy loading and prediction.
