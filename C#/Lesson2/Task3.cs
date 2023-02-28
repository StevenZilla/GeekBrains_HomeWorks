Console.WriteLine("Введите число от 1 до 7, где 1 - это понедельник, 2 - вторник ... 7 - воскресенье: ");
int input = Convert.ToInt32(Console.ReadLine());
if (input > 5 & input < 8){
    Console.WriteLine("Это выходной день");
}
else if (input > 7 || input < 1){
    Console.WriteLine("Не соответствует значению");
}
else {
    Console.WriteLine("Это будний день");
}