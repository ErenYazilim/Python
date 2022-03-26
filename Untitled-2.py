import os
os.listdir()#klasörün içindekileri list tipinde verir.
for i in os.listdir("C:/Users/ogr9/Desktop"):#listenin elemanlarına tek tek ulaşmak için
   #if ".txt" in i: 
        #print(i)
    if i.endswith(".txt"):#kelimenin son bitiş harfleri .txt ise true döndürür
        print(i)
    #if i.startswith("Dosyanın başında istenilen kelime"): kelimenin başı istelinen kelime ise true döndürür