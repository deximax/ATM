print("********************\nDEX BANK sistemine hoşgeldiniz\n********************")

print("""

İŞLEMLER:

1.BAKİYE SORGULAMA
2.PARA YATIRMA
3.PARA ÇEKME
""")

bakiye=2000

while True:
    islem=input("Yapmak İstediğniz İşlemi Giriniz:")

    if islem == 'q' or islem == 'Q':
        print("Yine Bekleriz :)")
        break
    elif islem == "1":
        print("Bakiyeniz",bakiye,"TL")
    elif islem == "2":
        yatir=int(input("Yatırmak İstediğniz Miktar:"))
        bakiye=bakiye+yatir
        print("Bakiyenizin Son Miktarı:",bakiye,"TL")
    elif islem == "3":
        cek=int(input("Çekmek İstediğiniz Miktar:"))
        if bakiye - cek < 0:
            print("Bu Büyüklükte Bir Miktarı Çekemezsiniz !")
            print("Bakiyenizin Son Miktarı:",bakiye,"TL")
        else:
            bakiye=bakiye-cek
            print("Bakiyenizin Son Miktarı:",bakiye,"TL")

    else:
     print("Geçersiz İşlem")



