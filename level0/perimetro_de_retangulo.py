# calcula e converte o perimetro de mm pra cm

base = int(input("base? "))
altura = int(input("altura? "))

perimetro_mm = (2 * base) + (2 * altura)
perimetro_cm = perimetro_mm  / 10

print(f"O perímetro resultante (em cm) é {perimetro_cm:.2f}.")
