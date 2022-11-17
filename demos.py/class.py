#%%
class Matematik:
    def topla(self, sayi1, sayi2):
        return sayi1 + sayi2

    def cikar(self, sayi1, sayi2):
        return sayi1 - sayi2
    
    def bol(self, sayi1, sayi2):
        return sayi1 / sayi2

    def carp(self, sayi1, sayi2):
        return sayi1 * sayi2

matematik = Matematik()
a = int(input("Sayı giriniz: "))
b = int(input("Sayı giriniz: "))
print("Toplam =", matematik.topla(a, b))
print("Çarpım =", matematik.carp(a, b))
print("Bölüm =", matematik.bol(a, b))
print("Çıkarma =", matematik.cikar(a, b))
#%%
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

a = int(input("Sayı giriniz: "))
b = int(input("Sayı giriniz: "))
matematik1 = Matematik(a, b)
matematik2 = Matematik(a, b)
matematik3 = Matematik(a, b)
matematik4 = Matematik(a, b)
print("Toplam =", matematik1.topla())
print("Çarpım =", matematik2.carp())
print("Bölüm =", matematik3.bol())
print("Çıkarma =", matematik4.cikar())
#%%
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Eren", "Mulkoglu", "26")
print("Ad Soyad: " + person1.firstName, person1.lastName + "\n" + "Yaş: " + person1.age)

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary

class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

Zeynep = Worker()
Ayse = Customer()
# %%