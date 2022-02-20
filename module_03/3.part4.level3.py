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


def login_function(login, passwd):
    with open('users.json', 'r') as f:
        current_users = json.load(f)
    if login in current_users:
        if passwd == current_users[login]:
            return print(f"Вы вошли в систему под пользователем {login}")
        else:
            return print("Неверный логин или пароль!")
    else:
        return print("Неверный логин или пароль!")


new_user_login = input("Введите логин: ")
new_user_passwd = input("Введите пароль: ")

register(new_user_login, new_user_passwd)
login_function(new_user_login, new_user_passwd)