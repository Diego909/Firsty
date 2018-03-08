import random

print("Adivina el numero")

chosen_number = random.randint(1, 10)
#print("numero:", chosen_number)

exit = False

while not exit:
    answer = int(input("Dime un numero del 1 al 10: "))
    #print(answer)
    if chosen_number == answer:
            print("Has ganado!")
            exit = True
    elif chosen_number > answer:
            print("El numero es mayor")
    else:
            print("El numero es menor")
