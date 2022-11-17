ogrenciler = ["Eren","Mehmet","Osman","Hüseyin"]

ogrenciler[0] = "Murat" #(Elemanı değiştirme)
print(ogrenciler)

ogrenciler.append("Ahmet") #Listeye yeni eleman ekler.
print(ogrenciler)

ogrenciler.remove("Osman") #Listeden eleman siler.
print(ogrenciler)

ogrenciler.sort() #Alfabetik sıralama yapar.
print(ogrenciler)

ogrenciler.reverse() #Tersine çevirir elemanları
print(ogrenciler)

ogrenciler.pop(1) #Listeden eleman ÇIKARTIR.
print(ogrenciler)

ogrenciler.insert(0,"Ayşe") #Yerleştirme, Listeye eleman yerleştir
print(ogrenciler)

ogrenciler.clear()
print(ogrenciler)

isimler = ["Ahmet","Mehmet","Osman"]
for isim in isimler:
     print(isim)
