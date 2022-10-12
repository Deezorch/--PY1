salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

need_money = spend - salary  # колличество денег, нужное чтобы прожиит первый месяц
n = 0  # сколько раз выросли цены

for i in range(1, months):
    need_money += (spend * (increase + 1)**(n + 1) - salary)
    n += 1

print(round(need_money))
