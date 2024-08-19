#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def tas_kagit_makas_ENES_SERAN():
    
    liste_secenekler = ["taş", "kağıt", "makas"]
    
    print(" Taş, Kağıt, Makas Oyununa Hoşgeldin! Bakalım bana karşı kazanabilecek misin!!!\n Oyuna başlamadan önce kuralları hatırlatmak istiyorum. Oyunda Taş, Kağıt ve Makas olarak seçimler yapacağız. Bu seçimlerde:\n - Makas Kağıdı Keser\n - Kağıt Taşı Sarar\n - Taş Makası Kırar\n Aynı seçimler gelirse berabere kalır. Toplam 3 tur oynayacağız ve 2 olan kazanacak.")
    
    oyun_sayisi = 0
    oyuncu_toplam_win = 0
    bilgisayar_toplam_win = 0

    while True:
        oynanan_tur_sayisi = 0
        oyuncu_tur_win = 0
        bilgisayar_tur_win = 0

        while oynanan_tur_sayisi < 3:
            
            oyuncu_secimi = input("Seçimini yap (taş, kağıt, makas): ")
            
            bilgisayar_secimi = random.choice(liste_secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}\n")

            if oyuncu_secimi not in liste_secenekler:
                print("Geçersiz seçim yaptın. Lütfen tekrar seçim yap.\n")
                continue

            if (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Sen Kazandın!\n")
                oyuncu_tur_win += 1
           
            elif oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!\n")
            
            else:
                print("Kaybettin!\n")
                bilgisayar_tur_win += 1

            oynanan_tur_sayisi += 1

        if oyuncu_tur_win >= 2:
            oyuncu_toplam_win += 1
        
        elif bilgisayar_tur_win >= 2:
            bilgisayar_toplam_win += 1

        oyun_sayisi += 1
        print(f"Oynanan Oyun Sayısı: {oyun_sayisi}")
        print(f"Oyuncu Galibiyet Sayısı: {oyuncu_toplam_win}")
        print(f"Bilgisayar Galibiyet Sayısı: {bilgisayar_toplam_win}\n")

        devam = input("Tekrar oynamak ister misin? (evet/hayır): ")
        if devam != "evet":
            print("Hoşçakal!")
            break

tas_kagit_makas_ENES_SERAN()

                

