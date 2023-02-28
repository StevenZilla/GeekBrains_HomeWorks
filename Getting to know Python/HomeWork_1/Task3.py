num = (input("Введите шестизначное число: ")) 
num2 = int(num) 
check_num = int(num2 // 100000) 
if check_num >= 1 and check_num < 10: 
    half1 = int(num[0]) + int(num[1]) + int(num[2]) 
    half2 = int(num[3]) + int(num[4]) + int(num[5]) 
    if half1 == half2: 
        print('Вам выпал счасливый билет!') 
    else: 
        print('Ваш билет не является счастливым') 
else: 
    print("Вы ввели не шестизначное число!")
