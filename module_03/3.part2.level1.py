input_list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
result_list = []

for i in input_list:
    if input_list.count(i) > 1 and i not in result_list:
        result_list.append(i)

print(f"В исходном списке следующие элементы повторялись: {' '.join(map(str, result_list))}")

# Или с помощью множества

result_list_2 = {j for j in input_list if input_list.count(j) > 1}
print(f"Метод 2: В исходном списке следующие элементы повторялись: {result_list_2}")
