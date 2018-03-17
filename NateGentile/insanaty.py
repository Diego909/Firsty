#Crear un programa que le repita al usuario all lo que dice pero con todas las vocales cambiadas por i.

fin = 1

vocales = ["a", "e", "i", "o", "u"]

while 1 == 1:

    frase = input("dimi ilgi y ti diri li mismi: ")

    for vocal in vocales:

        frase = frase.replace(vocal, "i")

    print(frase)