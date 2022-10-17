money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
money_capital = money_capital - spend
spend = spend * (1 + increase)
month = 1
differ = spend - salary
while money_capital > differ:
    money_capital = money_capital + salary - spend
    spend = spend * (1+increase)
    differ = spend - salary
    month = month + 1

# TODO Оформить решение

print(month)
