def prime_number():
    number = 1
    while True:
        k = 0
        for j in range(2, round(number ** 1 / 2)):
            if number % j == 0:
                k += 1
        if k == 0:
            yield number
        number += 1


g = prime_number()

for i in g:
    print(i)
