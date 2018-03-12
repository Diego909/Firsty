
number_to_guess = 4

user_number = int(input("Intenta adivinar un numero del 1 al 5: "))

if user_number == number_to_guess:
    print("Es correcto")
else:
    print("No es correcto, intentelo de nuevo.")
    user_number = int(input("Intenta adivinar un numero del 1 al 5: "))
    if user_number == number_to_guess:
        print("Es correcto")
    else:
        print("No es correcto, intentelo de nuevo.")
        user_number = int(input("Intenta adivinar un numero del 1 al 5: "))
        if user_number == number_to_guess:
            print("Es correcto")
        else:
            print("No es correcto, intentelo de nuevo.")
            user_number = int(input("Intenta adivinar un numero del 1 al 5: "))
            if user_number == number_to_guess:
                print("Es correcto")
            else:
                print("No es correcto, intentelo de nuevo.")
                user_number = int(input("Intenta adivinar un numero del 1 al 5: "))
                if user_number == number_to_guess:
                    print("Es correcto")
                else:
                    print("No es correcto, eres mu tonto")