import os
import sys

global repeat
repeat=""
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def ImportNomen():
    global Nomen
    global NomenListe
    NomenListe = []
    Nomen = open('Worte/Nomen.txt','r')
    for Zeile in Nomen:
        NomenListe.append(Zeile.rstrip())
def ImportVerben():
    global Verben
    global VerbenListe
    VerbenListe = []
    Verben = open('Worte/Verben.txt','r')
    for Zeile in Verben:
        VerbenListe.append(Zeile.rstrip())
def ImportEndungen():

    omListe = []
    om = open('Endungen/Nomen/om.txt','r')
    for Zeile in om:
        omListe.append(Zeile.rstrip())


    onListe = []
    on = open('Endungen/Nomen/on.txt','r')
    for Zeile in on:
        onListe.append(Zeile.rstrip())

    afListe = []
    af = open('Endungen/Nomen/af.txt','r')
    for Zeile in af:
        afListe.append(Zeile.rstrip())
    
    drmListe = []
    drm = open('Endungen/Nomen/drm.txt','r')
    for Zeile in drm:
        drmListe.append(Zeile.rstrip())

    drnListe = []
    drn = open('Endungen/Nomen/drn.txt','r')
    for Zeile in drn:
        drnListe.append(Zeile.rstrip())
    
    umListe = []
    um = open('Endungen/Nomen/drn.txt','r')
    for Zeile in um:
        umListe.append(Zeile.rstrip())

    drniListe = []
    drni = open('Endungen/Nomen/drni.txt','r')
    for Zeile in drni:
        drniListe.append(Zeile.rstrip())

    drfListe = []
    drf = open('Endungen/Nomen/drf.txt','r')
    for Zeile in drf:
        drfListe.append(Zeile.rstrip())

    drmEListe = []
    drmE = open('Endungen/Nomen/drmE.txt','r')
    for Zeile in drmE:
        drmEListe.append(Zeile.rstrip())

    drfEListe = []
    drfE = open('Endungen/Nomen/drfE.txt','r')
    for Zeile in drfE:
        drfEListe.append(Zeile.rstrip())

    drnEListe = []
    drnE = open('Endungen/Nomen/drnE.txt','r')
    for Zeile in drnE:
        drnEListe.append(Zeile.rstrip())

    emListe = []
    em = open('Endungen/Nomen/em.txt','r')
    for Zeile in em:
        emListe.append(Zeile.rstrip()) 

    efListe = []
    ef = open('Endungen/Nomen/ef.txt','r')
    for Zeile in ef:
        efListe.append(Zeile.rstrip()) 

    global Endungen
    Endungen = {
        "om" : omListe,
        "on" : onListe,
        "af" : afListe,
        "drm" : drmListe,
        "drn" : drnListe,
        "um" : umListe,
        "drni": drniListe,
        "drf" : drfListe,
        "drmE" : drmEListe,
        "drfE" : drfEListe,
        "drnE" : drnEListe,
        "em" : emListe,
        "ef" : efListe }
    
    global präsens
    global imperfekt
    global perfect
    global imperativ
    global passiv
    präsens = ["o","s","t","mus","tis","nt"]
    imperfekt = ["m","s","t","mus","tis","nt"]
    perfect = ["i","isti","it","imus","istis","erunt"]
    passiv = ["r","ris","tur","mur","mini","ntur"]
    imperativ = ["","te"]
def funktionrepeat(repeatnow):
    if repeatnow == "n": sys.exit
    while repeatnow == "y":
        main()
    while repeatnow == "clear":
        clearConsole()
        main()
def setup():
    clearConsole()
    ImportNomen()
    ImportEndungen()
    ImportVerben()

def main():
    global repeat
    inputString = input("Input: ")
    inputListe = inputString.split()

    outputListe = []
    formenListe = []

    print(inputListe)

    for Wort in inputListe:
        form = ""
        output = ""
        for NomenZeile in NomenListe: #Nomen

            NomenZeile = NomenZeile.split("#") #"import" des Nomen
            NomenEndungen = NomenZeile[2]+NomenZeile[3] #welche Endung
            NomenEndungen = Endungen[NomenEndungen]
            NomenNominativ = NomenZeile[0]
            if Wort == NomenNominativ: #Nominativ
                if form != "":
                        form = form+" or "
                form = f"Nomen#{NomenZeile[0]}#{NomenZeile[2]}#{NomenZeile[3]}Nominativ#Singular"

                if output != "":
                        output = output+" or "
                output = NomenZeile[4]

                print(Wort," = ",NomenZeile[4],"(Nominativ, Singular)")


            for x, Endung in enumerate(NomenEndungen):
                allreadythere = 0
                WortDekliniert = NomenZeile[1]+Endung
                if Wort == WortDekliniert:
                    if form != "": #mehrere bedeutung werden mit "or" gespeichert
                        form = form+" or "

                    form = form+"Nomen#"+NomenZeile[0]+"#"+NomenZeile[2]+"#"+NomenZeile[3]
                    print(Wort ," = ", NomenZeile[4], end = "")

                    outputSplit = output.split(" or ")
                    for outputInListe in outputSplit:
                        if outputInListe == NomenZeile[4]:
                            allreadythere = 1

                    if output != "": #mehrere bedeutung werden mit "or" gespeichert
                        output = output+" or "
                    if allreadythere == 1: #mehrere formen aber gleiches Wort = in output "/"
                        output = output+"/"
                    else:
                        output = output+NomenZeile[4]

                    if x == 0 or x == 5:
                        form = form+"#Genitiv"
                        print(" (Genitiv, ", end = ""),
                    if x == 1 or x == 6:
                        print(" (Dativ, ", end = ""),
                        form = form+"#Dativ"
                    if x == 2 or x == 7:
                        form = form+"#Akkusativ"
                        print(" (Akkusativ, ", end = ""),
                    if x == 3 or x == 8:
                        form = form+"#Ablativ"
                        print(" (Ablativ, ", end = ""),
                    if x == 4:
                        form = form+"#Nominativ"
                        print(" (Nominativ, ", end = ""),

                    if x <= 3:
                        form = form+"#Singular"
                        print("Singular)"),
                    if x >= 4:
                        form = form+"#Plural"
                        print("Plural)"),

                if NomenZeile[2] == "o" and x == 0: #Vokativ, Singular
                    WortDekliniert = NomenZeile[1]+"e"
                    if WortDekliniert == Wort:
                        form = form+"Nomen#"+NomenZeile[0]+"#"+NomenZeile[2]+"#"+NomenZeile[3]
                        form = form+"#Singular#Vokativ"
                        print(Wort, " = ", NomenZeile[4],end = "")
                        print(" (Vokativ, Singular)"),



        for VerbenZeile in VerbenListe: #Verben
            VerbenZeile = VerbenZeile.split("#")

            if Wort == VerbenZeile[0]: #Infinitiv, Präsens, Aktiv
                print(Wort," = ","Infinitiv#Präsens#Aktiv von ",VerbenZeile[5])

            if VerbenZeile[4] == "a": #a-Konjugation

                for Endungsnummer, Endung in enumerate(präsens): #Präsens, Aktiv
                    if Endungsnummer == 0:
                        vokabelKonjugiert = VerbenZeile[1]+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                    else:
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert: 
                            if Endung == "s":
                                print("2.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                            if Endung == "t":
                                print("3.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                            if Endung == "mus":
                                print("1.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                            if Endung == "tis":
                                print("2.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                            if Endung == "nt":
                                print("3.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Präsens, Passiv:
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                    if Wort == vokabelKonjugiert:             
                        if Endung == "ris":
                            print("2.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tur":
                            print("3.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "ntur":
                            print("3.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                for Endungsliste in [imperfekt, passiv]: #Imperfekt, Aktiv; Präsens/Imperfekt, Konjuktiv:
                    for Endungsnummer, Endung in enumerate(Endungsliste):
                        for Bindung,KonjPrä in ["aba","Imperfekt#Aktiv#Indikativ"],["e","Präsens#Aktiv#Konkunktiv"],["are","Imperfekt#Aktiv#Konjuktiv"]:
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                Nummerus = "Singular"
                                Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                            vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                            if Wort == vokabelKonjugiert:
                                print(f"{Person}.#{Nummerus}#{KonjPrä} von {VerbenZeile[5]}")




                for Endung in präsens: #Futur, Aktiv
                    if Endung == "o":
                        vokabelKonjugiert = VerbenZeile[1]+"ab"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "nt":
                        vokabelKonjugiert = VerbenZeile[1]+"abu"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"abi"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "s":
                            print("2.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Futur, Passiv
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"abo"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ntur":
                        vokabelKonjugiert = VerbenZeile[1]+"abu"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ris":
                        vokabelKonjugiert = VerbenZeile[1]+"abe"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("2.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"abi"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "tur":
                            print("3.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperativ: #Imperativ 1
                    vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "":
                            print("Singular#Imperativ# von ",VerbenZeile[5])

                        if Endung == "te":
                            print("Plural#Imperativ# von ",VerbenZeile[5])

                if Wort == VerbenZeile[1]+"ari": #Infinitiv, Präsens, Passiv
                    print(Wort," = ","Infinitiv#Präsens#Passiv von ",VerbenZeile[5])

            if VerbenZeile[4] == "e": #e-Konjugation
                for Endung in präsens: #Präsens, Aktiv

                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "o":
                            print("1.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "s":
                            print("2.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "nt":
                            print("3.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Präsens, Passiv:
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:             
                        if Endung == "ris":
                            print("2.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tur":
                            print("3.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "ntur":
                            print("3.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperfekt: #Imperfekt, Aktiv; Präsens/Imperfekt, Aktiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["ba","Imperfekt#Aktiv#Indikativ"],["a","Präsens#Aktiv#Konkunktiv"],["re","Imperfekt#Aktiv#Konjuktiv"]:
                        vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "m":
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "s":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "t":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mus":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tis":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "nt":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in passiv: #Imperfekt, Passiv; Präsens/Imperfekt, Passiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["ba","Imperfekt#Passiv#Indikativ"],["a","Präsens#Passiv#Konkunktiv"],["re","Imperfekt#Passiv#Konjuktiv"]:
                        vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "r": 
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "ris":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tur":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mur":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mini":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "ntur":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in präsens: #Futur, Aktiv
                    if Endung == "o":
                        vokabelKonjugiert = VerbenZeile[1]+"b"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "nt":
                        vokabelKonjugiert = VerbenZeile[1]+"bu"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"bi"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "s":
                            print("2.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Futur, Passiv
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"bo"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ntur":
                        vokabelKonjugiert = VerbenZeile[1]+"bu"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ris":
                        vokabelKonjugiert = VerbenZeile[1]+"be"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("2.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"bi"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "tur":
                            print("3.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperativ: #imperativ 1
                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "":
                            print("Singular#Imperativ# von ",VerbenZeile[5])

                        if Endung == "te":
                            print("Plural#Imperativ# von ",VerbenZeile[5])

                if Wort == VerbenZeile[1]+"ri": #Infinitiv, Präsens, Passiv
                    print(Wort," = ","Infinitiv#Präsens#Passiv von ",VerbenZeile[5])

            if VerbenZeile[4] == "i": #i-Konjugation

                for Endung in präsens: #Präsens, Aktiv
                    if Endung == "nt":
                        vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "o":
                            print("1.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "s":
                            print("2.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Präsens, Passiv:
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ntur":
                        vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:             
                        if Endung == "ris":
                            print("2.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tur":
                            print("3.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperfekt: #Imperfekt, Aktiv; Präsens/Imperfekt, Aktiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["eba","Imperfekt#Aktiv#Indikativ"],["a","Präsens#Aktiv#Konkunktiv"],["re","Imperfekt#Aktiv#Konjuktiv"]:
                        vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "m":
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "s":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "t":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mus":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tis":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "nt":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in passiv: #Imperfekt, Passiv; Präsens/Imperfekt, Passiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["eba","Imperfekt#Passiv#Indikativ"],["a","Präsens#Passiv#Konkunktiv"],["raudianture","Imperfekt#Passiv#Konjuktiv"]:
                        vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "r": 
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "ris":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tur":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mur":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mini":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "ntur":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in imperfekt: #Futur, Aktiv
                    if Endung == "m":
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])


                    vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "s":
                            print("2.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "nt":
                            print("3.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Futur, Passiv
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])


                    vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "ris":
                            print("2.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tur":
                            print("3.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "ntur":
                            print("3.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperativ: #Imperativ 1
                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "":
                            print("Singular#Imperativ# von ",VerbenZeile[5])

                        if Endung == "te":
                            print("Plural#Imperativ# von ",VerbenZeile[5])

                if Wort == VerbenZeile[1]+"ri": #Infinitiv, Präsens, Passiv
                    print(Wort," = ","Infinitiv#Präsens#Passiv von ",VerbenZeile[5])

            if VerbenZeile[4] == "kons": #konsonantische Kojugation

                for Endung in präsens: #Präsens, Aktiv
                    if Endung == "nt":
                        vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "o":
                        vokabelKonjugiert = VerbenZeile[1]+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"i"+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "s":
                            print("2.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Präsens, Passiv:
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ntur":
                        vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ris":
                        vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("2.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+"i"+Endung
                    if Wort == vokabelKonjugiert:             
                        if Endung == "tur":
                            print("3.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperfekt: #Imperfekt, Aktiv; Präsens/Imperfekt, Aktiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["eba","Imperfekt#Aktiv#Indikativ"],["a","Präsens#Aktiv#Konkunktiv"],["re","Imperfekt#Aktiv#Konjuktiv"]:
                        if Bindung != "re": vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        else:
                            vokabelKonjugiert = VerbenZeile[0]
                            vokabelKonjugiert = vokabelKonjugiert[0:-2]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "m":
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "s":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "t":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mus":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tis":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "nt":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in passiv: #Imperfekt, Passiv; Präsens/Imperfekt, Passiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["eba","Imperfekt#Passiv#Indikativ"],["a","Präsens#Passiv#Konkunktiv"],["re","Imperfekt#Passiv#Konjuktiv"]:
                        if Bindung != "re": vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        else:
                            vokabelKonjugiert = VerbenZeile[0]
                            vokabelKonjugiert = vokabelKonjugiert[0:-2]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "r": 
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "ris":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tur":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mur":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mini":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "ntur":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in imperfekt: #Futur, Aktiv
                    if Endung == "m":
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])


                    vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "s":
                            print("2.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "nt":
                            print("3.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Futur, Passiv
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])


                    vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "ris":
                            print("2.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tur":
                            print("3.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "ntur":
                            print("3.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperativ: #Imperativ 1
                    if Endung == "":
                        vokabelKonjugiert = VerbenZeile[0]
                        vokabelKonjugiert = vokabelKonjugiert[0:-2]+Endung
                        if Wort == vokabelKonjugiert:
                            print("Singular#Imperativ# von ",VerbenZeile[5])

                    if Endung == "te":
                        vokabelKonjugiert = VerbenZeile[1]+"i"+Endung
                        if Wort == vokabelKonjugiert:
                            print("Plural#Imperativ# von ",VerbenZeile[5])

                if Wort == VerbenZeile[1]+"i": #Infinitiv, Präsens, Passiv
                    print(Wort," = ","Infinitiv#Präsens#Passiv von ",VerbenZeile[5])

            if VerbenZeile[4] == "konsI": #konsonatische Konjugation (i-Erweiterung)

                for Endung in präsens: #Präsens, Aktiv
                    if Endung == "nt":
                        vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:
                        if Endung == "o":
                            print("1.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "s":
                            print("2.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Präsens#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Präsens, Passiv:
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ntur":
                        vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("3.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    if Endung == "ris":
                        vokabelKonjugiert = VerbenZeile[0]
                        vokabelKonjugiert = vokabelKonjugiert[0:-2]+Endung
                        if Wort == vokabelKonjugiert:  
                            print("2.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                    vokabelKonjugiert = VerbenZeile[1]+Endung
                    if Wort == vokabelKonjugiert:             
                        if Endung == "tur":
                            print("3.#Singular#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Präsens#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperfekt: #Imperfekt, Aktiv; Präsens/Imperfekt, Aktiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["eba","Imperfekt#Aktiv#Indikativ"],["a","Präsens#Aktiv#Konkunktiv"],["re","Imperfekt#Aktiv#Konjuktiv"]:
                        if Bindung != "re": vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        else:
                            vokabelKonjugiert = VerbenZeile[0]
                            vokabelKonjugiert = vokabelKonjugiert[0:-2]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "m":
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "s":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "t":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mus":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tis":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "nt":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in passiv: #Imperfekt, Passiv; Präsens/Imperfekt, Passiv, Konjuktiv:
                    for Bindung,KonjPrä, in ["eba","Imperfekt#Passiv#Indikativ"],["a","Präsens#Passiv#Konkunktiv"],["re","Imperfekt#Passiv#Konjuktiv"]:
                        if Bindung != "re": vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                        else:
                            vokabelKonjugiert = VerbenZeile[0]
                            vokabelKonjugiert = vokabelKonjugiert[0:-2]+Bindung+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "r": 
                                print("1.#Singular#"+KonjPrä+" von ",VerbenZeile[5])                
                            if Endung == "ris":
                                print("2.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "tur":
                                print("3.#Singular#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mur":
                                print("1.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "mini":
                                print("2.#Plural#"+KonjPrä+" von ",VerbenZeile[5])
                            if Endung == "ntur":
                                print("3.#Plural#"+KonjPrä+" von ",VerbenZeile[5])

                for Endung in imperfekt: #Futur, Aktiv
                    if Endung == "m":
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])


                    vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "s":
                            print("2.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "t":
                            print("3.#Singular#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mus":
                            print("1.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tis":
                            print("2.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "nt":
                            print("3.#Plural#Futur#Aktiv#Indikativ von ",VerbenZeile[5])

                for Endung in passiv: #Futur, Passiv
                    if Endung == "r":
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:  
                            print("1.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])


                    vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                    if Wort == vokabelKonjugiert:               
                        if Endung == "ris":
                            print("2.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "tur":
                            print("3.#Singular#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mur":
                            print("1.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "mini":
                            print("2.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])
                        if Endung == "ntur":
                            print("3.#Plural#Futur#Passiv#Indikativ von ",VerbenZeile[5])

                for Endung in imperativ: #Imperativ 1
                    if Endung == "":
                        vokabelKonjugiert = VerbenZeile[0]
                        vokabelKonjugiert = vokabelKonjugiert[0:-2]+Endung
                        if Wort == vokabelKonjugiert:
                            print("Singular#Imperativ# von ",VerbenZeile[5])

                    if Endung == "te":
                        vokabelKonjugiert = VerbenZeile[1]+""+Endung
                        if Wort == vokabelKonjugiert:
                            print("Plural#Imperativ# von ",VerbenZeile[5])

                if Wort == VerbenZeile[1]: #Infinitiv, Präsens, Passiv
                    print(Wort," = ","Infinitiv#Präsens#Passiv von ",VerbenZeile[5])

        formenListe.append(form)
        outputListe.append(output)

    print(formenListe)
    print(outputListe)

    e= input("Repeat?(y/n)")
    repeat=e

setup()
main()
funktionrepeat(repeat)

print("hallo")