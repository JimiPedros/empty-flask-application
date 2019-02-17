from flask import Flask, render_template # url_for, redirect, request, flash, escape, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.secret_key = "big secret"

if __name__ == "__main__":
    app.debug = True
    app.run()
