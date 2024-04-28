# o programa para quando o limite de peso do elevador eh atingido ou a proporcao crianca/adulto nao eh atendida
razao_lim = float(input())
adulto = 0
crianca = 0
pessoas = 0
peso_total = 0
razao_ca = 0

while True:
    pessoa_peso = input().split()
    peso = float(pessoa_peso[1])

    if pessoa_peso[0] == 'a':
        adulto += 1
    elif pessoa_peso[0] == 'c':
        crianca += 1
    if adulto == 0:
        break

    razao_ca = crianca / adulto

    if razao_ca > razao_lim:
        break
    if peso_total + peso > 700:
        break

    peso_total += peso
    pessoas += 1

print("Limite atingido.")
print(f"Elevador saiu com {pessoas} pessoas e {peso_total:.2f} kg.")
