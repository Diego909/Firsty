#Tabla de multiplicar en la que el usuario elige el numero que desea multiplicar. Hasta multiplo 10 y invertido.

numero = int(input("¿Que numero quieres multiplicar?: "))

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiplo in lista:
    print("{} X {} = {}".format(numero, multiplo, numero * multiplo))
