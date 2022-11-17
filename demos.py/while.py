defKullanici = "eren"
defParola = "157"
while (True):
    kullanici = input("Kullanıcı adı: ")
    parola = input("Parola: ")
    if kullanici == defKullanici and parola == defParola:
        print("Hoşgeldiniz.")
        break
    elif kullanici != defKullanici and parola == defParola:
        print("Kullanıcı adı yanlış.")
    elif kullanici == defKullanici and parola != defParola:
        print("Şifre yanlış. Şifrenizi mi unuttunuz? (E/H)")
        cevap = input()
        if cevap == "E":
            defParola = input("Yeni şifre belirleyiniz: ")
            print("Şifre kaydedildi.")
    else:
        print("Tekrar deneyin.")