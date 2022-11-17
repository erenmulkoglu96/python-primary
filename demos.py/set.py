studentsSet = {"Eren", "Hüseyin","Osman"} #Çıktı karışık (indexsiz)
print(studentsSet)

studentsSet.remove("Hüseyin") #Eleman siler
print(studentsSet)

studentsSet.add("Ali") #Yeni Eleman ekler
print(studentsSet)

for student in studentsSet:
    print(student)
print("Osman" in studentsSet)

if "Osman" in studentsSet:
     print("Listede var")