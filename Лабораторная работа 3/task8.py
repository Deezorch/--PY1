money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
d = (spend * (increase + 1) - salary)  # разница между заработной платой и расходами в первый месяц
while money_capital >= d:
    d = (spend * (increase + 1) ** (month + 1) - salary)
    money_capital = money_capital - d
    month += 1

print(month)
