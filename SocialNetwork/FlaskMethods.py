import numpy as np
import requests
import pandas as pd
import simplejson as simplejson


def register(login, password):
    response = requests.get('http://127.0.0.1:5000/register', params={'login': login, 'password': password})
    if response:
        return True
    else:
        return False

def auth(login, password):
    response = requests.get('http://127.0.0.1:5000/login', params={'login': login, 'password': password})
    user_id = response.text
    if response.status_code == 403:
        return user_id
        #return True
    else:
        return False

def checkInfo(user_id):
    response = requests.get('http://127.0.0.1:5000/check', params={'user_id': user_id})
    if response.status_code == 403:
        userInfo = response.text
        #print(userInfo)
        userInfo2 = userInfo.replace('\'', '')
        #print(userInfo2)
        userInfoMas = userInfo2.split(',')
        buf1 = userInfoMas[3]
        buf1 = buf1[-4:]
        #print(buf1)
        buf2 = userInfoMas[4]
        buf2 += '.'
        #print(buf2)
        buf3 = userInfoMas[5]
        buf3 = buf3[:-1]
        buf3 += '.'
        #print(buf3)
        buf4 = buf3+buf2+buf1
        buf4 = buf4.replace(' ', '')
        #print(buf4)
        for i in range(3):
            del userInfoMas[3]
        userInfoMas.insert(3, buf4)
        #print(userInfoMas)
        userInfoMas[0] = userInfoMas[0][1:]
        userInfoMas[1] = userInfoMas[1][1:]
        userInfoMas[2] = userInfoMas[2][1:]
        userInfoMas[4] = userInfoMas[4][1:]
        userInfoMas[5] = userInfoMas[5][1:]
        userInfoMas[6] = userInfoMas[6][1:]
        userInfoMas[7] = userInfoMas[7][1:]
        userInfoMas[7] = userInfoMas[7][:-1]
        #print(userInfoMas[0])
        #print(userInfoMas[1])
        #print(userInfoMas[2])
        #print(userInfoMas[3])
        #print(userInfoMas[4])
        #print(userInfoMas[5])
        #print(userInfoMas[6])
        #print(userInfoMas[7])
        #print(userInfoMas)
        return userInfoMas
    else:
        return False

