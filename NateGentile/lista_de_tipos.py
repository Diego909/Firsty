# obtener los tipos de datos que hay en una variable

lista_datos = [1, 2, 3, "asd", False, [], True, 23]
lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)