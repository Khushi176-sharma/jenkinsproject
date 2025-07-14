from flask import Flask

app = Flask(__flask__)

@app.route('/')
def home():
    return "Namesta, CI/CD with Jenkins!"
if __name__ == '__main__':
    app.run(host='0.0.0.0/', port=8080)
