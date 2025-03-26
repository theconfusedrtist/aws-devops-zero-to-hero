from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Namaste india!!!!!!!!!!!!!!!!!!'

if __name__ == '__main__':
    app.run()

