yazilimcilar = ["Eren", "Osman", "Mehmet"]

fileToAppend = open("yazilim.txt", "w")
for ogrenci in yazilimcilar:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

yazilimcilar2 = ["Zeynep", "Ayse"]
fileToAppend = open("yazilim.txt", "a")
for ogrenci in yazilimcilar2:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
fileToAppend.close()