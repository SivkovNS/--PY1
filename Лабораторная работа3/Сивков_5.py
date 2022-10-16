src = not False and True or False and not True

# TODO расписать упрощение выражения

result = True and True or False and True
result = True or False and True
result = True

print(src == result)
