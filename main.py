from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('index.html')

app.run(debug=True)