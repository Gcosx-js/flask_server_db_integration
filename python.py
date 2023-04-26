import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/AddUser')
def index2():
    return render_template('page2.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    conn = sql.connect('log-reg.db')
    c = conn.cursor()
    c.execute('INSERT INTO USERS (Ad, Şifrə) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/data')
def get_data():
    conn = sql.connect('log-reg.db')
    c = conn.cursor()
    c.execute('SELECT * FROM USERS')
    data = c.fetchall()
    conn.close()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)