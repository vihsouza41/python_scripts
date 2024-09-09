import random
import itertools
import time

### Mostra o menu inicial
def ShowMenu():
    print ("\n* JOGO DA FORCA * \n\n")
    print (" MENU: \n")
    print (" 1) Configuração do jogo \n 2) Jogar \n 3) Sair \n")
    OPT=int(input("Digite a opção que deseja escolher:"))
    return OPT

### Menu de configuração do jogo
def ConfigMenu():
    print ("\n* JOGO DA FORCA * \n\n")
    print (" CONFIGURAÇÃO DO JOGO: \n")
    print (" Escolha uma opção: \n A) Adicionar nova palavra ao jogo. \n B) Concluir configuração.  \n")
    OPT=str(input("Opção escolhida: "))
    return OPT

### Função para adicionar palavras ao banco de dados
def AdicionaPalavra(Palavra):
    arquivo = open ('BancoDePalavras.txt', 'r+')
    quantidade=sum(1 for line in arquivo)
    arquivo.seek(0)
    arquivo.write(str(quantidade) + '\n')
    arquivo = open ('BancoDePalavras.txt', 'a+')
    arquivo.write(Palavra + '\n')
    arquivo.close()

### Checa se o arquivo está preenchido
def ChecaArquivo():
    arquivo = open ('BancoDePalavras.txt', 'r+')
    quantidade=sum(1 for line in arquivo)
    arquivo.close()
    return quantidade

### Solicita uma letra ao usuário
def SolicitaLetra(lista_certa,lista_errada,segredo):
    result=str(input("Digite uma letra: "))
    if (result==segredo.rstrip('\n')):
        print ("\n\n Você venceu! a palavra é:\n",segredo, "\n\n\n\nVoltando ao menu principal...\n")
        main()
    while result in lista_certa or result in lista_errada:
        result=str(input("Letra já digitada. Favor digitar outra:"))
    if result in segredo:
        lista_certa.append(result)
    else:
        lista_errada.append(result)

### Código do jogo em si
def Jogo():
    loop=0
    palavra=PalavraAleatoria()
    tamanho=(len(palavra)-1)
    LetrasErradas=[]
    LetrasCertas=[]
    ListaSegredo=[]
    print ("\n A palavra secreta tem este tamanho: \n")
    print("_ "*tamanho+"\n")

    while (loop==0):
        HangMan(len(LetrasErradas))
        SolicitaLetra(LetrasCertas,LetrasErradas,palavra)
        for position in range(len(palavra)-1):
            if palavra[position] in LetrasCertas:
                ListaSegredo.append(palavra[position])
            else:
                ListaSegredo.append("_")
        print ("\n")
        print ("A palavra secreta tem este tamanho: \n")
        print (' '.join(map(str, ListaSegredo)))
        print ("\n\n"+"Letras erradas: \n",(' - '.join(map(str, LetrasErradas))))
        
        if (len(LetrasErradas) > 5):
            print ("\n\n ENFORCADO !")
            HangMan(6)
            print ("\n Você perdeu o jogo!\n\n\n\n Voltando ao menu principal...\n")
            time.sleep(2)
            main()
        
        if "_" not in ListaSegredo:
            print ("\n\n Você venceu! a palavra é:\n",palavra, "\n\n\n\nVoltando ao menu principal...\n")
            main()

        ListaSegredo=[]

### Função da forca
def HangMan(erros):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    if erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O  ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    if erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O  ")
        print("|    |  ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    if erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O  ")
        print("|    |\\  ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    if erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O  ")
        print("|   /|\\ ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()    
    if erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O  ")
        print("|   /|\\ ")
        print("|     \\ ")
        print("|      ")
        print("_      ")
        print()
    if erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O  ")
        print("|   /|\\ ")
        print("|   / \\ ")
        print("|      ")
        print("_      ")
        print()

### Seleciona aleatoriamente uma palavra do banco
def PalavraAleatoria():
    arquivo = open ('BancoDePalavras.txt', 'r')
    quantidade=sum(1 for line in arquivo)
    arquivo.close
    arquivo = open ('BancoDePalavras.txt', 'r')
    lista=[]
    for line in itertools.islice(arquivo, 1, quantidade ):
        lista.append(line)
    aleatorio = random.choice(lista)
    return aleatorio
    
def main():
    Option=ShowMenu()
    Sair=0
    while Sair==0:
        if (Option == 1):
            Option2=ConfigMenu()
            if (Option2 == 'A'):
                PALAVRA=str(input("Digite a Palavra: "))
                AdicionaPalavra(PALAVRA)
            elif (Option2 == 'B'):
                print ("Retornando ao menu anterior.")
                main ()
            else:
                print ("Opção não reconhecida.")
                
        elif (Option == 2):
            if (ChecaArquivo() <= 1):
                print ("Favor configurar palavras antes de jogar, selecione opção 1. ")
                main()
            Jogo()

        elif (Option == 3):
            print ("Saindo do jogo...")
            exit()

        else:
            print ("\n Opção errada. Favor digitar corretamente.")
            main()

main ()