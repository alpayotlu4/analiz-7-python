from ogrenci import Ogrenci
from ogretmen import Ogretmen

ogrlist = []
tcrlist = []


def ogrenciEkle(name, surname, number) -> Ogrenci:
    return Ogrenci(name, surname, number)


def ogretmenEkle(name, surname, number) -> Ogretmen:
    return Ogretmen(name, surname, number)


def ogrenciListele(ogrList):
    for i in ogrList:
        print(
            f"Öğrencinin adı {i.name} Öğrencinin Soyadı {i.surname} Öğrencinin numarası {i.studentId}"
        )


def ogretmenListele(tcrList):
    for i in tcrList:
        print(
            f"Öğretmenin adı {i.name} Öğretmenin Soyadı {i.surname} Öğretmenin numarası {i.teacherId}"
        )


while True:
    inp = input(
        "*Öğrenci eklemek için 1 \n*Öğretmen eklemek için 2 \n*Öğrencileri listelemek için 3 \n*Öğretmenleri listelemek için 4 \n*Çıkmak için 'q' giriniz.\n"
    )
    if inp == "q":
        break

    elif inp == "1":
        isim = input("Öğrencinin ismi: ")
        soyisim = input("Öğrencinin soyismi: ")
        numara = int(input("Öğrencinin numarası: "))
        ogrlist.append(ogrenciEkle(isim, soyisim, numara))
    elif inp == "2":
        isim = input("Öğretmenin ismi: ")
        soyisim = input("Öğretmenin soyismi: ")
        numara = int(input("Öğretmenin numarası: "))
        tcrlist.append(ogretmenEkle(isim, soyisim, numara))
    elif inp == "3":
        ogrenciListele(ogrlist)
    elif inp == "4":
        ogretmenListele(tcrlist)
    else:
        print("Lütfen geçerli bir karakter giriniz.")
