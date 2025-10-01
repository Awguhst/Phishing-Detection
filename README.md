# Phishing Detection App 🔒

A machine learning-based phishing detection system built with **Scikit-learn** and **Streamlit**.  
The app classifies URLs as **phishing** or **legitimate** using text-based features.

---

## 🎥 Demo
![Streamlit app GIF](media/demo.gif)

---

## Overview
- **Data Preprocessing**: Tokenized and stemmed URLs to extract meaningful features.  
- **Feature Engineering**: Created text sequences and visualized patterns using word clouds.  
- **Modeling**: `CountVectorizer` + `LogisticRegression` pipeline.  
- **Validation**: Stratified 5-fold cross-validation; metrics include Accuracy, Precision, Recall, F1-score (~91%).  
- **Deployment**: Pickled model with interactive Streamlit interface for real-time predictions.
