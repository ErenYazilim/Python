def hesapla (a):
    print(a!(a-1))
while True:
    try:
        a=int(input("Bir Sayı Gir "))
        hesapla(a)
    except ValueError:
        print("Sayı girmen gerek.")
        continue