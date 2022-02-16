num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

max = (num1 > num2) * num1 + (num2 >= num1) * num2
print("Максимальное число: ", max)
