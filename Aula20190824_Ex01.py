print("Muda")
#Varíavel não é declarada (Python nao é fortemente tipada com 

n = 10
n = n+5

# O sinal de + serve para concatenar strings.
# a virgula serve para concatenar string com variável
print("O resultado é: ", n, "ok")

#float() - definiu o tipo para a entrada de dados.
# se fosse colocado int(), obrigatoriamente o usuário teria que digitar um número interiro.
# Casocontrário, será informado o erro.
aux = float(input("Digite um numero: "))

#input()- permite caputrar a entrada de dados do teclado

aux = aux + 5.5

print(aux)
'''
if aux>10:
    print("linha 1 do if")
    print("linha 2 do if")
print("linha 1 fora do if")
'''
'''
if aux>10:
    print("linha 1 do if")
    print("linha 2 do if")
    print("linha 3 do if")
else:
    print("linha 1 do else")
    print("linha 2 do else")
    print("linha 3 do else")
print("linha 1 hora do if")
'''


if aux>10:
    print("Entrei no primeiro if>10")
    if aux>20:
        print("Entrei no segundo if>20")
    else:
        print("entrei no else do segundo if>10 and <20")
# A regra principal do if é respeitar a indentação do código dos blocos if e else

if aux>10:
        print("Entrei no primeiro if > 10")
else:
    if aux<5:
       print("Entrei no else e no if < 5")

if (aux>10) and (aux%2==0):
    print("maior que 10 e múltiplo de 2")

if not aux>10:
    print("menor ou igual a 10")

if aux!=10:
    print("numero diferente de 10")

print("\nprimeiro FOR")
for i in range(0, 10, 2):
    print(i)
print("\nSegundo FOR")
for i in [2,4,6,9]:
    print(i)

print("\nterceito FOR")
for i in range(10, 0, -3):
    print(i)

print("\nPrimeiro WHILE")
i=20
while i>10:
    i-=1
    print(i)

print("Segundo WHILE")
i=20
while i>10 or i%2==0:
        print(i)
        i-=1


print("\n\nFim do Programa")
