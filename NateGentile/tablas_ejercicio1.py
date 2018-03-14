#Tabla de multiplicar en la que el usuario elige el numero que desea multiplicar. Multiplos del 5 al 15

numero = int(input("¿Que numero quieres multiplicar?: "))

for multiplo in range(5, 16):
    print("{} X {} = {}".format(numero, multiplo, numero * multiplo))
