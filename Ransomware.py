from cryptography.fernet import Fernet
def keyUret():
    key=Fernet.generate_key()
    with open("key.txt","wb") as file:
        file.write(key)

#keyUret()

def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read()
key=dosyaAc("key.txt")

icerik=dosyaAc("metin1.txt")
print(icerik)
print(key)