# medium-2-refund-wizard/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/refund/start", methods=["POST"])
def start():
    return jsonify({"refund_id":"R123"})

@app.route("/refund/confirm", methods=["POST"])
def confirm():
    # BUG: no validation of previous step
    return jsonify({"status":"refunded","flag":FLAG})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
