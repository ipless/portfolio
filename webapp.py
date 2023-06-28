import psycopg2
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

conn = psycopg2.connect(database="service_db", user="postgres", password="qwe123", host="localhost", port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.user WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            try:
                return render_template('account.html', password=records[0][3], login=records[0][2], full_name=records[0][1])
            except IndexError:
                return render_template('error.html')
        elif request.form.get("registration"):
            return redirect("/registration/")
    return render_template('login.html')

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        cursor.execute('SELECT * FROM service.user;')
        users = list(cursor.fetchall())
        for user in users:
            if str(user[2]) == str(login):
                return render_template('error.html')
        if login == '' or name == '' or password == '':
            return render_template('error.html')
        cursor.execute('INSERT INTO service.user (full_name, login, password) VALUES(%s, %s, %s);',(str(name), str(login), str(password)))
        conn.commit()
        return redirect('/login/')
    return render_template('registration.html')

