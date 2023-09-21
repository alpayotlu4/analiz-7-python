while True:

    vize = float(input("Vize notunuzu giriniz."))
    final = float(input("Final notunuzu giriniz."))
    ortalama = vize*0.4 + final*0.6


    if ortalama <= 49:
        print("Harf notunuz FF'dir, kaldınız.", "Ortalamanız:", ortalama)
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




