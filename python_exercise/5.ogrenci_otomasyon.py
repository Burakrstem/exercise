#OOP ile kodla
#ogrenci kayıt yapabilmeli
#ogrencinin ad,soyad,sinif,yas,cinsiyet bilgisini tut
#istenen ogrenci silinebilmeli
#istenilen ogrenci bilgileri sorgulanabilir

class Ogrenci_otomasyon:
    def __init__(self):
        self.run=True
        dosya=open("dosya.txt","r+")
    def giris(self):
        print("\n[1].Ogrenci kayit\n[2].Kayit silme\n[3].Ogrenci bilgi\n[4].Cikis")
        secim=int(input("Lutfen yapmak istediginiz islemi seciniz==>"))    
        if secim<1 and secim>3:
            print("Hatali islem")
        elif secim==1:
            self.ogrenci_kayit()
        elif secim==2:
            self.ogrenci_sil()
        elif secim==3:
            self.ogrenci_bilgi()
        elif secim==4:
            print("Cikis yapiliyor")
            self.run=False
        else:
            print("Hatali secim")
	
    def ogrenci_kayit(self):
        ad=input("ad==>")
        soyad=input("soyad    ==>")
        sinif=input("sinif ORN:(7-A)==> ")
        yas=input("yas==>")
        cinsiyet=input("cinsiyet==>")
        with open("dosya.txt","r+") as dosya:
            sira=len(dosya.readlines())+1    
            dosya.write(str(sira) + ")ISIM==>" + ad +"\t"+ "SOYISIM==>" + soyad + "\t" + "SINIF==>" + sinif + "\t" + "YAS==>" + yas +"\t"+"CINSIYET " + cinsiyet +"\n")
            print(f"{ad} {soyad}:{sira} numarali kayit olusturuldu ")
    def ogrenci_sil(self):
        numara=int(input("\nSilinmesini istediginiz ogrencinin sira numarasini giriniz==>"))
        with open ("dosya.txt","r+") as dosya:
            liste=dosya.readlines()
            liste[numara-1]="\n"
            
        with open("dosya.txt","w") as dosya:
            for i in liste:
                dosya.write(i)
            

    def ogrenci_bilgi(self):
        sira=int(input("Bilgi almak istediginiz ogrencinin sira numarasini giriniz==>"))
        with open ("dosya.txt","r") as dosya:
            liste=dosya.readlines()
            print(liste[sira-1])
        for i in range(len(liste)):
            if liste[i][0:1]==sira:
                print(liste[i])
        if liste[sira-1][0:1]=='\n':
            print("ogrenci bulunamadi")
    
if __name__=='__main__':
    print("OGRENCI OTOMASYONUNA HOSGELDINIZ\n")
    ogrenci=Ogrenci_otomasyon()
    while ogrenci.run:
        ogrenci.giris()
