# Phishing Detection App 🔒

A machine learning-based phishing detection system built with **Scikit-learn** and **Streamlit**.  
The app classifies URLs as **phishing** or **legitimate** using text-based features.

---

## What is Phishing?
Phishing is a type of cyber attack where attackers trick users into revealing sensitive information (like usernames, passwords, or financial details) by pretending to be a trustworthy entity.  
It is commonly carried out through deceptive emails, websites, or messages that mimic legitimate sources.

---

## 🎥 Demo
![Streamlit app GIF](media/demo.gif)

---

## Overview
The project begins with preprocessing the URL data, where URLs are tokenized and stemmed to extract features. Feature engineering follows, creating text sequences and visualizing patterns with word clouds to better distinguish phishing URLs from legitimate ones.

A machine learning pipeline is built using `CountVectorizer` and `LogisticRegression`. The model is evaluated with stratified 5-fold cross-validation, achieving approximately 91% across Accuracy, Precision, Recall, and F1-score.

The trained model is saved as a pickled file (`phishing.pkl`) for easy loading and prediction in a deployment setting.
