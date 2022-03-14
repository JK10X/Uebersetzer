def clearConsole():
    import os
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def inputf():
    inputString = input("Input: ")
    inputListe = inputString.split()
    print(inputListe)
    return(inputListe)
def funktionrepeat(repeatnow):
    import uebersetzer
    if repeatnow == "n": quit()
    if repeatnow == "y":
        return("y")
    if repeatnow == "clear":
        uebersetzer.clearConsole()
        return("y")

def bestimmen(In):
    Endungen = {} #Variable die in verschiedenen Funktionen verwendet werden
    präsens = []
    imperfekt = []
    perfect = []
    imperativ = []
    passiv = []
    VerbenListe = []
    NomenListe = []
    form = ""
    output = ""

    def ImportEndungen():
        nonlocal Endungen
        Endungen = {}
        for Dg in ["om","af","drf","drfE","drm","drmE","drn", "drnE", "drni", "ef", "em", "on", "um"]:
            locals()[Dg+"Liste"] = []
            with open('Endungen/Nomen/'+Dg+'.txt','r') as locals()[Dg]:

                for Zeile in locals()[Dg]:
                    locals()[Dg+"Liste"].append(Zeile.rstrip())
            
            Endungen[Dg] = locals()[Dg+"Liste"]

        nonlocal präsens
        nonlocal imperfekt
        nonlocal perfect
        nonlocal imperativ
        nonlocal passiv
        präsens = ["o","s","t","mus","tis","nt"]
        imperfekt = ["m","s","t","mus","tis","nt"]
        perfect = ["i","isti","it","imus","istis","erunt"]
        passiv = ["r","ris","tur","mur","mini","ntur"]
        imperativ = ["","te"]
        return([präsens,imperfekt,perfect,passiv,imperativ])
    def ImportNomen():
        nonlocal NomenListe
        NomenListe = []
        Nomen = open('Worte/Nomen.txt','r')
        for Zeile in Nomen:
            NomenListe.append(Zeile.rstrip())
    def ImportVerben():
        nonlocal VerbenListe
        VerbenListe = []
        Verben = open('Worte/Verben.txt','r')
        for Zeile in Verben:
            VerbenListe.append(Zeile.rstrip())
    def setup():
        ImportNomen()
        ImportEndungen()
        ImportVerben()
    def formDoppelt():
        nonlocal form
        if form != "": #mehrere bedeutung werden mit "or" gespeichert
            form = form+" or "
    def outputDoppelt():
        nonlocal output
        if output != "": #mehrere bedeutung werden mit "or" gespeichert
            output = output+" or "
    def identifizierung(inputListe):
        nonlocal form
        nonlocal output
        nonlocal VerbenListe
        nonlocal NomenListe
        outputListe = []
        formenListe = []

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

                for x, Endung in enumerate(NomenEndungen):
                    allreadythere = 0
                    WortDekliniert = NomenZeile[1]+Endung
                    if Wort == WortDekliniert:
                        if form != "": #mehrere bedeutung werden mit "or" gespeichert
                            form = form+" or "

                        form = form+"Nomen#"+NomenZeile[0]+"#"+NomenZeile[2]+"#"+NomenZeile[3]

                        outputSplit = output.split(" or ")
                        for IsoutputInListe in outputSplit:
                            if IsoutputInListe == NomenZeile[4]:
                                allreadythere = 1

                        if output != "": #mehrere bedeutung werden mit "or" gespeichert
                            output = output+" or "
                        if allreadythere == 1: #mehrere formen aber gleiches Wort = in output "/"
                            output = output+"/"
                        else:
                            output = output+NomenZeile[4]

                        if x == 0 or x == 5:
                            form = form+"#Genitiv"
                        if x == 1 or x == 6:
                            form = form+"#Dativ"
                        if x == 2 or x == 7:
                            form = form+"#Akkusativ"
                        if x == 3 or x == 8:
                            form = form+"#Ablativ"
                        if x == 4:
                            form = form+"#Nominativ"

                        if x <= 3:
                            form = form+"#Singular"
                        if x >= 4:
                            form = form+"#Plural"

                    if NomenZeile[2] == "o" and x == 0: #Vokativ, Singular
                        WortDekliniert = NomenZeile[1]+"e"
                        if WortDekliniert == Wort:
                            form = form+"Nomen#"+NomenZeile[0]+"#"+NomenZeile[2]+"#"+NomenZeile[3]
                            form = form+"#Singular#Vokativ"
                            outputSplit = output.split(" or ")
                            for IsoutputInListe in outputSplit:
                                if IsoutputInListe == NomenZeile[4]:
                                    allreadythere = 1

                            if output != "": #mehrere bedeutung werden mit "or" gespeichert
                                output = output+" or "
                            if allreadythere == 1: #mehrere formen aber gleiches Wort = in output "/"
                                output = output+"/"
                            else:
                                output = output+NomenZeile[4]



            for VerbenZeile in VerbenListe: #Verben
                VerbenZeile = VerbenZeile.split("#")

                if Wort == VerbenZeile[0]: #Infinitiv, Präsens, Aktiv
                    formDoppelt()
                    outputDoppelt()
                    form = form+f"Verb#{VerbenZeile[0]}#Infinitiv#Präsens#Aktiv"
                    output = output+VerbenZeile[5]

                if VerbenZeile[4] == "a": #a-Konjugation
                    for Endungsliste, PräoPas in [präsens, "Aktiv"], [passiv, "Passiv"]:#Präsens, Indikativ
                        for Endungsnummer, Endung in enumerate(Endungsliste): 
                            KonjPrä = f"Präsens#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                            if Endungsnummer == 0:
                                if PräoPas == "Passiv":
                                    vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                                else:
                                    vokabelKonjugiert = VerbenZeile[1]+Endung
                            else:
                                vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]
                                    
                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]: #Imperfekt; Konjuktiv:
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            for Bindung,KonjPrä in ["aba",f"Imperfekt#{PräoPas}#Indikativ"],["e",f"Präsens#{PräoPas}#Konkunktiv"],["are",f"Imperfekt#{PräoPas}#Konjuktiv"]:
                                if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                                else:
                                    Nummerus = "Plural"
                                    Person = Endungsnummer-2
                                vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                                if Wort == vokabelKonjugiert:
                                    formDoppelt()
                                    outputDoppelt()
                                    form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                    output = output+VerbenZeile[5]
                                    
                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]:#Futur
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            KonjPrä = f"Futur#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                                
                            vokabelKonjugiert = VerbenZeile[1]+"abi"+Endung
                            
                            if Endungsnummer == 0:
                                if Endungsliste == imperfekt:
                                    vokabelKonjugiert = VerbenZeile[1]+"ab"+Endung
                                else:
                                    vokabelKonjugiert = VerbenZeile[1]+"abo"+Endung
                                    
                            if Endungsnummer == 5:
                                vokabelKonjugiert = VerbenZeile[1]+"abu"+Endung
                                
                            if Endungsnummer == 1 and PräoPas == "Passiv":
                                vokabelKonjugiert = VerbenZeile[1]+"abe"+Endung
                            
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]                            
                                    
                    for Endung in imperativ: #Imperativ 1
                        vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Singular"
                                output = output+VerbenZeile[5]

                            if Endung == "te":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Plural"
                                output = output+VerbenZeile[5]                                                                                                                   

                    if Wort == VerbenZeile[1]+"ari": #Infinitiv, Präsens, Passiv
                        formDoppelt()
                        outputDoppelt()
                        form = form+f"Verb#{VerbenZeile[0]}Infinitiv#Präsens#Passiv"
                        output = output+VerbenZeile[5]

                if VerbenZeile[4] == "e": #e-Konjugation
                    for Endungsliste, PräoPas in [präsens, "Aktiv"], [passiv, "Passiv"]:#Präsens, Indikativ
                        for Endungsnummer, Endung in enumerate(Endungsliste): 
                            KonjPrä = f"Präsens#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                            if Endungsnummer == 0:
                                if PräoPas == "Passiv":
                                    vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                                else:
                                    vokabelKonjugiert = VerbenZeile[1]+Endung
                            else:
                                vokabelKonjugiert = VerbenZeile[1]+Endung
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]
                                
                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]: #Imperfekt; Konjuktiv:
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            for Bindung,KonjPrä in ["ba",f"Imperfekt#{PräoPas}#Indikativ"],["a",f"Präsens#{PräoPas}#Konkunktiv"],["re",f"Imperfekt#{PräoPas}#Konjuktiv"]:
                                if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                                else:
                                    Nummerus = "Plural"
                                    Person = Endungsnummer-2
                                vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                                if Wort == vokabelKonjugiert:
                                    formDoppelt()
                                    outputDoppelt()
                                    form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                    output = output+VerbenZeile[5]

                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]:#Futur
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            KonjPrä = f"Futur#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                                
                            vokabelKonjugiert = VerbenZeile[1]+"bi"+Endung
                            
                            if Endungsnummer == 0:
                                if Endungsliste == imperfekt:
                                    vokabelKonjugiert = VerbenZeile[1]+"b"+Endung
                                else:
                                    vokabelKonjugiert = VerbenZeile[1]+"bo"+Endung
                                    
                            if Endungsnummer == 5:
                                vokabelKonjugiert = VerbenZeile[1]+"bu"+Endung
                                
                            if Endungsnummer == 1 and PräoPas == "Passiv":
                                vokabelKonjugiert = VerbenZeile[1]+"abe"+Endung
                            
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]
                                
                    for Endung in imperativ: #imperativ 1
                        vokabelKonjugiert = VerbenZeile[1]+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Singular"
                                output = output+VerbenZeile[5]

                            if Endung == "te":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Plural"
                                output = output+VerbenZeile[5]                                                                                                                   

                    if Wort == VerbenZeile[1]+"ri": #Infinitiv, Präsens, Passiv
                        formDoppelt()
                        outputDoppelt()
                        form = form+f"Verb#{VerbenZeile[0]}Infinitiv#Präsens#Passiv"
                        output = output+VerbenZeile[5]

                if VerbenZeile[4] == "i": #i-Konjugation
                    for Endungsliste, PräoPas in [präsens, "Aktiv"], [passiv, "Passiv"]:#Präsens, Indikativ
                        for Endungsnummer, Endung in enumerate(Endungsliste): 
                            KonjPrä = f"Präsens#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                            vokabelKonjugiert = VerbenZeile[1]+Endung
                            
                            if Endungsnummer == 0:
                                if PräoPas == "Passiv":
                                    vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                            if Endungsnummer == 5:
                                vokabelKonjugiert = VerbenZeile[1]+"u"+Endung

                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]

                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]: #Imperfekt; Konjuktiv:
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            for Bindung,KonjPrä in ["eba",f"Imperfekt#{PräoPas}#Indikativ"],["a",f"Präsens#{PräoPas}#Konkunktiv"],["re",f"Imperfekt#{PräoPas}#Konjuktiv"]:
                                if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                                else:
                                    Nummerus = "Plural"
                                    Person = Endungsnummer-2
                                vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                                if Wort == vokabelKonjugiert:
                                    formDoppelt()
                                    outputDoppelt()
                                    form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                    output = output+VerbenZeile[5]

                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]:#Futur
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            KonjPrä = f"Futur#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                                
                            vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                            
                            if Endungsnummer == 0:
                                vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                            
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]

                    for Endung in imperativ: #Imperativ 1
                        vokabelKonjugiert = VerbenZeile[1]+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Singular"
                                output = output+VerbenZeile[5]

                            if Endung == "te":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Plural"
                                output = output+VerbenZeile[5]                                                                                                                   

                    if Wort == VerbenZeile[1]+"ri": #Infinitiv, Präsens, Passiv
                        formDoppelt()
                        outputDoppelt()
                        form = form+f"Verb#{VerbenZeile[0]}Infinitiv#Präsens#Passiv"
                        output = output+VerbenZeile[5]

                if VerbenZeile[4] == "kons": #konsonantische Kojugation
                    for Endungsliste, PräoPas in [präsens, "Aktiv"], [passiv, "Passiv"]:#Präsens, Indikativ
                        for Endungsnummer, Endung in enumerate(Endungsliste): 
                            KonjPrä = f"Präsens#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                            vokabelKonjugiert = VerbenZeile[1]+"i"+Endung
                            
                            if Endungsnummer == 0:
                                if PräoPas == "Passiv":
                                    vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                            if Endungsnummer == 5:
                                vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                            if Endungsnummer == 1 and Endungsliste == passiv:
                                vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]

                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]: #Imperfekt; Konjuktiv:
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            for Bindung,KonjPrä in ["eba",f"Imperfekt#{PräoPas}#Indikativ"],["a",f"Präsens#{PräoPas}#Konkunktiv"],["re",f"Imperfekt#{PräoPas}#Konjuktiv"]:
                                if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                                else:
                                    Nummerus = "Plural"
                                    Person = Endungsnummer-2
                                if Bindung != "re": vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                                else:
                                    vokabelKonjugiert = VerbenZeile[0]
                                    vokabelKonjugiert = vokabelKonjugiert[0:-2]+Bindung+Endung
                                if Wort == vokabelKonjugiert:
                                    formDoppelt()
                                    outputDoppelt()
                                    form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                    output = output+VerbenZeile[5]
                                    
                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]:#Futur
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            KonjPrä = f"Futur#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                                
                            vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                            
                            if Endungsnummer == 0:
                                vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                            
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]

                    for Endung in imperativ: #Imperativ 1
                        vokabelKonjugiert = VerbenZeile[1]+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Singular"
                                output = output+VerbenZeile[5]

                            if Endung == "te":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Plural"
                                output = output+VerbenZeile[5]                         

                    if Wort == VerbenZeile[1]+"i": #Infinitiv, Präsens, Passiv
                        formDoppelt()
                        outputDoppelt()
                        form = form+f"Verb#{VerbenZeile[0]}Infinitiv#Präsens#Passiv"
                        output = output+VerbenZeile[5]

                if VerbenZeile[4] == "konsI": #konsonatische Konjugation (i-Erweiterung)
                    for Endungsliste, PräoPas in [präsens, "Aktiv"], [passiv, "Passiv"]:#Präsens, Indikativ
                        for Endungsnummer, Endung in enumerate(Endungsliste): 
                            KonjPrä = f"Präsens#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                            vokabelKonjugiert = VerbenZeile[1]+Endung
                            
                            if Endungsnummer == 0:
                                if PräoPas == "Passiv":
                                    vokabelKonjugiert = VerbenZeile[1]+"o"+Endung
                            if Endungsnummer == 5:
                                vokabelKonjugiert = VerbenZeile[1]+"u"+Endung
                            if Endungsnummer == 1 and Endungsliste == passiv:
                                vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]

                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]: #Imperfekt; Konjuktiv:
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            for Bindung,KonjPrä in ["eba",f"Imperfekt#{PräoPas}#Indikativ"],["a",f"Präsens#{PräoPas}#Konkunktiv"],["re",f"Imperfekt#{PräoPas}#Konjuktiv"]:
                                if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                                else:
                                    Nummerus = "Plural"
                                    Person = Endungsnummer-2
                                if Bindung != "re": vokabelKonjugiert = VerbenZeile[1]+Bindung+Endung
                                else:
                                    vokabelKonjugiert = VerbenZeile[0]
                                    vokabelKonjugiert = vokabelKonjugiert[0:-2]+Bindung+Endung
                                if Wort == vokabelKonjugiert:
                                    formDoppelt()
                                    outputDoppelt()
                                    form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                    output = output+VerbenZeile[5]

                    for Endungsliste, PräoPas in [imperfekt, "Aktiv"], [passiv, "Passiv"]:#Futur
                        for Endungsnummer, Endung in enumerate(Endungsliste):
                            KonjPrä = f"Futur#{PräoPas}#Indikativ"
                            if Endungsnummer == 0 or Endungsnummer == 1 or Endungsnummer == 2:
                                    Nummerus = "Singular"
                                    Person = Endungsnummer+1
                            else:
                                Nummerus = "Plural"
                                Person = Endungsnummer-2
                                
                            vokabelKonjugiert = VerbenZeile[1]+"e"+Endung
                            
                            if Endungsnummer == 0:
                                vokabelKonjugiert = VerbenZeile[1]+"a"+Endung
                            
                            if Wort == vokabelKonjugiert:
                                formDoppelt()
                                outputDoppelt()                                
                                form = form+f"Verb#{VerbenZeile[0]}#{Person}.#{Nummerus}#{KonjPrä}"
                                output = output+VerbenZeile[5]

                    for Endung in imperativ: #Imperativ 1
                        vokabelKonjugiert = VerbenZeile[1]+Endung
                        if Wort == vokabelKonjugiert:
                            if Endung == "":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Singular"
                                output = output+VerbenZeile[5]

                            if Endung == "te":
                                formDoppelt()
                                outputDoppelt()
                                form = form+f"Verb#{VerbenZeile[0]}#Imperativ#Plural"
                                output = output+VerbenZeile[5]                                                                                                                              

                    if Wort == VerbenZeile[1]: #Infinitiv, Präsens, Passiv
                        formDoppelt()
                        outputDoppelt()
                        form = form+f"Verb#{VerbenZeile[0]}Infinitiv#Präsens#Passiv"
                        output = output+VerbenZeile[5]
                        
            formenListe.append(form)
            outputListe.append(output)

        return(formenListe, outputListe)
    
    setup()
    
    identifiziert = identifizierung(In)
    
    return(identifiziert[0],identifiziert[1])
    
def main():
    inputVar = inputf()
    test = bestimmen(inputVar)
    print(test[0])
    print(test[1])
    if "y" == funktionrepeat(input("Repeat?(y/n)")): main()


if __name__ == '__main__' :
    clearConsole()
    main()