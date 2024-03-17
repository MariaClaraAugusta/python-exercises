j1 = input()
j2 = input()

if  (j1 == "pedra" and j2 == "tesoura") or (j1 == "tesoura" and j2 == "papel") or\
(j1 == "papel" and j2 == "pedra"):
    print(f"j1 vence: {j1} ganha de {j2}")
elif  (j2 == "pedra" and j1 == "tesoura") or (j2 == "tesoura" and j1 == "papel") or\
(j2 == "papel" and j1 == "pedra"):
    print(f"j2 vence: {j2} ganha de {j1}")
elif j1 == j2:
    print(f"empate: {j1} empata com {j2}")
