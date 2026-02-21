import random

def carinha(n):
    print("----------------------")
    if n > 0:
        print("-         0          -")
    else:
        print("-                    -")
    
    print("-        /|\\         -")
    print("-        / \\         -")
    print("----------------------")


# DEFINE A LISTA DE PALAVRAS
palavras = ['porta', 'chapeu', 'cadeira', 'controle', 'aspirador', 'ventilador']
# DEFINE O NUMERO DE TENTATIVAS ATUAL
tentativas = 0
letras_tentadas = []
tamanho = 0

erros = []
# DEFINE O NUMERO MAXIMO DE ERROS
max_erros = 6

while tamanho < 5 or tamanho > 10:
    tamanho = int(input("Oiii, digite o numero de caracteres para a palavra do jogo: "))

    if tamanho < 5:
        print(" o numero deve ser maior que 4")

    if tamanho > 10:
        print(" o numero deve ser menor que 11")

comprimento_lista = len(palavras)

posicao = 0

while posicao < comprimento_lista:
    if tamanho == len(palavras[posicao]):
        palavra = palavras[posicao]
    posicao = posicao + 1


acertos = []
posicao = 0 
while posicao < tamanho:
    acertos.append("_")
    posicao = posicao +1

print ("---------------------------------------------------------")
print ("                JOGO DA FORCA                            ")
print ("---------------------------------------------------------")

while tentativas < max_erros and "".join(acertos) != palavra:
    print("Palavra atual: ", end="")
    posicao = 0
    while posicao < len(palavra):
        print(acertos[posicao], end=" ")
        posicao = posicao + 1

    print()
    print("Tentativas restantes: " + str(max_erros - tentativas))
    carinha(tentativas)
    tentativa_atual = input("Tente acertar uma letra: ")
    posicao = 0
    teve_acerto = 0
    while posicao < len(palavra):
        if tentativa_atual == palavra[posicao]:
            acertos[posicao] = tentativa_atual
            teve_acerto = 1
        posicao = posicao + 1
    if teve_acerto == 0: 
        tentativas = tentativas + 1

if "".join(acertos) == palavra:
    print("PARABENS VOCE ACERTOU")
else:
    print("OPA CABECAO VOCE ERROU, TENTE NOVAMENTE")


