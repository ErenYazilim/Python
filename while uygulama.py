#kullanıcı adı admin şifre 123456 girildiğinde başarılı giriş yazan bunun dışında herhangi biri yanlış veya ikisi yanlış olduğunda kullanıcı adı veya şifre hatalı yazan ve tekrar kullanıcı adı ve şifre isteyen python programını yazınız.
from time import sleep
while True:
    ad=input("Kullanıcı adı: ").lower()
    sifre=input ("Şifre: ")
    if ad=="admin" and sifre=="123456":
        print("    ")
        print("Başarılı ")
        print("    ")
        print("Sisteme giriliyor")
        print("    ")
        print(".......")
        print("    ")
        input("İlerlemek için 'ENTER' tuşuna basın.  ")
        print("    ")
        print("....")
        print("....")
        print("    ")
        sleep(2)
        print("Lütfen bekleyiniz.")
        sleep(3)
        print("    ")
        print("Hoşgeldin Admin ")
        print("    ")
        break
    else:
        print("Kullanıcı adı veya şifre yanlış tekrar dene ")
        print("     ")
        print("İpucu: ")
        print("Yönetici")
        print("     ")
