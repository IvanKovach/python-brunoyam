password = input("Введите пароль: ")
while len(password) < 9 or password.islower() or password.isupper():
    print("Пароль должен состоять более, чем из 8 символов и содержать как прописные, так и заглавные буквы ...")
    password = input("Введите пароль: ")
