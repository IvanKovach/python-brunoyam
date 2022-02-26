a = [1, 2, 4, 7, 9, 12, 21, 34, 63]


def binary_search(numbers, x):
    middle = int(len(numbers) / 2)
    left = numbers[:middle]
    right = numbers[middle:]
    print(f"{len(numbers)=} {middle=}  {numbers[middle]=} {left=}  {right=}")
    if x == numbers[middle]:
        return print(f"В массиве найден {x=}")
    elif x > numbers[middle] and len(numbers) > 1:
        binary_search(right[:], x)
    elif x < numbers[middle] and len(numbers) > 1:
        binary_search(left[:], x)
    else:
        return print(f"Число в массиве не найдено")


print(a)
num = int(input("Введите число для поиска: "))
binary_search(a, num)
