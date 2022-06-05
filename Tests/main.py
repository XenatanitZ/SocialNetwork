from datetime import datetime

import requests
import time
print("---MongoDB---")
mas_time = []
n = 0
while n <= 1000:
    r = requests.get('http://127.0.0.1:5000/test', params={'login': 'Username'+str(n)})
    jsonInfo = r.json()['ok']
    dif = datetime.fromtimestamp(jsonInfo['answer_time'] - jsonInfo['question_time'])
    mas_time.append(float(dif.strftime("%S.%f")))
    n += 1
for i in mas_time:
    print(i)
    if i == 0.0:
        mas_time.remove(i)
print("---PostgreSQL---")
print("Минимальное время: ", min(mas_time))
print("Среднее время: ", sum(mas_time)/len(mas_time))
print("Максимальное время: ", max(mas_time))
print("Максимальная пропускная способность в секунду: ", int(1//min(mas_time)))


