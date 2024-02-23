# Gerando login do email, onde n = numero de pessoas com o mesmo nome

nome = input("nome? ")
sobrenome = input("sobrenome? ")
n = int(input("N? "))
n = str(n+1)
login = nome + n + "." + sobrenome

print(login)
