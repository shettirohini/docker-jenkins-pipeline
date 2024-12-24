from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Docker Jenkins Pipeline Demo!"

@app.route("/status")
def status():
    return {"status": "Application is running smoothly"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

