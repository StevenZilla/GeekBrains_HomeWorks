a = int(input("Введите число от 1 до 7, где 1 - это понедельник, 2 - это вторник и тд.: "))
if a < 6 and a > 0:
    print("Введенное число обозначает будний день!")
elif a > 5 and a < 8:
    print("Введенное число обозначает выходной день!")
else:
    print("Введенное число не соответсвует дню недели. Повторите попытку.")