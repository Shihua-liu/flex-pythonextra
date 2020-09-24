import os
# maakt een input zodat je een naam van de map kan maken, en een naam kan geven
mapnaam = input("welke naam wil je voor je map")
# hier kijk hij of de map naam meer dan 0 letters heeft, zo niet dan maakt hij een map aan met de naam dat je net had gegeven
lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map" + mapnaam +" is gemaakt.")
else:
    print("je hebt geen naam ingevoerd")
