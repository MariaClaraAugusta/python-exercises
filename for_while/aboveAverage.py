# I dont know why this isnt running on beecrowd, but the code is alright

final_grades = []
people_above_average = 0
sum = 0

n = int(input())

for i in range(n):
    grades = int(input())
    final_grades.append(grades)

for grade in final_grades:
    sum += grade

media = sum / n

for grade in final_grades:
    if grade >= media:
        people_above_average += 1

percent_above_average = (people_above_average / n) * 100

print(f"{percent_above_average:.3f}%")
