import datetime


def generate_tuple(year, month, day):
    while True:
        days = {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"}
        delta = 0
        date = datetime.date(year, month, day)
        weekday = date.weekday()
        while True:
            next_date = date + datetime.timedelta(delta)
            yield tuple([next_date.day, next_date.month, next_date.year, days.get(weekday)])
            if weekday == 6:
                weekday = 0
                continue
            weekday += 1
            delta += 1


g = generate_tuple(2000, 10, 20)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
