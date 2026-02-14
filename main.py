palavras = ['porta', 'chapeu', 'cadeira', 'controle', 'aspirador', 'ventilador']
palavra = ""

tamanho = 0
while tamanho < 5 or tamanho > 10:
    tamanho = int(input("Oiii, digite o numero de caracteres para a palavra do jogo: "))

    if tamanho < 5:
        print(" o numero deve ser maior que 4")

    if tamanho > 10:
        print(" o numero deve ser menor que 11")

comprimento = len(palavras)
print(comprimento)

posicao = 0

while posicao < comprimento:
    if tamanho == len(palavras[posicao]):
        palavra = palavras[posicao]
    posicao = posicao + 1
