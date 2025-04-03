# Solicita um número entre 1 e 10
while True:
    try:
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
        if 1 <= numero <= 10:
            break
        else:
            print("Número fora do intervalo válido!")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Calcula o fatorial
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
    print(f"{i}! = {fatorial}")  # Mostra o fatorial parcial

# Exibe o resultado final
print(f"\nO fatorial de {numero} é: {fatorial}")

# Verifica se é maior que 100
if fatorial > 100:
    print("O resultado é maior que 100!")
else:
    print("O resultado é 100 ou menos.")