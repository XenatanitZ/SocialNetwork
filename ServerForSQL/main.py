from flask import Flask, request, make_response, abort
from sqlalchemy import create_engine, update
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, scoped_session
import time
import pg8000
import pyodbc

Base = automap_base()

engine = create_engine('mssql+pyodbc://sa:fh[fyutkmcr1978@arch.designer/SocialNetwork?driver=ODBC+Driver+17+for+SQL+Server')
#engine = create_engine('postgresql+pg8000://postgres@arch.designer/SocialNetwork')
conn = engine.connect()

Session = sessionmaker(bind=engine)
session = scoped_session(Session)

Base.prepare(engine, reflect=True)


users = Base.classes.Users
user_profile = Base.classes.User_profile
posts = Base.classes.Posts
messages = Base.classes.Messages

app = Flask(__name__)

listOfMessages = []


@app.route('/test')
def test():
    session = Session()
    try:
        question_time = time.time()
        user = session.query(users).where(users.login == request.args['login']).first()
        session.close()
        ret = {'question_time': question_time, 'answer_time': time.time()}
        return {'ok': ret}, 200
    except:
        return "Error bd", 400


@app.route('/register', methods=['GET', 'POST'])
def reg():
    session = Session()
    if request.method == 'GET':
        try:
            user = users(login=request.args.get('login'), password=request.args.get('password'))
            session.add(user)
            session.flush()
            session.commit()
            session.close()
            return 'OK', 200
        except:
            session.rollback()
            return 'Not ok', 400

    else:
        return '...', 400


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
            session.close()
            return '''Good''', 200
        else:
            session.rollback()
            return '''<h1>Invalid login or password<h1>''', 400

    else:
        return '''Negative'''


@app.route('/check', methods=['GET', 'POST'])
def check():
    session = Session()
    if request.method == 'GET':
        login = request.args.get('login')
        user = session.query(users).where(users.login == login).first()
        user2 = session.query(user_profile).where(user_profile.user_id == user.user_id).first()
        UserInfo = {'Info': user2.name, 'Info1': user2.second_name, 'Info2': user2.sex, 'Info3': user2.birth_date, 'Info4': user2.city, 'Info5': user2.status, 'Info6': user2.email, 'Info7': user2.phone_number}
        session.close()
        return {'user': UserInfo}, 200
    else:
        session.rollback()
        return '''not ok''', 400


@app.route('/editing', methods=['GET', 'POST', 'DELETE'])
def edit():
    session = Session()
    if request.method == 'GET':
        login = request.args.get('login')
        name = request.args.get('name')
        surname = request.args.get('surname')
        sex = request.args.get('sex')
        city = request.args.get('city')
        email = request.args.get('email')
        number = request.args.get('number')
        date = request.args.get('date')
        user = session.query(users).where(users.login == login).first()
        try:
            updateInfo = update(user_profile).values(name=name, second_name=surname, sex=sex, city=city, email=email, phone_number=number, birth_date=date).where(user_profile.user_id == user.user_id)
            conn.execute(updateInfo)
            session.commit()
            session.close()
            return '''<h1>GOOD<h1>''', 200
        except:
            session.rollback()
            return '''<h1>Bad<h1>''', 400


@app.route('/editStat', methods=['GET', 'POST', 'DELETE'])
def editStat():
    if request.method == 'GET':
        login = request.args.get('login')
        status = request.args.get('status')
        user = session.query(users).where(users.login == login).first()
        try:
            session.flush()
            updateInfo = update(user_profile).values(status=status).where(user_profile.user_id == user.user_id)
            session.flush()
            conn.execute(updateInfo)
            session.commit()
            session.close()
            return '''<h1>GOOD<h1>''', 200
        except:
            session.rollback()
            return '''BAD''', 400


@app.route('/postAdding', methods=['GET', 'POST'])
def addPost():
    if request.method == 'GET':
        login = request.args.get('login')
        post = request.args.get('post')
        date = request.args.get('formatted_date')
        user = session.query(users).where(users.login == login).first()
        try:
            adding = posts(user_id=user.user_id, post_text=post, post_date=date)
            session.add(adding)
            session.flush()
            session.commit()
            session.close()
            return '''<h1>GOOD<h1>''', 200
        except:
            session.rollback()
            return '''BAD''', 400


@app.route('/postChecking', methods=['GET', 'POST'])
def checkPost():
    if request.method == 'GET':
        login = request.args.get('login')
        try:
            user = session.query(users).where(users.login == login).first()
            postUser = session.query(posts).where(posts.user_id == user.user_id).first()
            if postUser is None:
                postUser1 = posts(post_text="None", post_date="None", user_id=user.user_id)
                session.add(postUser1)
                session.flush()
                session.commit()
                postUser = session.query(posts).where(posts.user_id == user.user_id).first()
            postUserInfo = {'Info': str(postUser.post_date), 'Info1': postUser.post_text}
            session.commit()
            session.close()
            return {'user': postUserInfo}, 200
        except:
            session.rollback()
            return '''BAD''', 400


@app.route('/postChanging', methods=['GET', 'POST'])
def changePost():
    if request.method == 'GET':
        login = request.args.get('login')
        newPost = request.args.get('newPost')
        date = request.args.get('formatted_date')
        user = session.query(users).where(users.login == login).first()
        try:
            updateInfo = update(posts).values(post_text=newPost, post_date=date).where(user_profile.user_id == user.user_id)
            session.flush()
            conn.execute(updateInfo)
            session.commit()
            session.close()
            return '''<h1>GOOD<h1>''', 200
        except:
            session.rollback()
            return '''BAD''', 400


@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    login = request.json['login']
    message = request.json['message']
    now = time.time()
    listOfMessages.append({'login': login, 'message': message, 'date': now})
    session = Session()
    try:
        adding = messages(date=str(now), message_text=message, sender_name=login)
        session.add(adding)
        session.commit()
        session.close()
        return '''<h1>GOOD<h1>''', 200
    except:
        session.rollback()
        session.close()
        return '''<h1>FAIL<h1>''', 400

def message_filter(elements, key, min_value):
    new_elements = []

    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)
    return new_elements

@app.route('/getMessage')
def getMessage():
    global after
    print(request.args['after'])
    try:
        after = float(request.args['after'])

    except:
        abort(400)
    filteredmessages = message_filter(listOfMessages, key='date', min_value=after)
    return {'messages': filteredmessages}

if __name__ == '__main__':
    app.run()
