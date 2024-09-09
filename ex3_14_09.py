# Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721.

number=int(input("Digite um numero:"))

def reverso():
    string=str(number)
    rever=string[::-1]
    return rever

print (reverso())