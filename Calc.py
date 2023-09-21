print("Merhaba basit hesap makinesine hoşgeldiniz.")

sayi1 = float(input("Lütfen hesaplamada kullanılacak ilk sayıyı giriniz."))
sayi2 = float(input("Lütfen hesaplamada kullanılacak ikinci sayıyı giriniz."))

islemSec = """
(1) Toplama İşlemi
(2) Çıkarma İşlemi
(3) Çarpma İşlemi
(4) Bölme İşlemi
"""

print(islemSec)
soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

if soru == "1":
   print(sayi1, "+", sayi2, "=", sayi1 + sayi2)

elif soru == "2":
   print(sayi1, "-", sayi2, "=", sayi1 - sayi2)

elif soru == "3":
   print(sayi1, "x", sayi2, "=", sayi1 * sayi2)

elif soru == "4":
   print(sayi1, "/", sayi2, "=", sayi1 / sayi2)

else:
   print("Yanlış giriş.")
   print("Aşağıdaki seçeneklerden birini giriniz:", islemSec)