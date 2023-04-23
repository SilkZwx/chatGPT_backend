from flask import Flask
import os

app = Flask(__name__)

@app.route('/summarize')
def home():
    return {"task": "summarize"}

@app.route('/translate')
def home():
    return {"task": "translate"}

@app.route('/ocr')
def home():
    return {"name": "Ariyamada"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
