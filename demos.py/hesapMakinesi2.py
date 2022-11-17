print("Operasyon")
print("1: Topla")
print("2: Çıkar")
print("3: Çarp")
print("4: Böl")

sec = int(input("Operasyonu seç:"))

sayi1 = int(input("Birinci sayi:"))
sayi2 = int(input("İkinci sayi:"))

#Toplama
def topla(sayi1,sayi2):
   return sayi1 + sayi2

#Çıkar
def cıkar(sayi1,sayi2):
    return sayi1 - sayi2

#Çarpma
def carp(sayi1,sayi2):
    return sayi1 * sayi2

#Bölme
def bol(sayi1,sayi2):
    return sayi1 / sayi2


if sec == 1:
    print("Toplam : " + str(topla(sayi1,sayi2)))
elif sec == 2:
    print("Çıkarma " + str(cıkar(sayi1,sayi2)))
elif sec == 3:
    print("Çarpma: " + str(carp(sayi1,sayi2)))
elif sec == 4:
    print("Bölme: " +  str(bol(sayi1,sayi2)))
else:
    print("Geçersiz işlem")