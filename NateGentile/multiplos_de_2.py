#Tabla de multiplicar en la que el usuario elige el numero que desea multiplicar. Solo mostrar multiplos de 2

print("Solo saldran los multiplos de dos del numero que marques")

numero = int(input("¿Que numero quieres multiplicar?: "))

for multiplo in range(1, 11):
    if (numero * multiplo)%2 == 0:
        print("{} x {} = {}".format(numero, multiplo, numero * multiplo))