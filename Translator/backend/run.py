from flask import Flask, jsonify, request, url_for, redirect
from pymongo import MongoClient
from flask_cors import CORS
from uuid import uuid1

app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb://localhost:27017/translator")
db = client.translator


@app.route('/')
def index():
    return redirect(url_for('translate'))


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
    app.run(debug=False)
