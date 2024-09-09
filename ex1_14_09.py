
# Faça um programa que solicite ao usuário três numeros diferentes e exiba o dobro do maior numero. 
# Para Fazer isso separe seu codigo em duas funções diferentes: 
# Uma função para retornar o maior dos tres numeros e outra função para dobrar o numero

num1 = int(input ("digite um numero: "))
num2 = int(input ("digite um numero: "))
num3 = int(input ("digite um numero: "))

def compare():
    if num1 >= num2 and num1 >= num3:
        numb=num1
    elif num2 >= num1 and num2 >= num3:
        numb=num2
    elif num3 >= num1 and num3 >= num2:
        numb=num3
    return numb

number=(compare())

def dobrar():
    result=number*2
    return result

resultado=(dobrar())

print ("Numero maior eh:",number)
print ("Dobro dele eh:",resultado)






