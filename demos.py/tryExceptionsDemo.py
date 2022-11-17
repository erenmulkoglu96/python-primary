import sys

list = [7, 'Eren', 3, 0, 'Osman']

for x in list:
    try:
        print("Sayı = " + str(x))
        sonuc = 1/int(x)
        print("Sonuç = " + str(sonuc))
    except ValueError:
        print("Sistem uyarısı: " + str(sys.exc_info()[0]))
        print(str(x) + " bir sayı değil." )
    except ZeroDivisionError:
        print("Sistem uyarısı: " + str(sys.exc_info()[0]))
        print(str(x) + " için sıfıra bölme hatası")
    finally:
        print("İşlem bitti.")
        print("\n")
#%%
try:
    dosya = open("yazilim.txt","r")
except IOError:
    print("Dosya bulunamadı.")
finally:
    dosya.close()