#calcula o iptu (Imposto sobre a Propriedade Predial e Territorial Urbana)

# valor fixo de R$ 35,00, referentes à limpeza urbana.
# opção do contribuinte: em cota única, o que dá direito a um
# desconto de 25%; em 6 parcelas, com direito a desconto
# de 5%; ou em 10 parcelas, sem direito a desconto.

area_construida = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

iptu = area_construida * aliquota + 35
cota_unica = (1-0.25) * iptu
desconto_6parcelas = iptu * (1 - 0.05)
iptu_6parcelas = desconto_6parcelas / 6
iptu_10parcelas = iptu / 10

print(f"IPTU: R$ {iptu:.2f}")
print('')
print("Pagamento:")
print(f"1. Quota única. R$ {cota_unica:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {desconto_6parcelas:.2f}")
print(f"   6 x R$ {iptu_6parcelas:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {iptu:.2f}")
print(f"   10 x R$ {iptu_10parcelas:.2f}")
