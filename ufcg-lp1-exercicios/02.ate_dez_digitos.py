# calcula a diferença entre dois inteiros e imprime o resultado com exatamente 10 dígitos.

n1 = int(input())
n2 = int(input())

diferenca = n1 - n2
num_digitos = len(str(diferenca))
num_zeros = 10 - num_digitos

result = '0' * num_zeros + str(diferenca)
print(result)
