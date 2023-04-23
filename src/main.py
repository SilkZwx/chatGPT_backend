#!/usr/bin/env python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/summarize')
def summarize():
    return {"task": "summarize"}

@app.route('/translate')
def translate():
    return {"task": "translate"}

@app.route('/ocr')
def ocr():
    return {"name": "Ariyamada"}

@app.route('/')
def home():
    return {"root": "home"}

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
