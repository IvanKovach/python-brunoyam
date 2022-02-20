from random import randint

n = int(input("Введите размер массива: "))
numbers = [randint(0, 100) for i in range(n)]


def calc_maximum(list_numbers):
    list_numbers.sort(reverse=True)
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


numbers1 = [56, 9, 11, 2]
numbers2 = [3, 81, 5]
print(numbers)
print(f"Максимальное число: {calc_maximum(numbers)}")
print(f"Максимальное число: {calc_maximum(numbers1)}")
print(f"Максимальное число: {calc_maximum(numbers2)}")
