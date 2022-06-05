import pymongo
from flask import Flask, request, make_response, abort
import time


dbclient = pymongo.MongoClient("mongodb://arch.designer:27017")
currentdb = dbclient["SocialNetwork"]
users = currentdb["Users"]
posts = currentdb["Posts"]
messages = currentdb["Messages"]
user_profile = currentdb["User_profile"]
user_friends = currentdb["User_Friends"]

app = Flask(__name__)

listOfMessages = []

@app.route('/test')
def test():
    try:
        question_time = time.time()
        users.find_one({'login': request.args['login']})
        ret = {'question_time': question_time, 'answer_time': time.time()}
        return {'ok': ret}, 200
    except:
        return "Error bd", 400


@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        try:
            user_id = users.insert_one({'login': request.args.get('login'), 'password': request.args.get('password')})
            user_profile.insert_one({'user_id': user_id.inserted_id, 'name': "None", 'second_name': "None", 'sex': "None", 'birth_date': "None", 'status': "None", 'email': "None", 'phone_number': "None", 'city': "None"})
            return 'OK', 200
        except:
            return 'Not ok', 400
    else:
        return '...', 400


@app.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'GET':
        user = users.find_one({'login': request.args['login'], 'password': request.args['password']})
        print(user)
        if user is None:
            return '''Bad''', 400
        else:
            us_id = user['_id']
            return str(us_id), 200


@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        login = request.args.get('login')
        user_id = users.find_one({'login': login})
        user = user_profile.find_one({'user_id': user_id['_id']})
        UserInfo = {'Info': user['name'], 'Info1': user['second_name'], 'Info2': user['sex'], 'Info3': user['birth_date'], 'Info4': user['city'], 'Info5': user['status'], 'Info6': user['email'], 'Info7': user['phone_number']}
        if user is None:
            return '''not ok''', 400
        else:
            return {'user': UserInfo}, 200
    else:
        return '''not ok''', 400


@app.route('/editing', methods=['GET', 'POST', 'DELETE'])
def edit():
    if request.method == 'GET':
        login = request.args.get('login')
        name = request.args.get('name')
        surname = request.args.get('surname')
        sex = request.args.get('sex')
        city = request.args.get('city')
        email = request.args.get('email')
        number = request.args.get('number')
        date = request.args.get('date')
        try:
            user_id = users.find_one({'login': login})
            user_profile.update_one({'user_id': user_id['_id']}, {'$set': {'name': name, 'second_name': surname, 'sex': sex, 'city': city, 'email': email, 'phone_number': number, 'birth_date': date}})
            return '''<h1>GOOD<h1>''', 200
        except:
            return '''<h1>Bad<h1>''', 400


@app.route('/editStat', methods=['GET', 'POST', 'DELETE'])
def editStat():
    if request.method == 'GET':

        login = request.args.get('login')
        status = request.args.get('status')
        try:
            user_id = users.find_one({'login': login})
            user_profile.update_one({'user_id': user_id['_id']}, {'$set': {'status': status}})
            return '''<h1>GOOD<h1>''', 200
        except:
            return '''<h1>Bad<h1>''', 400


@app.route('/postAdding', methods=['GET', 'POST'])
def addPost():
    if request.method == 'GET':
        user_id = users.find_one({request.args.get('login')})
        try:
            posts.insert_one({'post_text': request.args.get('post'), 'post_date': request.args.get('formatted_date'), 'user_id': user_id['_id']})
            return '''<h1>GOOD<h1>''', 200
        except:
            return '''<h1>BAD<h1>''', 400


@app.route('/postChecking', methods=['GET', 'POST'])
def checkPost():
    if request.method == 'GET':
        try:
            user = users.find_one({'login': request.args['login']})
            user1 = posts.find_one({'user_id': user['_id']})
            if user1 is None:
                posts.insert_one({'post_text': "None", 'post_date': "None", 'user_id': user['_id']})
                user1 = posts.find_one({'user_id': user['_id']})
            postUserInfo = {'Info': user1[str('post_date')], 'Info1': user1['post_text']}
            return {'user': postUserInfo}, 200
        except:
            return '''BAD''', 400


@app.route('/postChanging', methods=['GET', 'POST'])
def changePost():
    if request.method == 'GET':
        newPost = request.args.get('newPost')
        date = request.args.get('formatted_date')
        try:
            user = users.find_one({'login': request.args['login']})
            user1 = posts.find_one({'user_id': user['_id']})
            posts.update_one({'user_id': user1['user_id']}, {'$set': {'post_text': newPost, 'post_date': date}})
            return '''<h1>GOOD<h1>''', 200
        except:
            return '''<h1>BAD<h1>''', 400


@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    login = request.json['login']
    message = request.json['message']
    now = time.time()
    listOfMessages.append({'login': login, 'message': message, 'date': now})
    try:
        messages.insert_one({'date': str('now'), 'message_text': message, 'sender_name': login})
        return '''<h1>GOOD<h1>''', 200
    except:
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
