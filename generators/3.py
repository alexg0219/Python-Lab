import datetime


def generate_dates(year, month, day):
    days = {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"}
    weekday = datetime.date(year, month, day).weekday()
    while True:
        yield days.get(weekday)
        if weekday == 6:
            weekday = 0
            continue
        weekday += 1


g = generate_dates(2000, 10, 20)

# for i in g:
#    print(i)
