#Klavyeden E harfi girildiğinde ekrana erkek k harfi girildiğinde kız yazdıran programı yapınız
cvp=input("E mi K mi ?  ").upper()
if cvp=="E":
    print("Erkek")
elif cvp=="K":
    print("Kız")
else:
    print("Ben sana demedimmi E veya K yaz diye niye" cvp "yazıyosun.")
