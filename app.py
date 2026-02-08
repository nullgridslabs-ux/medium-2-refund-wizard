# medium-2-refund-wizard/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/")
def index():
    return """
<h2>Refund Workflow Service</h2>
<p>Multi-step refund processing backend.</p>
<ul>
<li>POST /refund/start</li>
<li>POST /refund/confirm</li>
<li>GET /health</li>
</ul>
<p>Refunds are processed through a wizard style flow.</p>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/refund/start", methods=["POST"])
def start():
    return jsonify({"refund_id":"R123"})

@app.route("/refund/confirm", methods=["POST"])
def confirm():
    return jsonify({"status":"refunded","flag":FLAG})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
