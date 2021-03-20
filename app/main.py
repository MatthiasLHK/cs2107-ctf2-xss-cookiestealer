from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home_view():
    cookie = request.args.get('c')
    print(cookie)
    return "<h1>Welcome to Geeks for Geeks</h>"
