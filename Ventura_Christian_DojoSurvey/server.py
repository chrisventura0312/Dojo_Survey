from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET','POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['news'] = request.form['news']
    session['color'] = request.form['color']
    return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
