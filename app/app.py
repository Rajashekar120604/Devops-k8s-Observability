from flask import Flask, render_template, request, redirect, url_for, session
import logging
import os

app = Flask(__name__)

# Secret key (will later come from K8s Secret)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")

# Logging to stdout (K8s + ELK friendly)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Fake users (demo)
USERS = {
    "admin": "password123",
    "raj": "devops"
}

@app.route("/")
def home():
    if "user" in session:
        return f"""
        <h2>Welcome {session['user']} 🚀</h2>
        <a href="/logout">Logout</a>
        """
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if USERS.get(username) == password:
            session["user"] = username
            app.logger.info("Login successful for user: %s", username)
            return redirect(url_for("home"))

        app.logger.warning("Failed login attempt for user: %s", username)
        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
def logout():
    user = session.pop("user", None)
    app.logger.info("User logged out: %s", user)
    return redirect(url_for("login"))

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
