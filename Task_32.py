# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(list_1, min_number, max_number):
    indexes = []
    for index, value in enumerate(list_1):
        if min_number <= value <= max_number:
            indexes.append(index)
    return indexes

list_1 = [1, 5, 3, 8, 2, 7, 4, 6]
min_number = int(input())
max_number = int(input())
result = find_indexes(list_1, min_number, max_number)
print(result)  

