import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        patroon = r"..."

        gevonden = re.findall(...)

        ...
        
        regel = bestand.readline()

print(emails)