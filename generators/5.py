def head(count, filename):
    with open(filename) as f:
        for i in range(count):
            yield f.readline().strip('\n')


reader = head(10, '1.txt')

for i in reader:
    print(i)