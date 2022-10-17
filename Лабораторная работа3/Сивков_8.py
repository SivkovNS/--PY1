salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
dif_begin = salary - spend
need_money = 0  # количество денег, чтобы прожить 10 месяцев
for i in range(months - 1):
    spend = spend * (1 + increase)
    dif_ = dif_begin + salary - spend
    dif_begin = dif_

# TODO Оформить решение
need_money = dif_ * (-1)
print(round(need_money))
