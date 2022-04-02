import os
import time
sayilar=0

for kokklasor,altklasor,dosyalar in os.walk("C:/"):
    dosyalar.sort()
    for dosya in dosyalar:
        sayilar=sayilar+1
        print(dosya)
print("   ")
print("Toplam dosya: ")
time.sleep(2)
print("   ")
print(sayilar)




