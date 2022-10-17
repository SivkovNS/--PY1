list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
len_ = len(list_numbers)
count = len_ - 1
last_early = list_numbers[-1]
# TODO Оформить решение
for i in range(count):
    if list_numbers[i] > list_numbers[count]:
        list_numbers[count] = list_numbers[i]
count_two = count - 1
for i in range(count_two):
    if list_numbers[i] == list_numbers[-1]:
        list_numbers[i] = last_early
print(list_numbers)
