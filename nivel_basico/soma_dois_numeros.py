#Aqui estão 10 exercícios básicos de lógica de programação em Python para você praticar:

def soma_de_dois_numeros(valor1,valor2):
    valor1=int(input("Digite um número inteiro:"))
    valor2=int(input("Digite um o segundo número inteiro:"))
    resultado= valor1 + valor2
    return f"A soma de {valor1} + {valor2} é: {resultado}"

resposta=soma_de_dois_numeros('valor1','valor2')
print(resposta)