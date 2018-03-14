#Tabla de multiplicar en la que el usuario elige el numero que desea multiplicar. Hasta multiplo 10 y invertido.

numero = int(input("¿Que numero quieres multiplicar?: "))

for multiplo in range(11, 1):
    print("{} X {} = {}".format(numero, multiplo, numero * multiplo))


NO TERMINADO