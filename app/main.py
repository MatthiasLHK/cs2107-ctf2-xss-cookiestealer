from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home_view():
    print("Hello in console")
    return "<h1>Welcome to Geeks for Geeks</h>"
