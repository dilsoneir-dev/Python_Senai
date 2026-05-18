inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)