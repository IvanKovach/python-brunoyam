from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
maximum = 0
for i in m:
    for j in i:
        if j > maximum:
            maximum = j

print(f"В списке {m=} максимальный элемент {maximum=}")