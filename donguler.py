# # Döngüler

# # bir liste veye string bir ifade üzerinde çalışır , integer ifadelerde işe yaramaz.
# # bir işlemi birden fazla defa yapmak istersek kullanabiliriz.

# liste = [1,2,3,4,5,6]

# print(liste[0])                 # / 1
# print(liste[1])                 # / 2
# print(liste[2])                 # / 3
# print(liste[3])                 # / 4
# print(liste[4])                 # / 5
# print(liste[5])                 # / 6


# # for döngü yapısı : 


# liste = [1,2,3,4,5,6]

# for degisken in liste:
#     print(degisken)             # / 1,2,3,4,5,6 

# isim = "Ahmet"

# for harf in isim:
#     print(harf)                 # / A h m e t

# sayi = 123456

# # for rakam in sayi:
# #     print(rakam)                # / TypeError: 'int' object is not iterable hatası


# # range fonksiyonu kullanımı :
#     # range fonksiyonunda alt sınır dahildir , üst sınır dahil değildir.
#     # parantez içindeki 3.index adımları gösterir.
#     # parantez içinde sadece tek bir index varsa üst sınırı belli eder.


# for i in range(1,5):
#     print(i)                        # / 1,2,3,4 

# for x in range(1,7,2):
#     print(x)                        # / 1,3,5 


# # örnek uygulama: 

# sonuc = 1
# for i in range(10):
#     sonuc *= 2
#     print(sonuc)                    # her adımı bastırdık / 2 4 8 16 32 64 128 256 512 1024

# sonuc = 1
# for i in range(10):
#     sonuc *= 2
# print(sonuc)                        # dongu bitince sonucu bastırdık / 1024


# # iç içe for döngüsü kullanımı

# liste1 = ["a","b","c"]
# liste2=[1,2,3]

# for harf in liste1:
#     for rakam in liste2:
#         print(harf,rakam)           # / a 1 , a 2 , a 3 , b 1 , b 2 , b 3 , c 1 , c 2 , c 3 ,  


# # break ve continue kullanımı : 

# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)                        # / 1 2 3 4 5

# liste = [1,2,3,4,5]
# for i in liste:
#     if i == 3:
#         continue
#     print(i)                        # / 1 2 4 5 

# liste = [1,2,3,4,5]
# for i in liste:
#     if i ==4:
#         break
#     print(i)                        # / 1 2 3 

# # örnek

# liste = range(20)                   # 0 dan 19a kadar bir range tanımladık.

# for i in liste:                     # i değişkeni ile döngü kurduk
#     if i%3 != 0:                    # eğer i 3e bölünmüyorsa devam et dedik
#         continue
#     if i == 15:                     # eğer i = 15 olursa yazdırmadan döngüden çık dedik.
#         break
#     print(i)                        # 3 6 9 12 

# While döngüsü 

# tanım : belirli bir koşul sağlandığı sürece çalışan döngüdür.

x = 2
while x <7:
    print(x)
    x +=1                           # 2 3 4 5 6 


#100 e kadar olan tek sayıları ekrana yazdırma

i = 1
while True:
    if i%2 ==0:
        i+=1
        continue
    print(i)
    i+=1
    if i == 100:
        break