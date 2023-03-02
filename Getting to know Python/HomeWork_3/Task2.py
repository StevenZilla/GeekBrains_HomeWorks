n = int(input("Ввдеите число элементов: "))
num_list = list(map(int, input("Введите элементы: ").split()))
x = int(input("Введите искомое число: "))
print(num_list.count(x))