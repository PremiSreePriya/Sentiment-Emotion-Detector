# Sentiment-Emotion-Detector
A Flask-based web application that analyzes a single sentence to detect sentiment (positive/negative) and emotion (joy, sadness, anger, etc.) using Hugging Face Transformers, with real-time mental wellness suggestions.

✨FEATURES

   💬Identifies Sentiment: Positive or Negative

   🔍Detects Emotion: Joy, Sadness, Anger, Fear, Love, or Surprise

   📊Shows confidence score and a helpful suggestion

🤖MODELS USED

🔗Sentiment: distilbert-base-uncased-finetuned-sst-2-english

🔗Emotion: j-hartmann/emotion-english-distilroberta-base (requires PyTorch)

⚙️TECH STACK

🔁Flask – for the web app

🤗Transformers – for NLP models

🔥 Torch (PyTorch) – required backend for the emotion model

🖥 HTML&CSS – for UI templates

🚀 HOW TO RUN THE APPLICATION
1. 🔧 Install Requirements
   
   pip install flask transformers torch

2. ▶️ Start the App

   python app.py
   
3. 🌐 Access in Browser

   Open your browser and go to:
http://127.0.0.1:5000

✅ SAMPLE RESULT

Input: I feel really low and anxious.

Output:

 Sentiment: NEGATIVE
 
 Emotion:  FEAR
 
 Confidence: 0.94
 
 Suggestion: Try grounding exercises and talk to someone you trust.

