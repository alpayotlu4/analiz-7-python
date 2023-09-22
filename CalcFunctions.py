print("Merhaba basit hesap makinesine hoşgeldiniz.")

while True:

    islemSec = """
    (1) Toplama İşlemi
    (2) Çıkarma İşlemi
    (3) Çarpma İşlemi
    (4) Bölme İşlemi
    (5) Mod Operatörü
    (q) Çıkış
    """

    print(islemSec)
    soru = input("Lütfen yapmak istediğiniz işlemi seçiniz eğer çıkmak istiyorsanız Q tuşuna basınız: ")

    if soru == "q":
        break
    else:

        sayı1 = float(input("Lütfen hesaplamada kullanılacak ilk sayıyı giriniz."))
        sayı2 = float(input("Lütfen hesaplamada kullanılacak ikinci sayıyı giriniz."))

        def toplama():
            toplam = sayı1 + sayı2
            print("Sonuç:", toplam) 

        def çıkarma():
            sonuç = sayı1 - sayı2
            print("Sonuç:", sonuç)

        def çarpma():
            çarpım = sayı1 * sayı2
            print("Sonuç:", çarpım)

        def bölme():
            bölüm = sayı1 / sayı2
            print("Sonuç:", bölüm)

        def mod_operatörü():
            sonuc = sayı1 % sayı2
            print("Sonuç:", sonuc)

        if soru == "1":
            toplama()
        elif soru == "2":
            çıkarma()
        elif soru == "3":
            çarpma()
        elif soru == "4":
            bölme()
        elif soru == "5":
            mod_operatörü()
        else:
            print("Yanlış giriş.")




