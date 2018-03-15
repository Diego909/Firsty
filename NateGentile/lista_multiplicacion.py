#Dada una lista de numeros, devolver el resultado de la multiplicacion de todos los números.

lista_datos = [1, 2, 3, 4, 5, 50]
suma = 1

for dato in lista_datos:
    suma = dato * suma

print(suma)