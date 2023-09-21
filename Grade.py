vize = float(input("Vize notunuzu giriniz."))
final = float(input("Final notunuzu giriniz."))
ortalama = vize*0.4 + final*0.6

if final < 40:
    print("Final notunuz 40'dan küçük olduğu için, kaldınız.", "Final notunuz:", final)
elif vize == 2 * final :
    print("Vize notunuz final notunuzun iki katı olduğundan kaldınız", "Vize notunuz:", vize, "Final notunuz:", final)
else:
    if ortalama <= 49:
        print("Harf notunuz FF'dir, ortalamanız 50'den düşük olduğundan kaldınız.", "Ortalamanız:", ortalama)
    elif ortalama <= 59:
        print("Harf notunuz DD'dir, şartlı geçtiniz.", "Ortalamanız:", ortalama)
    elif ortalama <= 69:
        print("Harf notunuz CC'dir, tebrikler! Geçtiniz.", "Ortalamanız:", ortalama)
    elif ortalama <= 79:
        print("Harf notunuz BB'dir, tebrikler! Geçtiniz.", "Ortalamanız:", ortalama)
    elif ortalama <= 100:
        print("Harf notunuz AA'dır, tebrikler! Geçtiniz.", "Ortalamanız:", ortalama)
    else:
        print("Ortalama 100'den büyük olarak hesaplandı, tekrar deneyiniz.")




