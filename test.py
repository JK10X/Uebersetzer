import urllib
from urllib import request

response = request.urlopen('https://raw.githubusercontent.com/JK10X/Uebersetzer/main/to-do.txt')
data = response.read()
data = data.decode()
 
#print(data)

l = ["hallo", "hallo1", "hallo2"]
m = ["tschüss","tschüss1","tschüss2"]

for x,Bindung in enumerate((["aba","Imperfekt#Aktiv#Indikativ"],["e","Präsens#Aktiv#Konkunktiv"],["are","Imperfekt#Aktiv#Konjuktiv"])):
    print(x)
    print(Bindung)
    #print("KonjPrä="+KonjPrä)
    
for x, o in enumerate(l):
    print(f"nummer={x}")
    print(f"element={o}")

t = 1
print(f"t={t-3}")