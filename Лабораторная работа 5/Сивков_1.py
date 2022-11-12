# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
A = 0
B = 16

list_of_numbers = [{'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)} for i in range(A, B)]

pprint(list_of_numbers)
