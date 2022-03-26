import os
print(os.getcwd())#dosya yolunu verir
os.listdir()#klasörün içindekileri list tipinde verir.
for i in os.listdir("C:/Users/ogr9/Desktop"):#listenin eleöanlarına tek tek ulaşmak için
    print(i)