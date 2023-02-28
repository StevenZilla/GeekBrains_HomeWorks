Console.WriteLine("Введите первое число: ");
int number1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второе число: ");
int number2 = Convert.ToInt32(Console.ReadLine());

if (number1 > number2){
    Console.Write(number1 + " больше " + number2);
}
else if (number2 > number1){
    Console.Write(number1 + " меньше " + number2);
}
else {
    Console.Write("Введенные числа равны");
}