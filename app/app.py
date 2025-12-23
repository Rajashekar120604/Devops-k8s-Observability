from flask import Flask, request, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import logging
import json

# 🔥 IMPORTANT: raw JSON logs (no prefixes)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    force=True
)

def log_event(level, event, **kwargs):
    logging.log(level, json.dumps({
        "event": event,
        **kwargs
    }))

app = Flask(__name__)

login_attempts = Counter(
    "login_attempts_total",
    "Total number of login attempts",
    ["result"]
)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            login_attempts.labels(result="success").inc()
            log_event(logging.INFO, "login_success", username=username)
            return render_template("login.html", error="Login successful")
        else:
            login_attempts.labels(result="failure").inc()
            log_event(logging.WARNING, "login_failure", username=username)
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
