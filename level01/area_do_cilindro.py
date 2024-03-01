#calcula area do cilindro
import math

print("Cálculo da Superfície de um Cilindro")
print("---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro / 2

area_do_cilindro = (2 * math.pi * (raio ** 2)) + ((2 * math.pi * raio)*altura)

print("---")
print(f"Área calculada: {area_do_cilindro:.2f}")
