import base64
import io
from PIL import Image
import sys

sys.path.append("./src")
from main import app


def test_ocr():
    client = app.test_client()
    image_path = "image/sample.jpg"

    with open(image_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()

    data = {
        "post_imgs": [img_base64]
    }

    response = client.post('/ocr', json=data)
    assert response.status_code == 200

    results = response.get_json()["results"]
    print(results)
    assert len(results) == 1

    txt = results[0]
    assert isinstance(txt, str)
    assert len(txt) > 0


if __name__ == "__main__":
    test_ocr()

