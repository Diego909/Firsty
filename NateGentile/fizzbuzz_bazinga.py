#Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):

    numero = numeros[indice]

    if numero % 3 == 0:
        numeros[indice] = "Fizz"
    if numero % 5 == 0:
        numeros[indice] = "Buzz"

    if numero % 3 == 0 and numero % 5 == 0:
        numeros[indice] = "Bazinga"

print(numeros)