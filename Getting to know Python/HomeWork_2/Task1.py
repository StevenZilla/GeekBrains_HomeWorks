n = int(input())
heads = 0
tails = 0
for i in range(n):
    x = int(input())
    if x == 0:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
else:
    print(heads)
