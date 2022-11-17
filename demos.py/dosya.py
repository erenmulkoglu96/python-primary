# r Read okuma
# a append yeni datalar, veriler ekleme
# w write yoksa yeni dosya oluşturup dosyanın üzerine yazma
# x create dosya oluşturma


#f = open("yazilim.txt","w") # oluşturur ve içindekileri siler.
#f.write("Php: Ramus Lerdorf\n")
#f.write("Python: Guido van Rossum\n")

#f = open("yazilim.txt","a") #dosya oluşturuyor ve yazıyor
#f.write("\n")
#f.write("Java: James Gosling\n")
#f.write("C: Dennis Ritchie")


# Dosya okuma parametresi
# f = open("yazilim.txt")
# print(f.read())

# Dosyayı satır satır okuma
#f = open("yazilim.txt")
#print(f.readline())

# f = open("yazilim.txt")
# for l in f:
#     print(l)

# Dosyayı siler.
#import os
#os.remove("yazilim.txt")

# import os

# if os.path.exists("yazilim.txt"):
#     os.remove("yazilim.txt")
# else:
#     print("Dosya yok")

#Klasör silme
#os.rmdir("empty")

# Örnek yapma 
#ogrenciler = ["Osman","Hüseyin","Mehmet","Eren"]

#fDosya = open("ogrenciler","a")

#for ogrenci in ogrenciler:
     #fDosya.write(ogrenci)
     #fDosya.write("\n")