#Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario (media = suma de todos los numeros / numero de numeros )

lista = []
numero_user = ""
sumas = 0
#siguiente =

while numero_user != "FIN":
    numero_user = input("Dime un numero: ")
    if numero_user != "FIN":
        lista.append(int(numero_user))
        print("¡Numero añadido!")

print("Estos son tus numeros: ", lista)

suma = 0

for numero in lista:
    suma = numero + suma

media = suma / len(lista)

print("La media es {}".format(media))