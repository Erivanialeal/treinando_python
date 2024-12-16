#Desenvolva uma calculadora que permita ao usuário escolher entre adição, subtração, 
# multiplicação e divisão.
def menu():
    calculadora='''
        1.ADIÇÃO (+)
        2.SUBTRACÃO (-)
        3.MULTIPLICAÇÃO (x)
        4.DIVISÃO (/)
        5.SAIR
'''
    return calculadora
while True :
    print(menu())
    esconha=(input("Escolha Uma Opção:"))
    
    if esconha == '1':
        
        tabuada=int(input("Tabuada:"))
        numero=int(input("Numero:"))
        soma = tabuada + numero
        print(f"{tabuada} + {numero} = {soma}")

    elif esconha == '2':
        tabuada= int(input("Tabuada:"))
        numero= int(input("Numero:"))
        soma=tabuada - numero
        print(f"{tabuada} - {numero} = {soma}")
    
    elif esconha == '3':
        tabuada=int(input("Tabuada:"))
        numero=int(input("Numero:"))
        soma= tabuada * numero
        print(f"{tabuada} X {numero} = {soma}")

    elif esconha == '4':
        tabuada=int(input("Tabuada:"))
        numero=int(input("Numero:"))
        soma= tabuada / numero
        print(f"{tabuada} / {numero} = {soma}")

    else:
        print("Saindo...")


    