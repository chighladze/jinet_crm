from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '12121121'


if __name__ == '__main__':
    app.run()
