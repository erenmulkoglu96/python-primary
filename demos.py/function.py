sehir = "Ankara"
print(sehir.upper())
print(sehir.endswith("e"))

def selamVer(isim, soyIsim = "arkadaş"):
    print("Merhaba " + isim + " " + soyIsim)
selamVer("Eren")

def selamVer2(isim = "ziyaretçi", soyIsim = "Beyfendi"):
    print("Merhaba " + isim + " " + soyIsim)
selamVer2("Eren")
selamVer2("Eren", "Mulkoglu")
selamVer2("Eren " + "Mulkoglu")

def dikUcgenAlaniHesapla(a,b):
    return a*b/2
print(dikUcgenAlaniHesapla(2,3))
alan = dikUcgenAlaniHesapla(2,3)
print(alan)

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlaniHesapla2(4,5))
x = dikUcgenAlaniHesapla2
print(x(4,5))