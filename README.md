# TOPSIS Decision Tool - Chahat Jindal-102303831

[![PyPI Version](https://img.shields.io/pypi/v/Topsis-Chahat-102303831.svg)](https://pypi.org/project/Topsis-Chahat-102303831/)

A comprehensive TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) implementation for multi-criteria decision making.

## 📦 Official Package

The package is published on PyPI:  
https://pypi.org/project/Topsis-Chahat-102303831/1.0.2/

## 🚀 Installation

```bash
pip install Topsis-Chahat-102303831
```

## 📋 Features

- Multi-criteria decision making using TOPSIS method
- Web interface for easy file upload and analysis
- Email functionality to send results
- Supports CSV input files
- Calculates TOPSIS scores and ranks alternatives

## 🎯 What is TOPSIS?

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a decision-making method that helps rank alternatives based on their similarity to the ideal solution.

## 💻 Project Structure

**Chahat_102303831_Topsis**/ – Main project directory

topsis.py – Core TOPSIS implementation

setup.py – PyPI package configuration

README.md – Package documentation

**topsis_web**/ – Flask web application

app.py – Main Flask application

templates/ – HTML templates

topsis.py – TOPSIS logic for web app

## 🌐 Web Interface
```bash
The project includes a Flask-based web application for easy TOPSIS analysis:
cd topsis_web
pip install -r requirements.txt
python app.py
```

Then visit: `http://127.0.0.1:5000/`

## Features:

Upload Excel/CSV file with criteria data

Specify weights for each criterion

Define impacts (+ for benefit, - for cost)

Get TOPSIS scores and rankings

Receive results via email

<img width="1600" height="624" alt="image" src="https://github.com/user-attachments/assets/c57b1873-948a-4fe6-a6d5-56c8246da753" />
<img width="1279" height="865" alt="image" src="https://github.com/user-attachments/assets/007d5981-eab5-4832-8d42-61bfff484764" />



## 📊 Example Usage
Command Line:
```bash
topsis data.xlsx "1,1,1,1,1" "+,+,+,-,+" output.csv

Python:
from topsis import topsis

topsis("data.xlsx", [1,1,1,1,1], ['+','+','+','-','+'], "output.csv")
```

## 📝 Input & Ouput 

Your Excel/CSV file should be like this:


**Input**


<img width="495" height="317" alt="image" src="https://github.com/user-attachments/assets/935dfd6f-44d5-49cc-9896-08559653e2fe" />

**Output** 

<img width="645" height="219" alt="image" src="https://github.com/user-attachments/assets/3d10b688-aa47-4dc3-a99d-1e8d358b4f0c" />



## 📧 Email Setup

To use the email functionality:

Enable 2-Step Verification on your Gmail account
Generate an App Password from:
https://myaccount.google.com/apppasswords
Paste the 16-digit app password in app.py

## 🔒 Security

No hardcoded passwords in public repository

App password used only for SMTP authentication

## 👨‍💻 Author

Chahat Jindal
Roll Number: 102303831

## 📄 License

This project is developed for academic purposes under MIT License.
