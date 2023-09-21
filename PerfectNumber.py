while True:

    sayi = int(input("Sayı giriniz"))
    toplam = 0 
    for i in range (1,sayi):
        if sayi%i == 0:
            toplam += i
    if toplam == sayi:
        print(sayi, "mükemmel sayıdır.")
    else:
        print(sayi, "mükemmel sayı değildir.")

        


    