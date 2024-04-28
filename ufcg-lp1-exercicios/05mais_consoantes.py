def conta_vogais(string):
    cont_vogal = 0
    for car in string:
        if car.lower() in "aeiou":
            cont_vogal += 1
    return cont_vogal

num_palavras_lidas = 0

while True:

    palavra = input()
    num_vogais = conta_vogais(palavra)
    num_consoantes = len(palavra) - num_vogais
    num_palavras_lidas += 1

    if num_consoantes > num_vogais:
        break

print(num_palavras_lidas)
