elemento = int(input())
num_impares = 0
num_pares = 0

while True:
    if elemento == 1:
        num_impares += 1
        break
    if elemento % 2 == 0:
        num_pares += 1
        elemento = elemento / 2
    else:
        num_impares += 1
        elemento = elemento * 3 + 1


print(f"> ímpares: {num_impares}")
print(f"> pares: {num_pares}")
