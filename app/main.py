from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home_view():
    cookie = request.args.get('c')
    if(cookie == None):
        cookie = "LOL"
    return "<h1>This is the cookie: {cookie}</h>"
