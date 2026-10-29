from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/emotionDetector", methods = ["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid input! Please enter a statement."

    result = emotion_detector(text_to_analyze)

    if not result or result.get("dominant_emotion") is None:
        return "Invalid input! Please enter a valid statement."


    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is "
        f"{result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)