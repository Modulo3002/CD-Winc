from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CD CD CD Hello, World ! TEST TEST TEST TEST1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
