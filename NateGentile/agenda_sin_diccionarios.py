
agenda = []
salida = False


while not salida:
    user_choice = input("Que quieres hacer: [Añadir un numero (A) / Consultar un numero (C) / Salir (S)] ").upper()

    #Añadiendo numero
    if user_choice == "A":
        nombre = input("Dime el nombre del numero que quieres añadir: ")
        numero = input("Dime el número: ")
        agenda.append([nombre, numero])

    #Consultando numero
    elif user_choice == "C":
        consulta = input("Dime el nombre del numero que quieres saber: ")
        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])

    #Salir
    elif user_choice == "S":
        salida = True