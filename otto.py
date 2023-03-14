from flask import Flask, render_template
app = Flask(__name__)

import datetime

@app.route('/')

def index():
  return render_template("index7.html", Ora=datetime.datetime.utcnow())


@app.route('/mappa')

def mappa():
  return render_template("index7.html", Ora=datetime.datetime.utcnow())

@app.route('/mappa600')

def mappa600():
  return render_template("index7.html", dimensione = 600)

@app.route('/mappa800')

def mappa800():
  return render_template("index7.html", dimensione = 800)

@app.route('/mappa1000')

def mappa1000():
  return render_template("index7.html", dimensione = 1000)

@app.route('/mappa/<width>')

def width(width):
  return render_template("index7.html", dimensione = width)
if __name__ == '__main__':#sempre alla fine queste due righe
  app.run(host='0.0.0.0', port=3245, debug=True)#sempre alla fine queste due righe
