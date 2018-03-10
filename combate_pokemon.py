
print("Combate pokemon! Tu llevas a Picachu, tu unico pokemon.")

enemy = input("Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasur) ").upper()

print("Tu enemigo es ", enemy)

picachu_health = 100
enemy_health = 0

if enemy == "SQUIRTLE":
    enemy_health = 90
elif enemy == "CHARMANDER":
    enemy_health = 80
elif enemy == "BULBASUR":
    enemy_health = 100


while picachu_health > 0 and enemy_health > 0:
    attack = input("Que ataque quieres usar: (Chispazo / Bola Voltio) ").upper()
    if attack == "CHISPAZO":
        enemy_health -= 10
        print("Has usado Chispazo")
    elif attack == "BOLA VOLTIO":
        enemy_health -= 12
        print("Has usado Bola Voltio")

    if enemy == "SQUIRTLE":
        picachu_health -= 8
        print("Squirtle te ha hecho 8 de daño")
    elif enemy == "CHARMANDER":
        picachu_health -= 7
        print("Charmander te ha hecho 7 de daño")
    elif enemy == "BULBASUR":
        picachu_health -= 10
        print("Bulbasur te ha hecho 10 de daño")


if picachu_health <= 0 and enemy_health <= 0:
    print("Habeis empatado.")
elif picachu_health > 0 and enemy_health <= 0:
    print("Has ganado")
else:
    print("Has perdido")

print("El combate ha terminado")