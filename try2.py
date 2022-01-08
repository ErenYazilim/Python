while True:
    try:
        bir=int(input("1. Sayı "))
        print(" ")
        iki=int(input("2. Sayı "))
        print(bir/iki)
        print(" ")

    except ValueError:
        print("Lütfen sayı giriniz harf değil.")
        print(" ")

    except ZeroDivisionError:
        print("Bir sayı 0 a bölünemez.")
        print(" ")
