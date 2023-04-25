import sys

sys.path.append("./src")
from main import app

def test_convert_text(uri):
    # テスト用のデータを用意
    text = "The present volume consists of chapters by participants in \
    the Language and Space conference held in Tucson, Arizona, 16-19 March 1994. \
    In most cases the chapters have been written to reflect the numerous interactions at the conference, \
    and for that reason we hope the book is more than just a compilation of isolated papers. \
    The conference was truly interdisciplinary, including such domains as neurophysiology, \
    neuropsychology, psychology, anthropology, cognitive science, and linguistics. Neu- \
    ral mechanisms, developmental processes, and cultural factors were all grist for the \
    mill, as were semantics, syntax, and cognitive maps."

    data = {"text": text}
    # テスト対象のエンドポイントをリクエスト
    client = app.test_client()
    response = client.post(uri, json=data)
    result = response.get_json()["result"]
    print(result)
    # レスポンスのステータスコードが200であることを検証
    assert response.status_code == 200

    assert isinstance(result, str)

if __name__ == "__main__":
    test_convert_text("/summarize")
    test_convert_text("/translate")


