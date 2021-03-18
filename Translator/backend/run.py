from app import app, db
from flask import jsonify, request, url_for, redirect
from uuid import uuid1

@app.route('/')
def index():
    return redirect(url_for('translate'))


@app.route('/addwords/', methods=['POST'])
def addwords():
    req = request.json
    word = req.get('word')
    translated = req.get('translate')
    word_trans = {
        'word': word,
        'translate': translated
    }
    db.words.insert_one(word_trans)
    return ('OK', 200)


@app.route('/words/')
def get_words():
    words = db.words.find()
    output = {}
    for word in words:
        if "word" in word.keys():
            index = str(uuid1())
            data = {k:word.get(k) for k in ("word", "translate")}
            output[index] = data
    return jsonify(output)


@app.route('/translate/', methods=['POST'])
def translate():
    req = request.get_json()
    word = req['word']
    words = db.words.find_one({'word': word})
    translation = words.get('translate')
    return jsonify({'translated': translation})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
