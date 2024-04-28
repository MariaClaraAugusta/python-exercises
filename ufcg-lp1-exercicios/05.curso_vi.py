#acrescenta ou decrementa de acordo com a posição do cursor
def cursor(posicao, direcao):
    quant = int(direcao[0])
    sentido = direcao[1]
    if sentido == 'h':
        posicao[1] -= quant
    elif sentido == 'j':
        posicao[0] += quant
    elif sentido == 'k':
        posicao[0] -= quant
    elif sentido == 'l':
        posicao[1] += quant

pos_atual = input().split()
pos_atual = [int(e) for e in pos_atual]

while True:
    direcao = input()
    if direcao == '':
        break
    direcao = direcao.split()
    cursor(pos_atual, direcao)
    print(f"[{pos_atual[0]} {pos_atual[1]}]")
