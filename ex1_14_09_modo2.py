
# Faça um programa que solicite ao usuário três numeros diferentes e exiba o dobro do maior numero. 
# Para Fazer isso separe seu codigo em duas funções diferentes: 
# Uma função para retornar o maior dos tres numeros e outra função para dobrar o numero

def compare(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        numb=num1
    elif num2 >= num1 and num2 >= num3:
        numb=num2
    elif num3 >= num1 and num3 >= num2:
        numb=num3
    return numb

def dobrar(num):
    result=num*2
    return result

a = int(input ("digite um numero: "))
b = int(input ("digite um numero: "))
c = int(input ("digite um numero: "))

maior=(compare(a,b,c))
print (maior)
dobro=(dobrar(maior))
print (dobro)





