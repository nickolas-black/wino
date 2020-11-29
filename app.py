import flask
from flask import render_template
import pickle

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        temp = 1
        with open('modelw1.pkl', 'rb') as fh:
            loaded_model = pickle.load(fh)
        a1 = float(flask.request.form['a1'])
        a2 = float(flask.request.form['a2'])
        a3 = float(flask.request.form['a3'])
        a4 = float(flask.request.form['a4'])
        a5 = float(flask.request.form['a5'])
        a6 = float(flask.request.form['a6'])
        a7 = float(flask.request.form['a7'])
        a8 = float(flask.request.form['a8'])
        a9 = float(flask.request.form['a9'])
        a10 = float(flask.request.form['a10'])
        a11 = float(flask.request.form['a11'])
        temp = loaded_model.predict([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]])
        if temp == 0:
            temp = "WORST RED WINE"
        if temp == 1:
            temp = "VERY GOOD RED WINE"
        return render_template('main.html', result=temp)


if __name__ == '__main__':
    app.run()
