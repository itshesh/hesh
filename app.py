"""
Minimal Flask backend that can:
1. Serve the static site
2. Handle the contact form (POST /send)
Install:  pip install flask python-dotenv
Run:      python app.py
"""
from flask import Flask, request, jsonify, send_from_directory
import os, smtplib, ssl
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='.')

# ---------- CONFIG ----------
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT   = int(os.getenv("SMTP_PORT", 465))
EMAIL_ADDR  = os.getenv("EMAIL_ADDR")          # your email
EMAIL_PASS  = os.getenv("EMAIL_PASS")          # app password
TO_EMAIL    = os.getenv("TO_EMAIL", EMAIL_ADDR) # receive form msgs here

# ---------- ROUTES ----------
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/send", methods=["POST"])
def send():
    data    = request.get_json(force=True)
    name    = data.get("name", "")
    email   = data.get("email", "")
    message = data.get("message", "")

    if not all([name, email, message]):
        return jsonify({"error": "Missing fields"}), 400

    msg = EmailMessage()
    msg["Subject"] = f"Hesh.site contact from {name}"
    msg["From"]    = EMAIL_ADDR
    msg["To"]      = TO_EMAIL
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_ADDR, EMAIL_PASS)
            server.send_message(msg)
        return jsonify({"status": "sent"}), 200
    except Exception as e:
        print("Mail error:", e)
        return jsonify({"error": "Message not sent"}), 500

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)