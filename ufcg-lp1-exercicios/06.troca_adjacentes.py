# recebe uma lista de inteiros e troca pares de elementos adjacentes se uma das
# seguintes condições for satisfeita:
# 1. o segundo elemento do par é maior do que o primeiro; ou,
# 2. um for múltiplo do outro.

def eh_multiplo(num1,num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True

def troca_adjacentes(inteiros):
    pares_trocados = 0
    for i in range(0, len(inteiros)-1, 2):
        temp = inteiros[i]
        if inteiros[i+1] > inteiros[i] or eh_multiplo(inteiros[i],inteiros[i+1]):
            inteiros[i] = inteiros[i+1]
            inteiros[i+1] = temp
            pares_trocados += 1
    return pares_trocados


lista = [6,2,3,1,2,2]
troca_adjacentes(lista)
