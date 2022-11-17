sozluk = {
    "book" : "kitap",
    "table" : "masa"
}

print(sozluk)
print(sozluk["book"]) #Çıktı: kitap
sozluk["pencil"] = "kalem"  #yeni eleman ekler
print(sozluk)
del(sozluk["book"])  #Eleman siler
print(sozluk)
print(len(sozluk))