from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_surya():
    return "<h1>Hello Surya!</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
