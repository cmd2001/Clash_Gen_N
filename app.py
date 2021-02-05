# web interface based on flask

from flask import Flask
from work import work

app = Flask(__name__)


@app.route('/')
def root():
    return work()


if __name__ == '__main__':
    app.run()
