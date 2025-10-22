import datetime


def generate_dates(year, month, day):
    date = datetime.date(year, month, day)
    days = 0
    while True:
        yield date + datetime.timedelta(days)
        days += 1


g = generate_dates(2000, 10, 20)

for i in g:
    print(i)
