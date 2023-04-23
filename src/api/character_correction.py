import openai #OpenAIのAPIを利用するために必要
import time

def character_correction():
    res = openai.ChatCompletion.create( # resにAPIのレスポンスが格納される
        model="gpt-3.5-turbo", # ChatGPTのモデルを選択する 後述➀
        messages=[
            {
                "role": "system", # ChatGPTの設定・状況を指定
                "content": "summarize it" # 日本語で返答するよう設定・状況づけ
            },
            {
                "role": "user", # roleをsystem, user, assistantの3種類から選択する 後述➁
                "content": "summarize this text. \n\"an Si\
                    Men, =\
                    317\
                    Preface\
                    The present volume consists of chapters by participants in the Language and Space\
                    conference held in Tucson, Arizona, 16-19 March 1994. In most cases the chapters\
                    have been written to reflect the numerous interactions at the conference, and for that\
                    reason we hope the book is more than just a compilation of isolated papers. The\
                    conference was truly interdisciplinary, including such domains as neurophysiology,\
                    neuropsychology, psychology, anthropology, cognitive science, and linguistics. Neu-\
                    ral mechanisms, developmental processes, and cultural factors were all grist for the\
                    mill, as were semantics, syntax, and cognitive maps.\
                    \
                    The conference had its beginnings in a seemingly innocent conversation in 1990\
                    between two new colleagues at the University of Arizona (Bloom and Peterson), who\
                    wondered about the genesis of left-right confusions. One of them (M. A. P.) assumed\
                    that these confusions reflected a language problem; the other (P. B.) was quite certain\
                    that they reflected a visual perceptual problem. Curiously, it was the perception\
                    researcher who saw this issue as being mainly linguistic and the language researcher\
                    who saw it as mainly perceptual. In true academic form they decided that the best\
                    way to arrive at an answer would be to hold a seminar on the topic, which they did\
                    the very next year. Their seminar on language and space was attended by graduate\
                    students, postdoctoral fellows, and many faculty members from a variety of depart-\
                    ments. Rather than answering the question that led to its inception, the seminar\
                    raised other questions: How do we represent space? What aspects of space can we\
                    talk about? How do we learn to talk about space? And what role does culture play in\
                    all these matters? One seminar could not explore all of these issues in any depth; an\
                    enlarged group of interested colleagues (the four coeditors) felt that perhaps several\
                    \
                    workshops might.\
                    \
                    The Cognitive Neuroscience Program at the University of Arizona, in collabora-\
                    tion with the Cognitive Science Program and the Psychology Department, sponsored\
                    two one-day workshops on the relations between space and language. Although\
                    stimulating and helpful, the workshops gave rise to still other questions: How does\
                    \
                    ee\"" # 聞きたい質問や行いたい指示を入力する
            },
        ],
    )
    print(res) # レスポンス（res）を出力する
    print(res['choices'][0]['message']['content']) # レスポンス（res）の中から返答のみを指定して出力する

if __name__ == "__main__":
    openai.api_key = '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' # 取得したAPIkeyをXXXと置き換える
    start = time.perf_counter()
    character_correction()
    end = time.perf_counter()
    print(start, end)
    print(end-start)