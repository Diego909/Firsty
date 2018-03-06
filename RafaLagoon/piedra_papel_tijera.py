import random

opcion = input("Piedra, papel o tijeras: ").upper()
print("Tu opcion es:",opcion)

oponente = random.randint(1, 3)

if oponente == 1:
    opcion_oponente = "PIEDRA"
elif oponente == 2:
    opcion_oponente = "PAPEL"
elif oponente == 3:
    opcion_oponente = "TIJERAS"

print("El oponente elige", opcion_oponente)

if opcion == opcion_oponente:
    print("Has empatado")

elif opcion == "PIEDRA":
    if opcion_oponente == "TIJERAS":
        print("Has ganado!")
    elif opcion_oponente == "PAPEL":
        print("Has perdido!")
elif opcion == "TIJERAS":
    if opcion_oponente == "PAPEL":
        print("Has ganado!")
    elif opcion_oponente == "PIEDRA":
        print("Has perdido!")
elif opcion == "PAPEL":
    if opcion_oponente == "PIEDRA":
        print("Has ganado!")
    elif opcion_oponente == "TIJERAS":
        print("Has perdido!")