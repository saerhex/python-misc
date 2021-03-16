from app import app


@app.route("/")
def index():
    return "HI there!"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
