#Programa un codigo que utilizando el metodo "replace" de las strings me sustituya las claves de mi string inicial

valores_a_sustituir = [1, 2, "Hola", "adios"]
string_a_cambiar = "Hola, numero {}, numero {}, {} y {}"

for valor in valores_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("{}", str(valor), 1)

print(string_a_cambiar)