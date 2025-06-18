from flask import Flask, render_template, request
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load models
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1  # return top emotion
)

# Suggestion logic
def get_suggestion(sentiment, emotion):
    emotion = emotion.lower()
    if emotion == "sadness":
        return "Listening to uplifting music or journaling may help you process sadness."
    elif emotion == "anger":
        return "Take deep breaths, go for a walk, or practice mindfulness to calm down."
    elif emotion == "fear":
        return "Try grounding exercises and speak to someone you trust."
    elif emotion == "joy":
        return "Share your joy with others and celebrate your moment!"
    else:
        return "Stay balanced and take care of your well-being."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "analyze":
            text = request.form["text"]
            sentiment_result = sentiment_pipeline(text)[0]
            emotion_result = emotion_pipeline(text)[0][0]  # <- This is important

            sentiment = sentiment_result["label"]
            emotion = emotion_result["label"]
            suggestion = get_suggestion(sentiment, emotion)

            result = {
                "sentiment": sentiment,
                "emotion": emotion,
                "score": round(sentiment_result['score'], 2),
                "suggestion": suggestion
            }

        elif action == "clear":
            result = None  # this hides the result box

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    user_input = ""  # Track the input to retain or clear it

    if request.method == "POST":
        action = request.form.get("action")

        if action == "analyze":
            user_input = request.form.get("text", "")
            if user_input.strip() != "":
                sentiment_result = sentiment_pipeline(user_input)[0]
                emotion_result = emotion_pipeline(user_input)[0]

                sentiment = sentiment_result["label"]
                emotion = emotion_result["label"]
                suggestion = get_suggestion(sentiment, emotion)

                result = {
                    "sentiment": sentiment,
                    "emotion": emotion,
                    "score": round(sentiment_result["score"], 2),
                    "suggestion": suggestion
                }

        elif action == "clear":
            # Reset both input and result
            user_input = ""
            result = None

    return render_template("index.html", result=result, user_input=user_input)
