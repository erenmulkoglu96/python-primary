# JSON verilerini çözen iki fonksiyon
# json formatındaki stringi, json'a çevireceğiz. 

import json

data = '{"firstName":"Eren","lastName":"Osman"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

# # Python sözlüğünü json'a çeviriyoruz.
# #  JSON oluşturan fonksiyonlar

customer = {
         "firstName":"Eren",
         "email":"eren06@gmail.com"
}

customerJson = json.dumps(customer)
print(customer)
print(json.dumps("Osman"))