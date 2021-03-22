import mod_calculatrice


def calcul():
    nombre1 = float(input('entrer un 1er nombre: '))
    nombre2 = float(input('entrer un second nombre: '))
    choix = int(input("Quelle opération souhaitez vous faire ?\n"
                      "1 - addition\n"
                      "2 - soustraction\n"
                      "3 - division\n"
                      "4 - multiplication\n"))

    if choix == 1:
        résultat = mod_calculatrice.addition(nombre1, nombre2)
        print(résultat)
    elif choix == 2:
        résultat = mod_calculatrice.soustraction(nombre1, nombre2)
        print(résultat)
    elif choix == 3:
        résultat = mod_calculatrice.division(nombre1, nombre2)
        print(résultat)
    elif choix == 4:
        résultat = mod_calculatrice.multiplication(nombre1, nombre2)
        print(résultat)
    repeat = int(input('Voulez vous refaire une opération ?\n'
                       '1 - OUI, 0 - NON : '))
    while repeat == 1:
        calcul()


calcul()
