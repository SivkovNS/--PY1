import random

A = -10
B = 10
END = 15

def get_unique_list_numbers():
    fisrt_list = [random.randint(A, B) for _ in range(END)]
    ffirst = list(set(fisrt_list))
    while len(ffirst) < END:
        rand_num = random.randint(A, B)
        trum = [ffirst.append(rand_num) for num in range(END) if rand_num not in ffirst]
    return ffirst

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
