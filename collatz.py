def collatz(number):
    if int(number) % 2 == 0:
        resultado = int(number) // 2
        return resultado
    else:
        resultado = 3 * int(number) + 1
        return resultado



i = 2
numero = input("Digite um numero inteiro: ")
while i != 1:
    i = collatz(numero)
    print(i)
    numero = i
