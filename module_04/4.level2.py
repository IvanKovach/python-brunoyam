a = [21, 7, 2, 4, 1, 9, 12, 63, 34]


def insert_sort(numbers):
    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1
        while j >= 0 and current < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = current
        print(numbers)


print(f"Исходный массив {a=}")
insert_sort(a)
print(f"Отсортированный массив {a=}")
