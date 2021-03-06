from flask import Flask
from flask import render_template
from flaskext.lesscss import lesscss


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    lesscss(app)
    app.run(host='0.0.0.0', debug=True)
