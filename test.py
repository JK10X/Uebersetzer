import urllib
from urllib import request

response = request.urlopen('https://raw.githubusercontent.com/JK10X/Uebersetzer/main/to-do.txt')
data = response.read()
data = data.decode()
 
print(data)
