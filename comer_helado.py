
apetece_helado_input = input("Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetecce_helado = True
else:
    print("Pues nada")
    exit()
dinero = input("Tienes dinero? (Si / No): ").upper()
tia = input("Ha venido tu tia? (Si / No): ").upper()
if dinero == "SI" or tia == "SI":
    transaccion = True
else:
    print("Pues nada")
    exit()
vendedor_input = input("Esta el vendedor de helados? (Si/No):" ).upper()
if vendedor_input == "SI":
    vendedor = True
else:
    vendedor = False

if apetecce_helado and transaccion and vendedor:
    print("Pues toma tu helado.")
else:
    print("pues nada")