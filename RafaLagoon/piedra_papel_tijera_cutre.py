import random

opcion = input("Piedra, papel o tijeras: ").upper()
print("Tu opcion es:",opcion)

oponente = random.randint(1, 3)

if oponente == 1:
    opcion_oponente = "Piedra"
elif oponente == 2:
    opcion_oponente = "Papel"
elif oponente == 3:
    opcion_oponente = "Tijeras"

print("El oponente elige", opcion_oponente)

if opcion == "PIEDRA":
    if opcion_oponente == "Tijeras":
        print("Has ganado!")
    elif opcion_oponente == "Papel":
        print("Has perdido!")
    elif opcion_oponente == "Piedra":
        print("Empate!")
elif opcion == "TIJERAS":
    if opcion_oponente == "Papel":
        print("Has ganado!")
    elif opcion_oponente == "Piedra":
        print("Has perdido!")
    elif opcion_oponente == "Tijeras":
        print("Empate!")
elif opcion == "PAPEL":
    if opcion_oponente == "Piedra":
        print("Has ganado!")
    elif opcion_oponente == "Tijeras":
        print("Has perdido!")
    elif opcion_oponente == "Papel":
        print("Empate!")