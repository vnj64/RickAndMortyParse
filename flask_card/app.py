from fileinput import filename
from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/udjin')
def udjin():
    return render_template('udjin.html')

@app.route('/vankuver')
def vankuver():
    return render_template('vankuver.html')