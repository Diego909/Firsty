
agenda = dict()
salida = False


while not salida:
    user_choice = input("Que quieres hacer: [Añadir un numero (A) / Consultar un numero (C) / Salir (S)] ").upper()

    #Añadiendo numero
    if user_choice == "A":
        nombre = input("Dime el nombre del numero que quieres añadir: ")
        numero = input("Dime el número: ")
        agenda[nombre] = numero

    #Consultando numero
    elif user_choice == "C":
        consulta = input("Dime el nombre del numero que quieres saber: ")
        print(agenda[consulta])

    #Salir
    elif user_choice == "S":
        salida = True