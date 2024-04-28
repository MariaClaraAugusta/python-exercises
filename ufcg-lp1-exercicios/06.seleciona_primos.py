# separa numeros primos em uma nova lista
def seleciona_primos(nums):
    novo_nums = []
    for numero in nums:
        num_multiplos = 0
        for i in range(1,numero+1):
            if numero % i == 0:
                num_multiplos += 1
        if num_multiplos == 2:
            novo_nums += [numero]
    return novo_nums

nums = [3,6,9,12,15,18,19,1,2,21]

seleciona_primos(nums)
