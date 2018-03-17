
def string_reverse(string_to_reverse):

    string_reversed = ""
    current_index = len(string_to_reverse) - 1

    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed

frase = input("dime una frase o palabra: ")

esarf = string_reverse(frase)

print(esarf)