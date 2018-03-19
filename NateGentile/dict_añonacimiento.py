#Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.

agenda = dict()
salida = False

while not salida:
    user_choice = input("Que quieres hacer: [Añadir un amigo (A) / Consultar una fecha de un amigo (C) / Salir (S)] ").upper()

    #Añadiendo amigo
    if user_choice == "A":
        nombre = input("Dime el nombre del amigo que quieres añadir: ")
        fecha = input("Dime su fecha de nacimiento: ")
        agenda[nombre] = fecha

    #Consultando numero
    elif user_choice == "C":
        consulta = input("Dime el nombre del amigo: ")
        print(agenda[consulta])

    #Salir
    elif user_choice == "S":
        salida = True