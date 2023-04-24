#!/usr/bin/env python
from flask import Flask, request
import os
from ocr.ocr import ocr as ocr_tesseract

app = Flask(__name__)

@app.route('/summarize')
def summarize():
    return {"task": "summarize"}

@app.route('/translate')
def translate():
    return {"task": "translate"}

@app.route('/ocr', methods=["POST"])
def ocr():
    post_imgs = request.json["post_imgs"]
    txts = []
    for i, img_base64 in enumerate(post_imgs):
        # Base64データをバイナリに変換
        img_binary = io.BytesIO(base64.b64decode(img_base64))
        # PILライブラリを使って画像を読み込み
        img = Image.open(img_binary)
        
        txt = ocr(img)
        txts.append(txt)

    return {"results": txts}

@app.route('/')
def home():
    return {"root": "home"}

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    # print(ocr_tesseract("image/sample.jpg"))
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
