from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allnews')
def allnews():
    return render_template('allnews.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/info')
def info():
    return render_template('info.html')
