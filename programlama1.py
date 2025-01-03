


#Verilen bir sayının karesini hesaplayan algoritmayı yazınız.

def kare_hesaplama(sayi):
    kare = sayi ** 2
    return kare



#Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız.

def isaret_bulma(sayi):
    if sayi < 0:
        return "Sayı Negatiftir."
    elif sayi == 0:
        return "Sayı 0'dır"
    else:
        return "Sayı Pozitiftir."
    


#Girilen sayının 6'nın katı olup olmadığını bulan algoritma?

def altinin_kati(sayi):
    if sayi % 6 == 0:
        return "Sayı altının katıdır."
    else:
        return "Sayı altının katı değildir."
    



#Vize ve final notuna göre geçme durumunu hesaplayan algoritma(Not=Vize*0,4+Final*0,6) Geçme Notu:55

def gecme_notu(vize,final):
    if vize * (2/5) + final * (3/5) >= 55:
        return "Tebrikler geçtiniz."
    else:
        return "Maalesef kaldınız."
    

    
#Klavyeden girilen sıralı 3 tam sayı ile dik üçgen çizilip çizilemeyeceğini gösteren program kodunu yazınız.

def ucgen(a,b,c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        return "Üçgen çizilebilir."
    else:
        return "Üçgen çizilemez."



#Klavyeden girilen a ve b sayılarına göre a^b hesaplayınız

def us_bulma(a,b):
    return a**b



#Parametre olarak gönderilen iki sayı arasında kalan sayıların toplamını döndüren fonksiyonu yazınız.

def sayilar_toplami(a,b):
    toplam = 0
    for i in range(a,b+1):
        toplam = toplam + i
    return toplam



#Verilen sayının mutlak değerini döndüren fonksiyonu yazınız

def mutlak_deger(sayi):
    if sayi < 0:
        mutlak = sayi * (-1)
    elif sayi == 0:
        mutlak = "Sayı 0 olduğundan mutlak değeri yoktur."
    elif sayi > 0:
        mutlak = sayi
    return mutlak



#Yarıçap değerini parametre olarak alıp dairenin alanını ve çevresini hesaplayan AlanHesapla ve CevreHesapla fonksiyonlarını tek programda yazıp çağırınız, pi sayısı 3 alarak

def AlanHesapla(r):
    alan = 3 * r**2
    return alan

def CevreHesapla(r):
    cevre = 2 * 3 * r
    return cevre

def hesapla():
    yaricap = float(input("Bir yarıçap değeri giriniz:"))

    alan = AlanHesapla(yaricap)
    cevre = CevreHesapla(yaricap)

    return alan, cevre



#Fiyat ve kdv oranını parametre olarak alıp toplam fiyatı ekrana yazdıran fonksiyonu yazınız.

def toplam_fiyat(fiyat, kdv):
    toplam = fiyat + ((fiyat / 100) * kdv)
    return toplam



#Parametre olarak verilen taban ve üs değerlerine göre Üs Alma işlemi gerçekleştiren ve sonucu döndüren fonksiyonu yazınız.

def us_alma(taban,us):
    sonuc = taban ** us
    return sonuc



#Kendisine parametre olarak verilen bir tam sayının Asal olup olmadığını kontrol edip Asal ise 1, değilse 0 değerini döndüren fonksiyon
 
def asal_mi(sayi):
    if sayi < 2:
        return 0 
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return 0
    return 1



#1-N arası asal sayıları listeleyen programı önceki sorudaki Asal fonksiyonu kullanarak yazınız.

def asal_aralik(N):
    liste = []
    for i in range(2, int(N**0.5) + 1):
           liste.append(i)
    return liste 



#Bir tam sayının kaç basamaklı olduğunu döndüren fonksiyonu yazınız.

def basamak_sayisi(sayi):
    if sayi < 0:
        sayi = sayi * (-1)
        return len(str(sayi))
    if sayi == 0:
        return 1
    return len(str(sayi))



#Verilen sayının faktöriyelini döndüren fonksiyonu yazınız.

def faktoriyel(sayi):
    if sayi < 0:
        return("Sayının faktöriyeli bulunmamaktadır.")
    elif sayi == 0 or sayi == 1:
        return("Sayının faktöriyeli 1'dir.")
    else:
        toplam = 1
        for i in range(sayi,1,-1):
            toplam = toplam * i
        return toplam
    


# Aşağıdaki çıktıyı veren programı yazınız?

def faktoriyel_sekil(sayi):
    cikti="0! = 1\n"
    carpim=1
    for i in range(1,sayi+1):
        carpim*=i
        cikti+=str(i)+"! = "+str(carpim)+"\n"

    return cikti



#Dört işlem: Kullanıcıdan 2 sayı alarak işlem seçtiren ve kullanıcı çıkış yapana kadar bu işlemi devam ettiren algoritma(1.Toplama,2.Çıkarma, 3.Çarpma, 4.Bölme, 0.Çıkış)

def hesap_makinesi(sayi,sayi2):
    islem = int(input("Lütfen yapacağınız işlemi tuşlayınız, 1.Toplama,2.Çıkarma, 3.Çarpma, 4.Bölme, 0.Çıkış.."))
    if islem == 0:
        return "Çıkış yapılıyor..."
    elif islem == 1:
        return sayi + sayi2
    elif islem == 2:
        return sayi - sayi2
    elif islem == 3:
        return sayi * sayi2
    else:
        return sayi / sayi2



# Kısa ve uzun kenarı girilen dikdörtgenin alanını ve çevresini hesaplayan programı Python dilinde kodlayınız.

def alan_cevre(kk,uk):
    alan = kk * uk
    cevre = 2 * (uk+kk)
    return "Alan:", alan, "Çevre:", cevre



#Yarıçapı verilen çemberin alanını hesaplayan programı Python dilinde kodlayınız. (pi = 3,14)

def cember_alani(r):
    alan = 3,14 * r**2
    return alan



#Girilen gün sayısını kaç yıl ve kaç ay olduğunu bulan programı kodlayınız.

def yil_ay_hesaplama(gun):
    ay = gun / 30
    yil = gun / 365
    return ay, "Ay", ",", yil, "Yıl"



#100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme çeviriniz.

def beslik_sistem(Not):
    beslik = Not / 20
    return beslik



#Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran programın kodunuz yazınız.

def basamak_degeri2(sayi):
    sayi = str(sayi)
    yuzler = int(sayi[0]) * 100
    onlar = int(sayi[1]) * 10
    birler = int(sayi[2]) * 1
    return yuzler, onlar, birler



#Kullanıcının girdiği bir sayının hem 2'ye hemde 3'e bölünebilme durumunu kontrol eden programı kodlayınız.

def bolunebilme_durumu(sayi):
    if sayi % 2 == 0 and sayi % 3 == 0:
        return "Sayı bölünebilir."
    else:
        return "Sayı bölünemez."
    


#Bir kredi kartından 2000 TL üzeri alış veriş yapıldığında 100 TL hediye puan, 1000 TL ve üzeri alış veriş yapıldığında 50 TL
#hediye puan, 1000 TL’nin altında alış veriş yapıldığında 10 TL hediye puan kazanılmaktadır. Klavyeden girilen harcama tutarına
#göre hediye puanı yazan problemin Python kodlarını yazınız

def hediye_puan(harcama):
    if harcama >= 2000:
        return "Tebrikler 100 TL hediye puan kazandınız."
    elif 2000 > harcama >= 1000:
        return "Tebrikler 50 TL hediye puan kazandınız."
    else:
        return "Tebrikler 10 TL hediye puan kazandınız."
    


#Bir internet satış sitesi alışveriş tutarı 50 TL’nin üzerindeki her kargoyu bedava veriyor. 50 TL altı sipariş tutarına ise 7 TL ilave
#edilerek, ekrana kargo ücretini ve toplam tutarı yazdırıyor. Bu programın Python kodunu oluşturunuz.

def kargo_ucreti(tutar):
    if tutar >= 50:
        return "Kargonuz bedava!"
    else:
        return "Kargo ücretiniz 7 TL, Toplam tutar:" , tutar + 7
    


#Kullanıcının girdiği üç sayı arasındaki en küçük çift sayıyı bulun veya eğer hiç çift sayı yoksa bir mesaj yazdırın.

def ciftsayi_bul(sayi1,sayi2,sayi3):
    sayilar = [sayi1,sayi2,sayi3]
    cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
    if len(cift_sayilar) == 0:
        return "Çift sayı bulunmamaktadır."
    return min(cift_sayilar)



#Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program?

def nk_hesaplama(n,k):
    toplam = 0
    for i in range(1,n+1):
        toplam = toplam + i*k
    return toplam
    


# Girilen sayının kaç faktöriyel olduğunu bulunuz (720=6!)

def kac_faktoriyel(sayi):
    carpim=1
    degisken=1
    
    if sayi==1:
        return "sayı 0! ya da 1!"

    while carpim<sayi:
        carpim*=degisken
        if carpim==sayi:
            return degisken
        degisken+=1



#Girilen tamsayının sıfır, pozitif ya da negatif olup olmadığını bulan program?

def isaret_bulma(sayi):
    if sayi < 0:
        return "Sayı negatiftir."
    elif sayi == 0:
        return "Sayı 0'dır."
    else:
        return "Sayı pozitiftir."
    


#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?

def en_buyuk_sayi(sayi1,sayi2,sayi3):
    sayilar = [sayi1,sayi2,sayi3]
    return max(sayilar)



#İşçi maaşı ve çocuk sayısına göre eğer çocuk sayısı bir ise %5, iki ise %10, üç veya daha fazla ise %15 zamlı maaşı hesaplayınız?

def maas_cocuk(maas,cocuk):
    if cocuk == 1:
        maas = maas + (maas * 1/20)
        return maas
    elif cocuk == 2:
        maas = maas + (maas * 1/10)
        return maas
    else:
        maas = maas + (maas * 3/20)
        return maas
    


#Kullanıcıdan 2 sayı alarak işlem seçtiren ve kullanıcı çıkış yapana kadar bu işlemi devam ettiren algoritma(1.Toplama,2.Çıkarma, 3.Çarpma, 4.Bölme, 0.Çıkış)

def islem_sec(sayi,sayi2):
    while True:
        islem = int(input("Bir işlem seçiniz.. (1.Toplama,2.Çıkarma, 3.Çarpma, 4.Bölme, 0.Çıkış)"))
        if islem == 0:
            print("Çıkış yapılıyor..")
            break
        elif islem == 1:
            print(sayi+sayi2)
        elif islem == 2:
            print(sayi-sayi2)
        elif islem == 3: 
            print(sayi*sayi2)
        elif islem == 4:
            print(sayi/sayi2)
        


#Klavyeden 3 adet kenar uzunluğu giriliyor. Girilen kenar uzunlukları göz önüne alındığında üçgenin çizilip çizilemeyeceğini,
#çizilebilir ise türünü (ikizkenar, çeşitkenar, eşkenar), alanını ve çevresini hesaplayan program?

def ucgen_cizme(kenar,kenar2,kenar3):
    if kenar**2 == kenar2**2 + kenar3**2 or kenar2**2 == kenar**2 + kenar3**2 or kenar3**2 == kenar**2 + kenar2**2:
        if kenar == kenar2 == kenar3:
            print("Üçgen türü eşkenar üçgendir. ")
        elif kenar == kenar2 or kenar == kenar3 or kenar2 == kenar3:
            print("Üçgen türü ikizkenar üçgendir.")
        else:
            print("Üçgen türü çeşitkenar üçgendir.")
    else:
        print("Üçgen çizilemez.")



#Sayıları tersten yani geriye yazdıran program?

def geri_yazma(baslangic,bitis):
    Liste = []
    for i in range(bitis, baslangic-1,-1):
        Liste.append(i)
    return Liste



#Kullanıcıdan isim ve soyisim bilgisini alan ve bunların harf uzunluğunu bulan programı yazınız.
        
def isim_uzunlugu(isim,soyisim):
    print("İsim uzunluğu:", len(isim), "Soyisim uzunluğu:", len(soyisim))



#Verilen 3 basamaklı sayıyı tersten yazdıran programı yazınız.

def tersten_yazdir(sayi):
    sayi = str(sayi)  
    ters_sayi = sayi[::-1] 
    


#Girilen 2 basamaklı bir sayının basamaklarında bulunan sayıları büyükten küçüğe sıralayınız.

def kucuk_buyuk(sayi):
    sayi = str(sayi)

    onlar = sayi//10
    birler = sayi%10

    if onlar>birler:
        print(onlar,birler)
    else:
        print(birler,onlar)



#Girilen 3 basamaklı sayının rakamlarının basamaklarını ekrana yazdırın.

def basamak_yazdir(sayi):

    sayi = str(sayi)
    yuzler = int(sayi[0]) * 100
    onlar = int(sayi[1]) * 10
    birler = int(sayi[2]) * 1

    print("Yüzler basamağı:", yuzler, "Onlar basamağı", onlar, "Birler basamağı", birler)



#2 basamaklı sayının her basamağının faktoriyelini hesaplayan program?

def basamak_faktoriyel(sayi):
    
    onlar = sayi//10
    birler = sayi%10
    toplam = 1
    toplam2 = 1
    for i in range(onlar,1,-1):
        toplam = toplam * i
    for i in range(birler,1,-1):
        toplam2 = toplam2 * i
    print(toplam, toplam2)



#Kullanıcıdan alınacak pozitif tamsayılardan oluşturulacak “N” elemanlı bir dizide, yine kullanıcının
#belirlediği bir “k” indeks numarasına göre dizinin “k”.indeksinden büyük olan konumdaki değerleri dizinin
#sonundan başlayarak her adımda “0” olarak değiştiren bir özyinelemeli(recursive) fonksiyon yazılacaktır. Ayrıca
#her değiştirme adımında dizinin tüm elemanlarını yazdırılacaktır.

N = int(input("Bir N sayısı giriniz:"))
k = int(input("Bir K indeksi giriniz:"))

dizi = []

for i in range(N+1):
    sayi = int(input("Bir sayı giriniz:"))
    dizi.append(sayi)



#Klavyeden girilen 2 sayıdan büyük olan sayı küçük sayıya bölünerek bölüm ve kalan sonucu
#yazdırılacaktır. Bu işlem için yazılacak “Bolme()” fonksiyonu bölme işlemini yapıp bölüm ve kalanı bulacaktır. Sayı
#girişi ve sonuçları yazdırma işlemleri “main()” fonksiyonunda yapılacaktır.(Global değişken kullanılmayacaktır.)

def bolme(sayi1,sayi2):
    if sayi1 > sayi2:
        kucuk = sayi2
        buyuk = sayi1
    else:
        kucuk = sayi1
        buyuk = sayi2

    bolum = buyuk // kucuk
    kalan = buyuk % kucuk

    return bolum, kalan

def main():
    
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    bolum, kalan = bolme(sayi1, sayi2)
    
    print("Bölüm:", bolum)
    print("Kalan:", kalan)



#Kullanıcıdan N değeri alındıktan sonra N adet sayı girişi alınarak bu sayılar bellekte tutulacaktır. Tüm
#sayılar alındıktan sonra bu sayılardan en büyük ve en küçük sayı ile girilen sayıların ortalaması bulunacaktır.

def main2():
    liste = []
    N = int(input("Bir N sayısı giriniz:"))
    for i in range(N):
        sayi = int(input("Bir sayı giriniz:"))
        liste.append(sayi)
    en_buyuk = max(liste)
    en_kucuk = min(liste)
    ortalama = sum(liste) / N

    print("En büyük sayı:", en_buyuk)
    print("En küçük sayı:", en_kucuk)
    print("Ortalama:", ortalama)
    




#1'den 50'ye kadar tamsayıları yineleyen bir Python programı yazın.Üçün katları için sayı yerine “Big”,
#yedinin katları yerine “Bang” yazın.Hem üçün hem de yedinin katı olan sayılar için “BigBang” yazdırın.

def yazdir(sayi):
    liste = []
    for i in range(1,sayi+1):
        if i % 3 == 0 and i % 7 == 0:
            liste.append("BigBang")
        elif i % 3 == 0:
            liste.append("Big")
        elif i % 7 == 0:
            liste.append("Bang")
        else:
            liste.append(i)
    return liste



#Kullanıcıdan bir sayı alınız.ve bu sayının basamak değeri 3'ten küçükse bu sayının yerine karesini yazdırın.
#Eğer 3 ten büyük ve tek ise bu sayının 2 eksiğini yazdırın. Eğer 3 ten büyük ve çift sayı ise bu sayının 1 fazlasını ekrana yazdırın.
#Kullanıcıdan alınan girişin geçerli olup olmadığını da kontrol ediniz.

def sayi_isle():
    sayi = int(input("Bir sayı giriniz:"))
    if sayi < 0:
        print("Geçerli bir sayı girmediniz.")
    elif sayi < 3:
        print(sayi ** 2)
    elif 3 <= sayi and sayi % 2 == 1:
        print(sayi - 2)
    else:
        print(sayi + 1)



#Verilen sayının tam bölenleri bir listeye atanıp ve toplamlarının sonucunun tam bölenlerini bulup listeye eklediğimizde
#son listede bulunan tam bölenlerin toplamı ilk verilen sayıyı veriyorsa bu sayılara amicable numbers denir.
#Kullanıcının girdiği bir sayının amicable numbers sayı olup olmadığını kontrol ediniz.

def tambolen_toplam():
    sayi = int(input("Bir sayı giriniz:"))
    toplam = 0
    liste = []
    for i in range(1,sayi):
        if sayi % i == 0:
            toplam = toplam + i
            liste.append(toplam)
    if toplam == sayi:
        print("Sayı amicable sayıdır.")
    else:
        print("Sayı amicable sayı değildir.")
    


#Recursive fonksiyon ile faktöriyel çözümü yapınız.

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n-1)
    


#Recursive fonksiyon ile fibonacci serisi çözümü yapınız.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



#Recursive fonksiyon ile geri saydırma çözümünü yapınız.

def gerisayma(n):
    if n == 0:
        print("Geri sayım sonlandırılıyor")
    else:
        print(n, end=" ")
        gerisayma(n-1)
    


#Recursive fonksiykon ile tablo oluşturma çözümünü yapınız.

def tablo_olustur():
    olcu = int(input("Bir tablo ölçüsü giriniz:"))
    for satir in range(1, olcu+1):
        for sutun in range(1,olcu+1):
            tablo = satir * sutun
            print(tablo, end=" ")
        print()



##matrisin satır ve sütun toplamlarını hesaplayan programı yazınız

import random
def matrisiekranayaz(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print()
satir = 3
sutun = 5
A = [[int(10*random.random())for i in range(sutun)]for j in range(satir)]
#matrisiekranayaz(A,'A')

satirtop = []
for i in range(satir):
    top = 0
    for j in range(sutun):
        top = top + A[i][j]
#print("Satır toplamları:",top)

sutuntop = []
for j in range(sutun):
    top = 0
    for i in range(satir):
        top = top + A[i][j]
#print("Sütun toplamları:",top)



##0 matris oluşturma

def sifirmatris(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print()
satir = 4
sutun = 4

S = [[0 for i in range(sutun)]for j in range(satir)]

#sifirmatris(S,'S')



#Verilen matrislerin toplamını hesaplayan program

import random
def matrisiekranayaz(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print()
satir = 3
sutun = 5
A = [[int(10*random.random())for i in range(sutun)]for j in range(satir)]
#matrisiekranayaz(A,'A')
  
B = [[int(10*random.random())for i in range(sutun)]for j in range(satir)]
#matrisiekranayaz(B,'B')

C = [[0 for i in range(sutun)]for j in range(satir)]
for i in range(satir):
    for j in range(sutun):
        C[i][j]= A[i][j] + B[i][j]
#matrisiekranayaz(C,'C')
