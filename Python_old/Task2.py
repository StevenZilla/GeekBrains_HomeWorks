x = int(input("Введите число Х: "))
y = int(input("Введите число Y: "))
z = int(input("Введите число Z: "))
a = not (x or y or z) 
b = (not x and not y and not z)
if a == b:
    print("Утверждение верно!")
else:
    print("Утверждение неверно!")
    