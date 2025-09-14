# Phishing Detection App

A machine learning-based phishing detection app built with **Streamlit** and **Scikit-learn**. This app helps identify whether a URL is phishing or not by analyzing its textual features.

---

## 🎥 **Demo**
![Streamlit app GIF](media/demo.gif)

---

## What is Phishing?

**Phishing** is a type of cyber attack where attackers trick users into divulging sensitive information (like usernames, passwords, or financial details) by pretending to be a trustworthy entity. Phishing is commonly done through deceptive emails, websites, or messages that resemble legitimate sources.

---

## Model Overview

The phishing detection model is trained using a **Logistic Regression** classifier with text-based features extracted from URLs. The model is built with the following pipeline:

1. **Text Tokenization**: Extracts words from the URL using a custom tokenizer.
2. **Logistic Regression**: Classifies URLs as phishing or legitimate based on the extracted features.

The trained model is saved as a **pickled** file (`phishing_model.pkl`) for easy loading and prediction.

---
