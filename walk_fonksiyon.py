#listdir() ile sadece bir klasörün içini görebiliyorum klasörün içindeki klasörleride görebilmek için os.walk fonksiyonu kullanılır. 
import os
for i in os.walk("C:/Users/ogr9/Desktop/Elma"): 
    print(i)