from random import randint

n = int(input("Введите количество монет: "))
heads = 0
res = ''
for i in range(n):
    top = randint(0, 1)
    res += f'{top} '
    if top == 0:
        heads += 1
if heads < n/2:
    res += f'--- {heads}'
else: 
    res += f'--- {n - heads}'
print(res)
