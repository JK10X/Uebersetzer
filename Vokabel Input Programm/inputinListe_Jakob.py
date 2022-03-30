

def main():
    import pdb
    #pdb.set_trace()
    Wortart = input("Wortart:")
    if Wortart == "N" or Wortart == "n": Wortart = "Nomen"
    if Wortart == "V" or Wortart == "v": Wortart = "Verb"
    
    VokabelZeile = ""
    print(Wortart)
    if Wortart == "Nomen":
        Nominativ = input("Nominativ:")
        Genitiv = input("Genitiv:")
        GenitivPlural = input("GenitivPlural:")
        Geschlecht = input("Geschlecht:")
        Erweiterung = ""
        Stamm = ""        
        for Deklination in ["om","af","drf","drfE","drm","drmE","drn", "drnE", "drni", "ef", "em", "on", "um"]:
            if Geschlecht == "m":
                if Genitiv[-2:-1] == "ei": Deklination = "e"; Stamm = Genitiv[0:-2]
                else:
                    if Genitiv[-1] == "i":
                        Stamm = Genitiv[0:-1]
                        Deklination = "o"
                    if Genitiv[-2:] == "us":
                        Stamm = Genitiv[-2:] 
                        Deklination = "u"
                    if Genitiv[-2:] == "is": 
                        Deklination = "dr"
                        if GenitivPlural[-3:-1] == "ium": Erweiterung = "E"
                        Stamm = Genitiv[0:-2]
            if Geschlecht == "f":
                if Genitiv[-2:] == "ei": Deklination = "e"
                else:
                    if Genitiv[-2:] == "ae":
                        Deklination = "a"
                        Stamm = Genitiv[-2:]
        Uebersetzung = input("Uebersetzung:")
                        
                    
                
        VokabelZeile = f"{Nominativ}#{Stamm}#{Deklination}#{Geschlecht}{Erweiterung}#{Uebersetzung}"
        print(VokabelZeile)
if __name__ == "__main__":
    main()