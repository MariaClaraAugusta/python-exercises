a = int(input())
b = int(input())
c = int(input())

if a >= b and b >= c:
    msg = f"{c} {b} {a}"
elif b >= a and a >= c:
    msg = f"{c} {a} {b}"
elif a >= c and c >= b:
    msg = f"{b} {c} {a}"
elif b >= c and c >= a:
    msg = f"{a} {c} {b}"
elif c >= a and a >= b:
    msg = f"{b} {a} {c}"
else:
    msg = f"{a} {b} {c}"

print(msg)
