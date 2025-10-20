import os
from flask import Flask, request, jsonify, render_template
import openai
import requests

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)
chat_history = []  # Simple memory for the session

# Function to fetch Wikipedia summary
def fetch_wikipedia_summary(query):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        response = requests.get(url)
        data = response.json()
        if "extract" in data:
            return data["extract"]
        return ""
    except:
        return ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsoni
