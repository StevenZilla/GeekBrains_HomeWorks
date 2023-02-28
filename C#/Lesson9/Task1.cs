int M = AskNumber("M");
int N = AskNumber("N");
Console.WriteLine($"M = {M}; N = {N}. -> \"{PrintRange(M, N)}\"");

static string PrintRange(int M, int N) {
    if(N < M) {
        return "";
    }
    string part = N == M ? $"{N}" : $"{N}, ";
    return part + PrintRange(M, N - 1);
}

static int AskNumber(string name) {
    Console.Write($"Введите число {name}: ");
    return int.Parse(Console.ReadLine());
}
