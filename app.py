from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    return score

@app.route("/", methods=["GET", "POST"])
def index():
    strength_label = None
    if request.method == "POST":
        password = request.form["password"]
        score = check_password_strength(password)
        strength_label = ["Very Weak", "Weak", "Moderate", "Fair", "Strong", "Very Strong"][score]
    return render_template("index.html", strength=strength_label)

if __name__ == "__main__":
    app.run(debug=True)
