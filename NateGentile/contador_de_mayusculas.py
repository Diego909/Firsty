#Crea un programa que sea capaz de contar la cantidad de letras mayúsculas en una string introducida por el usuario.

frase = input("Escribe una frase: (Con puntos, comas y espacios) ")

print("Tu frase es {}".format(frase))

contador_mayusculas = 0

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for letra in frase:
    if letra in mayusculas :
        contador_mayusculas += 1

print("Mayusculas: ", contador_mayusculas)