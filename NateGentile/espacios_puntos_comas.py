#Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario.

frase = input("Escribe una frase: (Con puntos, comas y espacios) ")

print("Tu frase es {}".format(frase))

cuenta_espacios = 0
cuenta_puntos = 0
cuenta_comas = 0

for caracteres in frase:
    if caracteres == " ":
        cuenta_espacios += 1
    elif caracteres == ".":
        cuenta_puntos += 1
    elif caracteres == ",":
        cuenta_comas += 1

print("Espacios: {} ".format(cuenta_espacios))
print("Puntos: {} ".format(cuenta_puntos))
print("Comas: {} ".format(cuenta_comas))