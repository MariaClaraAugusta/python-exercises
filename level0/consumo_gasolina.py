#calcula o consumo de gasolina no trajeto

pos_inicial = float(input("p0? "))
litros_inicial = float(input("l0? "))
pos_final = float(input("pf? "))
litros_final = float(input("lf? "))

dist = pos_final - pos_inicial
litros_gastos = litros_final - litros_inicial

consumo = dist / litros_gastos

print(f"p0? {pos_inicial:.1f}")
print(f"l0? {litros_inicial:.1f}")
print(f"pf? {pos_final:.1f}")
print(f"lf? {litros_final:.1f}")
print(f"consumo = {consumo:.1f} km/l")
