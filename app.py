from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------- TOPSIS FUNCTION ----------
def topsis(input_file, weights, impacts, output_file):
    data = pd.read_excel(input_file)
    matrix = data.iloc[:, 1:].astype(float)

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != len(impacts):
        raise ValueError("Number of weights must be equal to number of impacts")

    for i in impacts:
        if i not in ['+', '-']:
            raise ValueError("Impacts must be either + or -")

    norm = np.sqrt((matrix ** 2).sum())
    normalized = matrix / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)

# ---------- EMAIL FUNCTION ----------
def send_email(to_email, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "ccjindal1312@gmail.com"
    msg["To"] = to_email
    msg.set_content("Please find attached the TOPSIS result file.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            "ccjindal1312@gmail.com",
            "lidusmthcgsvcmtz"
        )
        server.send_message(msg)

# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]
    email = request.form["email"]

    # Email validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email format"

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

    file.save(input_path)

    try:
        topsis(input_path, weights, impacts, output_path)
        send_email(email, output_path)
    except Exception as e:
        return str(e)

    return "Result sent successfully to your email!"

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
