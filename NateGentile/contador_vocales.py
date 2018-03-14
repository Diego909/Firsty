#Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario.

frase = input("Escribe una frase: ")

print("Tu frase es {}".format(frase))

lista_vocales = ["a", "e", "i", "o", "u"]
vocales_output = []

for letra in frase:
    if letra in lista_vocales:
        vocales_output.append(letra)

print("vocales = {}".format(vocales_output))