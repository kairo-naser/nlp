"""
Complete NLP Pipeline Module
============================
Comprehensive Natural Language Processing pipeline for text classification tasks.

Features:
- Text preprocessing and cleaning
- Tokenization and linguistic analysis
- TF-IDF vectorization
- Gradient Boosting classification
- Model evaluation and visualization

Author: NLP Lab
Date: 2024
"""

import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)



class NLPPipeline:
    """Complete NLP Pipeline for text processing and classification"""
    
    def __init__(self, max_features=500, test_size=0.2, random_state=42):
        """
        Initialize the NLP pipeline
        
        Args:
            max_features: Maximum number of features for TF-IDF
            test_size: Proportion of data for testing
            random_state: Random seed for reproducibility
        """
        self.max_features = max_features
        self.test_size = test_size
        self.random_state = random_state
        
        self.tfidf_vectorizer = None
        self.label_encoder = None
        self.gbt_model = None
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess_text(self, text):
        """Clean and preprocess text data"""
        if pd.isna(text):
            return ""
        
        # Convert to lowercase
        text = str(text).lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    def tokenize_and_clean(self, text):
        """Tokenize text and remove stopwords"""
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.lower() not in self.stop_words and word.isalpha()]
        return tokens
    
    def fit(self, X, y):
        """
        Fit the NLP pipeline
        
        Args:
            X: Text data (Series or array-like)
            y: Target labels (Series or array-like)
            
        Returns:
            Dictionary with model training results
        """
        # Preprocess text
        X_processed = pd.Series(X).apply(self.preprocess_text)
        
        # Vectorize text using TF-IDF
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=self.max_features,
            stop_words='english'
        )
        X_vectorized = self.tfidf_vectorizer.fit_transform(X_processed)
        
        # Encode labels
        self.label_encoder = LabelEncoder()
        y_encoded = self.label_encoder.fit_transform(y)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_vectorized, y_encoded,
            test_size=self.test_size,
            random_state=self.random_state
        )
        
        # Train model
        self.gbt_model = GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=self.random_state
        )
        self.gbt_model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.gbt_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        return {
            'train_size': X_train.shape[0],
            'test_size': X_test.shape[0],
            'accuracy': accuracy,
            'report': classification_report(y_test, y_pred),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
    
    def predict(self, X):
        """Make predictions on new data"""
        X_processed = pd.Series(X).apply(self.preprocess_text)
        X_vectorized = self.tfidf_vectorizer.transform(X_processed)
        y_pred_encoded = self.gbt_model.predict(X_vectorized)
        y_pred = self.label_encoder.inverse_transform(y_pred_encoded)
        return y_pred
    
    def predict_proba(self, X):
        """Get prediction probabilities"""
        X_processed = pd.Series(X).apply(self.preprocess_text)
        X_vectorized = self.tfidf_vectorizer.transform(X_processed)
        return self.gbt_model.predict_proba(X_vectorized)
    
    def get_feature_importance(self, top_n=20):
        """Get top N important features"""
        importance = self.gbt_model.feature_importances_
        features = self.tfidf_vectorizer.get_feature_names_out()
        
        top_indices = np.argsort(importance)[-top_n:][::-1]
        return list(zip(features[top_indices], importance[top_indices]))
    
    def get_classes(self):
        """Get class labels"""
        return self.label_encoder.classes_


# Example usage
if __name__ == "__main__":
    # Load data
    df = pd.read_csv('./cybersecurity_attacks.csv', encoding='latin-1')
    
    # Initialize pipeline
    pipeline = NLPPipeline(max_features=500, test_size=0.2)
    
    # Fit pipeline (adjust column names as needed)
    text_col = 'description'  # Change to your text column
    label_col = 'attack_type'  # Change to your label column
    
    if text_col in df.columns and label_col in df.columns:
        results = pipeline.fit(df[text_col], df[label_col])
        
        print("Model Performance:")
        print(f"Accuracy: {results['accuracy']:.4f}")
        print(f"\nClassification Report:\n{results['report']}")
        
        # Make predictions on new data
        new_text = pd.Series(["suspicious network activity detected"])
        predictions = pipeline.predict(new_text)
        print(f"\nPrediction: {predictions[0]}")
    else:
        print(f"Columns not found. Available columns: {df.columns.tolist()}")
