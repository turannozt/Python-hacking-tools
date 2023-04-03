import requests
import json
import time
import os

#api kısmı
url = ('https://www.virustotal.com/vtapi/v2/file/scan')
os.system("cls")
print("="*15+ "\n" + "Turan Antivirus" + "\n" + "="*15 )
print("Taratacağınız dosyayı programın olduğu klasöre sürükleyin")
fileqwe = input("Lütfen taratılacak dosyanın adını giriniz : ")
params = {'apikey': '623d6e735dab67a21436c1ee4aec561ba50007bf633e935d0261bf9af510d683'}

files = {'file': (fileqwe, open(fileqwe, 'rb'))}

response = requests.post(url, files=files, params=params)
data = json.loads(response.text)
linkkk = data['permalink']
print(data)
print("Virus taraması sonuçları 1,5 dakika içerisinde bu linkte olacaktır: " +linkkk)
time.sleep(5)
#api kısmı

#indiriliyor animasyon
a = 1
b = "="
c = ">"
dosya = "Dosya yükleniyor... "
while True:
    a += 1
    print(dosya+b*a+c)
    print("%",a)
    time.sleep(0.5)
    os.system("cls")
    if a == 100:
        os.system("ping" + linkkk)
        os.system("cls")
        break
#indiriliyor animasyonu
weblink = linkkk
os.system("cls")
print("Tarama Tamamlandı !" + "\n")
print("Sonuçlar Aşağıdaki Gibidir" + "\n")
print("Hangi antivirüs programları virüs algılaşmış detaylı bakmak için : " + linkkk)