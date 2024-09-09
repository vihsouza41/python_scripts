#Faça uma função que informe a quantidade de
#dígitos de um determinado número inteiro informado pelo usuário.

numero=int(input("Digite um numero:"))


def verifica():
    numb=str(numero)
    number=len(numb)
    return number

print(verifica())