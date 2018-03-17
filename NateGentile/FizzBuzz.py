#sustituir valores de esta lista siempre y cuando sean multiplos de 3 o de 5
#multiplos de 3 se sustituyen por un fizz
#multiplos de 5 se sustituyen por un buzz
#En el caso de multiplos de 3 y de 5 vamos a sustiruirlos por un FizzBuzz

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):

    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

        if numero % 3 == 0:
            numeros[indice] += "Fizz"

        if numero % 5 == 0:
            numeros[indice] += "Buzz"

print(numeros)