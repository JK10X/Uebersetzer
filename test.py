from urllib2 import urlopen as urlopen

response = urllib2.request('https://raw.githubusercontent.com/JK10X/Uebersetzer/main/to-do.txt')
data = response.read()
print(data)
