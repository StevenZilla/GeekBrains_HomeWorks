es (21 sloc)  508 Bytes

Console.WriteLine("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());
void Cube(int[] number){
  int counter = 0;
  int length = number.Length;
  while (counter <  length){
    number[counter] = Convert.ToInt32(Math.Pow(counter, 3));
    counter++;
  }
}

void PrintArray(int[] coll){
  int count = coll.Length;
  int index = 0;
  while(index < count){
    Console.Write(coll[index]+ " ");
    index++;
  }
} 

int[] array = new int[number+1];
Cube(array);
PrintArray(array);
