nombreEtudiants = int(
    input("Combien d'étudiants son inscrits dans votre UE ? : "))

global nomEtudiant
global noteDevoirSurveillé
global noteExamFinal
global moyenneGénérale

tabMoyenne = []
tabNomEtudiant = []
tabNoteDevoirSurveillé = []
tabNoteExamFinal = []


def ListeNotesEtudiants():
    print('No--Nom--Note Devoir Surveillé--Examen Final')
    for etudiant in range(nombreEtudiants):
        print(etudiant + 1, tabNomEtudiant[etudiant],
              tabNoteDevoirSurveillé[etudiant], tabNoteExamFinal[etudiant])


def ListeMoyennes():
    print('Nom-Moyenne')
    for etudiant in range(nombreEtudiants):
        print(tabNomEtudiant[etudiant], tabMoyenne[etudiant])


def InfosEtudiant():
    print('Nom--Note Devoir Surveillé--Note Exam Final--Moyenne')
    print("L'étudiant ayant la pplus forte moyenne")
    print(tabNomEtudiant[tabMoyenne.index(max(tabMoyenne))], tabNoteDevoirSurveillé[tabMoyenne.index(
        max(tabMoyenne))], tabNoteExamFinal[tabMoyenne.index(max(tabMoyenne))], max(tabMoyenne))
    print("L'étudiant ayant la plus faible moyenne")
    print(tabNomEtudiant[tabMoyenne.index(min(tabMoyenne))], tabNoteDevoirSurveillé[tabMoyenne.index(
        min(tabMoyenne))], tabNoteExamFinal[tabMoyenne.index(min(tabMoyenne))], min(tabMoyenne))


def moyenneGlobale():
    print('Moyenne Générale Globale des étudiants')
    print(sum(tabMoyenne) / len(tabMoyenne))


def compteEtudiants():
    print("Nombre d'étudiants ayant une moyenne supérieure ou égale à 10")
    for moyenne in tabMoyenne:
        if moyenne >= 10:
            print(tabMoyenne.count(moyenne))
    print("Nombre d'étudiants ayant une moyenne inférieure à 10")
    for moyenne in tabMoyenne:
        if moyenne <= 10:
            print(tabMoyenne.count(moyenne))


def rechercheInfosEtudiant():
    print("Quel est le nom de l'étudiant dont vous souhaiteriez obtenir les informations ?")
    nom = input('Nom: ')
    print("Nom--Note Devoir Surveillé--Note Examen final--Moyenne")
    try:
        print(tabNomEtudiant[tabNomEtudiant.index(nom)],
              tabNoteDevoirSurveillé[tabNomEtudiant.index(nom)], tabNoteExamFinal[tabNomEtudiant.index(nom)], tabMoyenne[tabNomEtudiant.index(nom)])
    except ValueError:
        print("\nLe nom saisi n'est pas présent dans la liste des étudiants\n")


def menu():
    print("***************************Menu: Entrer la lettre correspondante pour effectuer une opération********************************** \n"
          "a - Liste des notes des étudiants\n"
          'b - Liste des moyennes Générales des étudiants\n'
          "c - Informations de l’étudiant ou des étudiants ayant la plus forte moyenne et la plus faible moyenne\n"
          "d - Moyenne Générale globale des étudiants dans l’UE\n"
          "e - Nombre d’étudiants ayant une moyenne générale supérieure ou égale à 10 et nombre d’étudiants ayant une moyenne générale inférieure à 10\n"
          "f - Recherche d’un étudiant à partir de son nom et affichage de ses informations\n"
          )
    global choixMenu
    choixMenu = input('Votre choix : ')

    if choixMenu == 'a':
        ListeNotesEtudiants()
    elif choixMenu == 'b':
        ListeMoyennes()
    elif choixMenu == 'c':
        InfosEtudiant()
    elif choixMenu == 'd':
        moyenneGlobale()
    elif choixMenu == 'e':
        compteEtudiants()
    elif choixMenu == 'f':
        rechercheInfosEtudiant()
    else:
        print('**********Vous avez choisi une mauvaise option!**********')

    print("Souhaitez refaire une opération ?")
    global repeat
    try:
        repeat = int(input("1-OUI , 0-NON : "))
    except ValueError:
        print("*************Vous avez choisi une mauvaise option!***************\n")


for element in range(nombreEtudiants):
    print("Quel est le nom de l'étudiant", element+1, "?")
    nomEtudiant = input('Nom : ')
    tabNomEtudiant.append(nomEtudiant)
    print("Entrer la note du devoir surveillé de l'étudiant", element+1)
    noteDevoirSurveillé = float(input("Note Devoir Surveillé: "))
    while noteDevoirSurveillé < 0 or noteDevoirSurveillé > 20:
        print('Vous avez saisi une mauvaise valeur, la note doit être comprise entre 0 et 20!!')
        print("Entrer la note du devoir surveillé de l'étudiant", element+1)
        noteDevoirSurveillé = float(input("Note Devoir Surveillé: "))
    tabNoteDevoirSurveillé.append(noteDevoirSurveillé)
    print("Entrer la note de l'examen final de l'étudiant", element+1)
    noteExamFinal = float(input("Note Examen Final : "))
    while noteExamFinal < 0 or noteExamFinal > 20:
        print(
            'Vous avez saisi une mauvaise valeur, la note doit être comprise entre 0 et 20!!')
        print("Entrer la note de l'examen final de l'étudiant", element+1)
        noteExamFinal = float(input("Note Examen Final : "))
    tabNoteExamFinal.append(noteExamFinal)
    moyenneGénérale = ((noteDevoirSurveillé * 40 / 100) +
                       (noteExamFinal * 60 / 100))
    tabMoyenne.append(moyenneGénérale)

menu()

while repeat == 1:
    menu()
