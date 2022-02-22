import json


def register(login, passwd):
    with open('users.json', 'r') as f:
        current_users = json.load(f)
    if login in current_users:
        return print("Login already in use")
    else:
        current_users[login] = passwd
        with open('users.json', 'w') as f:
            json.dump(current_users, f)


new_user_login = input("Введите логин: ")
new_user_passwd = input("Введите пароль: ")

register(new_user_login, new_user_passwd)
