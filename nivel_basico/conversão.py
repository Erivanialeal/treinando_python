#Crie um programa que converta uma temperatura de graus Celsius 
# para Fahrenheit. A fórmula de conversão é:

def conversao(temperatura):
    temperatura=float(input("temperatura em Celsius:"))
    converter= (temperatura * 9) / 5 + 32
    return converter

resposta=conversao('temperatura')
print(resposta)

