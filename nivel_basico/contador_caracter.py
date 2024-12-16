# Contador de caracteres
#Peça ao usuário que insira uma frase e mostre quantos caracteres ela possui.

def contador(palavra):
    palavra=input("Digite uma frase:")
    caracter=len(palavra) #usando o len para contar quantos caracter existe
    return f'A palavra {palavra} tem {caracter} caracter'

resposta=contador('palavra')
print (resposta)
