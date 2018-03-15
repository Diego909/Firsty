#Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.

lista_datos = ["caja", 3, 4, "hola"]
lista_strings = []
lista_integers = []

for dato in lista_datos:
    if type(dato) == str:
        lista_strings.append(dato)
    elif type(dato) == int:
        lista_integers.append(dato)

print("Strings: ", lista_strings)
print("Enteros: ", lista_integers)