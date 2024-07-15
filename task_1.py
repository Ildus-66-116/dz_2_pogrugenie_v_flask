from pathlib import PurePath, Path
from flask import Flask, render_template, url_for, request, redirect, session, make_response
from werkzeug.utils import secure_filename
from markupsafe import escape
import requests

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    """Домашние задание 2"""
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('auth_email')
        response = make_response(redirect('/getcookie'))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    context = {
        'task': 'Авторизация'
    }
    return render_template('authorization.html', **context)


@app.route('/getcookie/')
def get_cookies():
    context = {
        'username': request.cookies.get('username'),
        'email': request.cookies.get('email')
    }
    return render_template('cook.html', **context)


@app.route('/logout/')
def logout():
    response = make_response(redirect('/authorization'))
    response.set_cookie('username', expires=0)
    response.set_cookie('email', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
