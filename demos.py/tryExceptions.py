try:
    sayi = int(input("Bir sayı giriniz: "))
except ValueError:
    print("Tip uyuşmazlığı; lütfen sayı giriniz.")
except ZeroDivisionError:
    print("Payda sıfır olamaz.")
except:
    print("Bir hata oluştu.")
print("Bitti.")