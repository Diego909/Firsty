# Create a calculator that's ask to the user what kind of operation he want and two numbers for.

repeticion = 1
operacion = 0
numero1 = 0
numero2 = 0

while repeticion > 0:
    operacion = input("Que tipo de operacion deseas hacer: ( Suma / Resta / Multiplicacion / Division )").upper()

    if operacion in ["SUMA", "RESTA", "MULTIPLICACION", "DIVISION"]:
        repeticion -= 1
    else:
        print("No te he entendido")

numero1 = int(input("Di un numero: "))
numero2 = int(input("Di un segundo numero: "))

if operacion == "SUMA":
    print("El resultado es", numero1 + numero2)
elif operacion == "RESTA":
    print("El resultado es", numero1 - numero2)
elif operacion == "DIVISION":
    print("El resultado es", numero1 / numero2)
    print("El resto de la division es", numero1 % numero2)
else:
    print("El resultado es", numero1 * numero2)

print("Calculo terminado")