from flask.ext.sqlalchemy import SQLAlchemy
from models.db import db_session
from flask import Flask, redirect
from flask import render_template
from flask import request
from cipher import encrypt_password, decrypt_password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/app.db'

db = SQLAlchemy(app)

from models import Password


@app.route('/', methods=['POST', 'GET'])
def view_passwords():
    passwords = Password.Password.query.all()
    password_dict = []

    for password in passwords:
        password_dict.append(
            {'id': password.id,
            'username': password.username,
            'platform': password.platform,
            'password': password.password}
            )

    if request.method == 'POST':
        password_dict = [decrypt_password(password, request.form.to_dict()['key']) for password in password_dict]

    return render_template('index.html.j2', passwords=password_dict)


@app.route('/create', methods=['POST', 'GET'])
def create_password():
    if request.method == 'POST':
        password_dict = request.form.to_dict()
        password_dict = encrypt_password(password_dict)
        newPassword = Password.Password(password_dict['username'], password_dict['platform'], password_dict['password'])
        db_session.add(newPassword)
        db_session.commit()

    return render_template('create.html.j2')

@app.route('/edit/<int:password_id>', methods=['POST', 'GET'])
def edit_password(password_id):
    password = Password.Password.query.filter_by(id=password_id).all()
    if password:
        if request.method == 'POST':
            password_dict = request.form.to_dict()
            password_dict = encrypt_password(password_dict)
            password[0].username = password_dict['username']
            password[0].platform = password_dict['platform']
            password[0].password = password_dict['password']

            db_session.commit()

        return render_template('edit.html.j2', password=password[0])
    else:
        return redirect('/', code=302)

@app.route('/delete/<int:password_id>', methods=['GET'])
def delete_password(password_id):
    password = Password.Password.query.filter_by(id=password_id).all()
    if password:
        db_session.delete(password[0])
        db_session.commit()

    return redirect('/', code=302)


if __name__ == '__main__':
    app.run()
