#Dada una lista de strings, devolver una lista con el largo de cada string.

lista_datos = ["hola", "rambo", "colonia"]
lista_largo = []

for dato in lista_datos:
    lista_largo.append(len(dato))

print(lista_largo)