a = []
b = []

for i in range(6):

    n = int(input())

    if n % 2 == 0:
        a.append(n)
    else:
        b.append(n)

f = ' '.join(str(num) for num in a)
d = ' '.join(str(num) for num in b)

print('Список чётных чисел = ', f)
print('Список нечётных чисел = ', d)
