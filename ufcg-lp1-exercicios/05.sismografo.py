# para de medir quando o limite de sismo é atingido
soma = 0
medicoes = 0
media = 0

while True:
    sismo = float(input())
    soma += sismo
    medicoes += 1
    media = soma / medicoes

    print(f"m = {sismo:.1f} (média = {media:.1f})")
    if sismo > 10:
        print("ALERTA: limite de sismo atingido!")
        break
print(f"número de medições: {medicoes}")
