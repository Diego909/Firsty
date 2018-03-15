#Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.


input_frase = input("Dime una frase donde exista la letra a: ")

input_vaca = input_frase.replace("a", "VACA")

print(input_vaca)