#adivina un numero. Jueg# o entre dos jugadores. Se pide un numero para adivinar a un jugador y el otro debe adivinarlo. intentos infinitos hasta que este lo adivine. Intentar ocultar el numero.

print("Este es un juego para dos jugadores. Un jugador eligira un numero entre el 1 y el 10 y el otro jugador tiene 3 intentos para adivinarlo. Se especificara si es mayor o menor en caso de no acertar")

jugador1 = int(input("Dime un numero para adivinar:"))
oportunidades = 3

print("Turno del segundo jugador")

while oportunidades >= 1:
    jugador2 = int(input("Adivina el numero: "))

    if jugador1 < jugador2:
        print("El numero es mas pequeño")
        oportunidades -= 1
    elif jugador1 > jugador2:
        print("El numero es mas grande")
        oportunidades -= 1
    else:
        print("Has adivinado el numero!")
        oportunidades = 0

print("El juego ha terminado")