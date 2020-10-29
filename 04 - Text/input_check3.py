import re


while True:

    invoer1 = input("Voer je telefoonnummer in: ")

    patroon1 = r"^06-?\d{8}$"
    matches1 = re.findall(patroon1, invoer1)
    
    if(len(matches1) > 0):
        break

while True:

    invoer = input("Voer je postcode in: ")

    patroon = r"^\d{4}\s?\D{2}$"
    matches = re.findall(patroon, invoer)
    
    if(len(matches) > 0):
        break

while True:
    
    invoer2 = input("Voer je kenteken in:")

    patroon2 = r"^\D{2}-123-\D{3}"
    matches2 = re.findall(patroon2, invoer2)

    if (len(matches2) > 0):
        break

print("Bedankt nummer in juiste formaat:", matches1[0])
print("uw postcode is dus:", matches[0])
print("uw kenteken is:", matches2[0])
