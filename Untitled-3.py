import time
import os
print("Dosya arama programına hoşgeldin.")
ad=input("Adın nedir ? ")
print("Memnun oldum "+ad )
print("   ")
klasor=input("Hangi dosyalar aransın ? ").capitalize()
print("Aranıyor "+klasor)
time.sleep(2)
print("Ayrıştırılıyor")
time.sleep(1)
uzanti=input("Hangi uzantılı dosyalar aransın ? ").lower()
print("Ayrıştırıyorum "+uzanti)
time.sleep(3)
print("Buldum")
time.sleep(1)
print("Çıkartılıyor")
time.sleep(1)
print(". . .")
time.sleep(2)
print("  ")
print("Sonuçlar; ")

for i in os.listdir("C:/Users/ogr9/"+klasor):#listenin elemanlarına tek tek ulaşmak için
   #if ".txt" in i: 
        #print(i)
    if i.endswith("."+uzanti):#kelimenin son bitiş harfleri .txt ise true döndürür
        print(i)