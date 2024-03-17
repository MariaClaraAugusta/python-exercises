def quadrante(angulo):
    if angulo % 90 == 0:
        msg = "Sobre eixos"
    elif angulo < 90:
        msg = "Quadrante 1"
    elif angulo < 180:
        msg = "Quadrante 2"
    elif angulo < 270:
        msg = "Quadrante 3"
    else:
        msg = "Quadrante 4"
    return msg

angulo = float(input())

if angulo > 360 or angulo < -360:
    angulo = angulo % 360

print(quadrante(angulo))
