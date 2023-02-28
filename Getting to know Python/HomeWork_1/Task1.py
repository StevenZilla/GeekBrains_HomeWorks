#Найдите сумму цифр трехзначного числа. 
 
num = int(input("Введите трехзначное число: ")) 
check_num = num // 100 
if check_num >= 1 and check_num < 10: 
    term1 = num % 10 
    num = num // 10 
    term2 = num % 10 
    num = num // 10 
    res = (term1 + term2 + num) 
    print(res) 
else: 
    print("Вы ввели не трехзначное число!")