#Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).

def numero_en_rango (user_number, rango1, rango2):

    rango2 += 1
    rango = range(rango1, rango2)
    dentro = None

    if rango1 <= user_number <= rango2:
        dentro = True
    else:
        dentro = False

    return dentro

rango1 = int(input("dime un numero: "))

fin = True
rango2 = ""

while fin:
    rango2 = int(input("Dime un numero mas grande que en anterior: "))
    if rango2 >= rango1:
        fin = False

user_number = int(input("Dime un numero: "))

dentro = numero_en_rango(user_number, rango1, rango2)

if dentro == True:
    print("El ultimo numero esta dentro del rango")
else:
    print("El ultimo numero no esta dentro del rango")
