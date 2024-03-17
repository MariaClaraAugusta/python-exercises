# imprime uma arvore de natal com 'o'

altura = int(input())
string = ''

for i in range(altura):
     string = 'o' + 2 * i * 'o'
     print(f"{string:>{altura+i}}")

print(f"{'o':>{altura}}")
