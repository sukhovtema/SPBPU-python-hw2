money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_without_debt = 0

while money_capital >= 0:
    monthly_budget = money_capital + salary - spend
    money_capital = monthly_budget
    spend *= (1 + increase)

    if money_capital >= 0:
        months_without_debt += 1

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)
