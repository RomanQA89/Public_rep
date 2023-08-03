tickets = int(input("Введите количество билетов, которое хотите приобрести: "))
sum_tickets = 0
for age_visitor in range(tickets):
    age_visitor = int(input("Введите возраст посетителя: "))
    if age_visitor < 18:
        sum_tickets += 0
    elif 18 <= age_visitor < 25:
        sum_tickets += 990
    elif age_visitor >= 25:
        sum_tickets += 1390
print("Сумма всех купленных билетов:", sum_tickets, "руб")
if tickets >= 4:
    print("Сумма всех купленных билетов со скидкой 10%:", (sum_tickets - sum_tickets * 10/100), "руб")
