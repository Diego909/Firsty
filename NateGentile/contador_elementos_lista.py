#Crea un programa que cuente los elementos de la lista de números introducida por el usuario. Está prohibido utilizar la función len() para resolver el problema.

lista = []
contador = 0
elemento = ""
while not elemento == "FIN":

    elemento = input("Dime un elemento que meter en la lista: (Escribe 'FIN' para terminar de añadir) ")
    if elemento != "FIN":
        lista.append(elemento)
        contador += 1

print("Has añadido {} elementos".format(contador))