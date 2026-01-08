
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/healthz")
def healthz():
    return jsonify(status="ok"), 200

@app.route("/")
def root():
    return jsonify(service="flask-hello", message="Hello OpenShift!"), 200

if __name__ == "__main__":
    # S2I e OpenShift gostam da porta 8080
    app.run(host="0.0.0.0", port=8080)

