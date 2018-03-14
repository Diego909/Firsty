
lista = []
input_usuario = input("Que quieres comprar: (Escribe 'Fin' para salir) ").capitalize()

while input_usuario != "Fin":
    lista.append(input_usuario)
    input_usuario = input("Que quieres comprar: (Escribe 'Fin' para salir) ").capitalize()

largo_lista = len(lista)

for indice in lista:
    print("Tengo que comprar: {}".format(indice))

print("La lista ha terminado")