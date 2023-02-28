n = int(input("Введите число: "))
res = ''
i = 0
while (2 ** i) <=n:
    res += f'{2 ** i} '
    i += 1 
print(res)