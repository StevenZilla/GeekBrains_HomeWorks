s = int(input("Введите сумму двух чисел: "))
p = int(input("Введите произведение двух чисел: "))
res = ''
for i in range(1, s):
    if (s - i) == (p / i):
        res += f'(x = {i}, y = {s - i})'
if res == '':
    print("Исходные данные не верны!")
print(res)
