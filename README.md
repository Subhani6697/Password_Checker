# Password_Checker
This is a simple Flask-based web application that checks password strength using HTML, CSS, and JavaScript. It runs locally in a browser.

📂 Project Structure
PasswordCheckerApp/
 ├── static/
 │    ├── script.js
 │    └── style.css
 ├── templates/
 │    └── index.html
 ├── app.py
 └── README.md

🚀 Features

Strong password checking rules

Visual UI with HTML, CSS, JS

Flask backend

Runs locally in browser

🛠️ Requirements
Tool	Version	Notes
Python	3.x	Required
Flask	Latest	Install via pip
Browser	Any modern browser	To open UI
📦 Install Dependencies

Open terminal / CMD inside your project directory and run:

pip install flask


If needed:

python -m pip install flask

▶️ Run Application

Inside PasswordCheckerApp folder:

python app.py

🌍 Access in Browser

Once running, go to:

http://127.0.0.1:5000/

🧪 Verify Installation

Check Python + Pip path if Flask doesn’t install:

where python
where pip

🔐 SSH + Git (Short Guide)

Check if you already have SSH keys:

ls -al ~/.ssh


Generate new key (if needed):

ssh-keygen -t ed25519 -C "your_email@example.com"


Start SSH agent and add key:

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519


Add key to GitHub:

Copy key

cat ~/.ssh/id_ed25519.pub


Go to GitHub → Settings → SSH & GPG Keys → Add Key

Test connection

ssh -T git@github.com

✅ Git Commands to Push
git init
git add .
git commit -m "Initial password checker app"
git branch -M main
git remote add origin git@github.com:USERNAME/REPO.git
git push -u origin main

📌 Notes

Keep your SSH private key safe

Use venv for clean Python setup (optional)

🙌 Credits

Created as a simple Flask practice project.