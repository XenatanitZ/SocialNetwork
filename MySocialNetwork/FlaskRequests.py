import requests


def register(login, password):
    response = requests.get('http://127.0.0.1:5000/register', params={'login': login, 'password': password})
    if response.status_code == 200:
        return True
    else:
        return False


def auth(login, password):
    response = requests.get('http://127.0.0.1:5000/login', params={'login': login, 'password': password})
    if response.status_code == 200:
        return True
    else:
        return False


def editing(surname, name, sex, city, number, email, date, login):
    response = requests.get('http://127.0.0.1:5000/editing', params={'surname': surname, 'name': name, 'sex': sex, 'city': city, 'number': number, 'email': email, 'date': date, 'login': login})
    if response.status_code == 200:
        return True
    else:
        return False


def editStatus(login, status):
    response = requests.get('http://127.0.0.1:5000/editStat', params={'login': login, 'status': status})
    if response.status_code == 200:
        return True
    else:
        return False


def checkInfo(login):
    response = requests.get('http://127.0.0.1:5000/check', params={'login': login})
    answer = response.json()['user']
    if response.status_code == 200:
        userInfoMas = []
        userInfoMas.append(answer['Info'])
        userInfoMas.append(answer['Info1'])
        userInfoMas.append(answer['Info2'])
        userInfoMas.append(answer['Info3'])
        userInfoMas.append(answer['Info4'])
        userInfoMas.append(answer['Info5'])
        userInfoMas.append(answer['Info6'])
        userInfoMas.append(answer['Info7'])
        return userInfoMas
    else:
        return False


def postAdding(login, post, formatted_date):
    response = requests.get('http://127.0.0.1:5000/postAdding', params={'login': login, 'post': post, 'formatted_date': formatted_date})
    if response.status_code == 200:
        return True
    else:
        return False


def checkPosts(login):
    response = requests.get('http://127.0.0.1:5000/postChecking', params={'login': login})
    answer = response.json()['user']
    if response.status_code == 200:
        postUserInfoMas = []
        postUserInfoMas.append(answer['Info'])
        postUserInfoMas.append(answer['Info1'])
        print(postUserInfoMas)
        return postUserInfoMas
    else:
        return False


def changingPosts(login, newPost, formatted_date):
    response = requests.get('http://127.0.0.1:5000/postChanging', params={'login': login, 'newPost': newPost, 'formatted_date': formatted_date})
    if response.status_code == 200:
        return True
    else:
        return False

def sendingMessage(data):
    response = requests.post('http://127.0.0.1:5000/sendMessage', json=data)
    if response.status_code == 200:
        return True
    else:
        return False

def gettingMessage(date):
    response = requests.get('http://127.0.0.1:5000/getMessage', params={'after': date})
    if response.status_code == 200:
        return response
    else:
        return False

