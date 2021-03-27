from flask import jsonify, request, make_response
from uuid import uuid1
from app import app, db


@app.route('/')
def index():
    response = make_response("<h1>Hello from Flask!</h1>")
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response


@app.route('/add-words/', methods=['POST'])
def add_words():
    req = request.json
    word = req.get('wordReq')
    translated = req.get('translateReq')
    word_trans = {
        'word': word,
        'translate': translated
    }
    db.words.insert_one(word_trans)
    return 'OK', 200


@app.route('/words/')
def get_words():
    words = db.words.find()
    output = {}
    for word in words:
        if "word" in word.keys():
            u_index = str(uuid1())
            data = {k: word.get(k) for k in ("word", "translate")}
            output[u_index] = data
    return jsonify(output)


@app.route('/translate/', methods=['POST'])
def translate():
    req = request.get_json()
    word = req.get('wordReq')
    sent_words = word.split()
    words = [db.words.find_one({'word': w}) for w in sent_words]
    translation = ' '.join(w.get('translate') for w in words)
    return jsonify({'translated': translation})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
