from random import randint

n = int(input("Введите размер массива: "))
numbers = [randint(0, 100) for i in range(n)]


def calc_maximum(list_numbers):
    #Сортируем список от больщего к меньшему
    list_numbers.sort(reverse=True)
    #В отсортированном списке перемещаем числа из 1 цифры вверх - ставим перед числами с тем же десятком
    #Например, цифру 2 ставим перед числами 20, 21, 22 .. и т.д.
    for i in list_numbers:
        if len(str(i)) == 1:
            for a in list_numbers:
                if i >= int(str(a)[0]) and i != a:
                    list_numbers.remove(i)
                    list_numbers.insert(list_numbers.index(a), i)
                    break
    result = "".join(str(b) for b in list_numbers)
    return result


numbers1 = [56, 9, 11, 2]
numbers2 = [3, 81, 5]
numbers3 = [2, 12, 21, 91, 9]
print(f"Из массива {numbers} можно составить максимальное число: {calc_maximum(numbers)}")
print(f"Из массива {numbers1} можно составить максимальное число: {calc_maximum(numbers1)}")
print(f"Из массива {numbers2} можно составить максимальное число: {calc_maximum(numbers2)}")
print(f"Из массива {numbers3} можно составить максимальное число: {calc_maximum(numbers3)}")
