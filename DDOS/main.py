import grequests

logins = [f"Username{login}" for login in range(300)]
passwords = [f"Password{password}" for password in range(300)]

sites = ["http://127.0.0.1:5000/register" for i in range(300)]
while True:
    for i in range(300):
        r = (grequests.get(url, params={'login': logins[i], 'password': passwords[i]}) for url in sites)
        print(grequests.map(r))

