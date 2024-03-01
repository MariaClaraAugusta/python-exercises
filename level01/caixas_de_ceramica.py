# quantidade de caixas de ceramicas necessarias para revestir o ambiente

capacidade_revestimento = float(input("Capacidade de revestimento? "))
print('')
print("== Dados do vão a revestir ==")

comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

area_ambiente = (comprimento * largura) + 2 * (largura * altura) + 2 * (comprimento * altura)
numero_caixas = area_ambiente / capacidade_revestimento


print('')
print("== Resultados ==")
print(f"Área total a revestir: {area_ambiente:.1f} m2")
print(f"Número de caixas: {numero_caixas:.0f}")
