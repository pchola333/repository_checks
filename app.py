import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM checks;')
    checks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', checks=checks)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        day = request.form['day']
        amount = int(request.form['amount'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO checks (name, day, amount, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (name, day, amount, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))


    return render_template('create.html')
