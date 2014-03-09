from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'A simple marvel app using the marvelpy library.'

if __name__ == '__main__':
    app.run()
