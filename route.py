from flask import render_template
from myapp import app

@app.route('/')
def login():
   return render_template('index.html')