#Crie um programa que receba um número inteiro e exiba se ele é par ou ímpar.
try:
    numero=int(input("Digite um numero:"))
    if numero%2 == 0:
        print(f"O numero {numero} é PAR:")
    elif numero % 2 == 1:
        print(f"O número {numero} é IMPAR:")
except ValueError:
    print("Voçê não digitou um número válido.")

