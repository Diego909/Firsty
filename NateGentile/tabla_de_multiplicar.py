#Tabla de multiplicar en la que el usuario elige el numero que desea multiplicar. Hasta multiplo 10

numero = int(input("¿Que numero quieres multiplicar?: "))

for multiplo in range(1, 11):
    print("{} X {} = {}".format(numero, multiplo, numero * multiplo))
