from flask import Flask, render_template, request
import re

app = Flask(__name__)

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password1",
    "admin", "welcome", "letmein", "iloveyou", "monkey", "football",
    "test", "login", "user", "guest", "root", "default"
}

def has_sequence(s):
    # Detect simple sequences like abc, 123, qwerty
    sequences = ["0123", "1234", "2345", "3456", "4567", "5678", "6789",
                 "abcd", "abc", "bcd", "cde", "def", "efg", "fgh", "qwerty",
                 "asdf", "zxcv", "pass", "test", "admin"]
    s = s.lower()
    return any(seq in s for seq in sequences)

def check_password_strength(password):
    pwd = password.strip()
    score = 0
    length = len(pwd)

    # Rule 1: Minimum length
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        return "Very Weak"

    # Rule 2: Complexity — uppercase, lowercase, digits, symbols
    upper = bool(re.search(r"[A-Z]", pwd))
    lower = bool(re.search(r"[a-z]", pwd))
    digit = bool(re.search(r"[0-9]", pwd))
    symbol = bool(re.search(r"[^A-Za-z0-9]", pwd))
    diversity = sum([upper, lower, digit, symbol])
    score += diversity

    # Rule 3: Penalize easy or common patterns
    if pwd.lower() in COMMON_PASSWORDS:
        return "Very Weak"

    if has_sequence(pwd):
        score -= 2

    # Rule 4: Penalize repetition (aaa, 111, etc.)
    if re.search(r"(.)\1{2,}", pwd):
        score -= 1

    # Rule 5: Reward good entropy (random-looking + long)
    if diversity == 4 and length >= 14 and not has_sequence(pwd):
        score += 2

    # Clamp score between 0–7
    score = max(0, min(score, 7))

    labels = [
        "Very Weak",      # 0
        "Weak",           # 1
        "Weak",           # 2
        "Moderate",       # 3
        "Fair",           # 4
        "Strong",         # 5
        "Very Strong",    # 6
        "Enterprise-Grade" # 7
    ]

    return labels[score]

@app.route("/", methods=["GET", "POST"])
def index():
    strength_label = None
    if request.method == "POST":
        password = request.form["password"]
        strength_label = check_password_strength(password)
    return render_template("index.html", strength=strength_label)

if __name__ == "__main__":
    app.run(debug=True)
