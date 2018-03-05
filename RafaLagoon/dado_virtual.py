
import random
dado = random.randint(1, 6)

print("Has sacado un", dado)

if dado > 3:
    print("Es mayor que 3")
if dado == 3:
    print("Es 3")
if dado < 3:
    print("Es menor que 3")