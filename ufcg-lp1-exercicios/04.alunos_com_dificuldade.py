alunos = input().split()
notas = input().split()
notas = [float(n) for n in notas]

media_turma = 0

for n in notas:
    media_turma += n

media_turma /= len(notas)

for i in range(len(alunos)):
    media = (notas[2*i] + notas[2*i+1]) / 2
    if media < media_turma:
        print(f"- {notas[2*i]:.1f} {notas[2*i+1]:.1f} ({media:.1f}) {alunos[i]}")


print(f"> media turma: {media_turma:.2f}")
