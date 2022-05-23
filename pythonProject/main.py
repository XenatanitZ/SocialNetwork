import sys
from urllib import response

from PyQt5 import QtWidgets
from flask import Flask, redirect, url_for, request, make_response, jsonify, render_template
from scipy.sparse import data
from sqlalchemy import text, create_engine, exc
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import requests
from Interface import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyodbc

Base = automap_base()

engine = create_engine(
    'mssql+pyodbc://sa:fh[fyutkmcr1978@arch.designer/SocialNetwork?driver=ODBC+Driver+17+for+SQL+Server')
conn = engine.connect()

Session = sessionmaker(bind=engine)
Base.prepare(engine, reflect=True)

users = Base.classes.Users
user_profile = Base.classes.User_profile

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def reg():
    session = Session()
    if request.method == 'GET':
        try:
            user = users(login=request.args.get('login'), password=request.args.get('password'))
            session.add(user)
            session.flush()

            profile = user_profile(user_id=user.user_id)
            session.add(profile)
            session.commit()

            return '''You are the best'''
        except:
            session.rollback()
            return '''Smth went wrong'''

    else:
        return '''Negative'''


@app.route('/login', methods=['GET', 'POST'])
def log():
    session = Session()
    if request.method == 'GET':
        us_id, us2_id = -1, -2
        login = request.args.get('login')
        password = request.args.get('password')
        user = session.query(users).where(users.login == login).first()
        if user is not None:
            us_id = user.user_id
            print(us_id)
        user2 = session.query(users).where(users.password == password).first()
        if user2 is not None:
            us2_id = user2.user_id
            print(us2_id)
        if us_id == us2_id:
            resp = make_response(str(us_id), 403)
            userID = us_id
            return resp
        else:
            session.rollback()
            return '''<h1>Invalid login or password<h1>'''

    else:
        return '''Negative'''

@app.route('/check', methods=['GET', 'POST'])
def check():
    userInfo = []
    session = Session()
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        user = session.query(user_profile).where(user_profile.user_id == user_id).first()
        userInfo.append(user.name)
        userInfo.append(user.second_name)
        userInfo.append(user.sex)
        userInfo.append(user.birth_date)
        userInfo.append(user.city)
        userInfo.append(user.status)
        userInfo.append(user.email)
        userInfo.append(user.phone_number)
        resp = make_response(str(userInfo), 403)
        return resp
        #user.name, user.second_name, user.sex, user.birth_date, user.city, user.status, user.email, user.phone_number
    else:
        return '''not ok'''

if __name__ == '__main__':
    app.run()
