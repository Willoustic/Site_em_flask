from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

app.run(debug=True)