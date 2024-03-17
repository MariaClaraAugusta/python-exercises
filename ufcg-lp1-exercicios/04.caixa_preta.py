# para de contar o numero de dados validos quando algum numero negativo é inserido

n = int(input())
existe_negativo = False
validos = 0
msg = ''
for i in range(n):
    medicoes = input().split()
    medicoes = [int(d) for d in medicoes]

    if existe_negativo == False:
        validos += 3
        if medicoes[0] < 0:
            print("dado inconsistente. peso negativo.")
            existe_negativo = True
            validos -= 3
        elif medicoes[1] < 0:
            print("dado inconsistente. combustível negativo.")
            existe_negativo = True
            validos -= 2
        elif medicoes[2] < 0:
            print("dado inconsistente. altitude negativa.")
            existe_negativo = True
            validos -= 1

print(f"{validos} dados válidos.")
