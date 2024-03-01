# Acrescenta um '-' antes dos dois ultimos digitos do cpf e soma esses dois ultimos digitos
cpf = int(input())

primeiros_digitos_cpf = cpf // 100
ultimos_digitos_cpf = cpf % 100

digito1_poshifen_cpf = ultimos_digitos_cpf // 10
digito2_poshifen_cpf = ultimos_digitos_cpf % 10

soma_cpf = digito1_poshifen_cpf + digito2_poshifen_cpf

print(f"{primeiros_digitos_cpf}-{ultimos_digitos_cpf}")
print(soma_cpf)
