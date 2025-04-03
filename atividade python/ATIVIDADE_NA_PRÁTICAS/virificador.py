# Boa tarde professor, esta é a atividade deste trabalho.
# O usuário deve inserir um número (positivo ou negativo).

num = int(input("Digite um número para ser classificado: "))

# Processamento: verifica se o número é positivo, negativo ou zero.
if num > 0:
    print("O número está classificado como positivo.")
elif num < 0:
    print("O número está classificado como negativo.")
else:
    print("O número é zero.")
