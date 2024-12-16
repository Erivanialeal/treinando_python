# Par ou Ímpar
#Peça ao usuário para digitar um número inteiro e informe se ele é par ou ímpar.

def par_ou_impar(numero):
    numero=int(input("Digite um número inteiro:"))
    resposta= numero % 2

    if resposta == 0:
        print(f"O número {numero} é par")  
    else:
        print(f"O numero {numero} é impar")

par_ou_impar('numero')


