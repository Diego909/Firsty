
def numero_mas_grande(lista_numeros):

    numero_grande = 0

    for numero in lista_numeros:
        numero > numero_grande
        numero_grande = numero

    return numero_grande

numeros = []
contador = 0

while contador < 3:
    numero = input("Dime un numero: ")
    if numero.isdigit():
        numeros.append(int(numero))
        contador += 1

numero_grande = numero_mas_grande(numeros)

print("El numero mas grande es {} ".format(numero_grande))