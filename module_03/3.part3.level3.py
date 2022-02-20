from random import randint

n = int(input("Введите размер массива: "))
numbers = [randint(0, 100) for i in range(n)]

def calc_maximum(list_numbers):
    list_numbers.sort()
    result = ""
    for i in list_numbers:
        if result == "":
            result = str(i)
            continue
        if int(str(i)[0]) >= int(result[0]):
            result = str(i) + result
        else:
            result = result + str(i)
    return result

numbers = [16, 2, 21, 25, 99]
print(numbers)
print(f"Максимальное число: {calc_maximum(numbers)}")