import pandas as pd  #pandas kütüphane ve diğer proje dosyalarından class yapılarını ekleme
from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta

def main():
    try:
        # Personeller
        personel1 = Personel(personel_no=1, ad='Ahmet', soyad='Yılmaz', departman='Muhasebe', maas=5000)
        personel2 = Personel(personel_no=2, ad='Ayşe', soyad='Kara', departman='İK', maas=6000)
        
        # Doktorlar
        doktor1 = Doktor(personel_no=3, ad='Mehmet', soyad='Öztürk', departman='Cerrahi', maas=8000, uzmanlik='Cerrahi', deneyim_yili=10, hastane='Hastane A')
        doktor2 = Doktor(personel_no=4, ad='Fatma', soyad='Demir', departman='Pediatri', maas=7500, uzmanlik='Pediatri', deneyim_yili=3, hastane='Hastane B')
        doktor3 = Doktor(personel_no=5, ad='Ali', soyad='Vural', departman='Kardiyoloji', maas=9000, uzmanlik='Kardiyoloji', deneyim_yili=6, hastane='Hastane C')
        
        # Hemşireler
        hemsire1 = Hemsire(personel_no=6, ad='Selin', soyad='Çelik', departman='Acil', maas=4000, calisma_saati=40, sertifika='Sertifika A', hastane='Hastane A')
        hemsire2 = Hemsire(personel_no=7, ad='Burak', soyad='Güneş', departman='Yoğun Bakım', maas=4500, calisma_saati=35, sertifika='Sertifika B', hastane='Hastane B')
        hemsire3 = Hemsire(personel_no=8, ad='Emine', soyad='Yıldız', departman='Poliklinik', maas=4300, calisma_saati=30, sertifika='Sertifika C', hastane='Hastane C')
        
        # Hastalar
        hasta1 = Hasta(hasta_no=1, ad='Kemal', soyad='Arslan', dogum_tarihi='1985-05-15', hastalik='Grip', tedavi='İlaç Tedavisi')
        hasta2 = Hasta(hasta_no=2, ad='Zeynep', soyad='Kaya', dogum_tarihi='1992-08-25', hastalik='Alerji', tedavi='İlaç Tedavisi')
        hasta3 = Hasta(hasta_no=3, ad='Murat', soyad='Erdoğan', dogum_tarihi='2000-12-12', hastalik='Kırık', tedavi='Cerrahi Müdahale')
        
        # Tüm nesneleri bir listeye ekleme
        personeller = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3]
        hastalar = [hasta1, hasta2, hasta3]

        # Personel, doktor, hemşire ve hasta nesnelerinden veri çerçevesi oluşturma
        personel_data = [{
            'personel_no': p.get_personel_no(), 'ad': p.get_ad(), 'soyad': p.get_soyad(), 'departman': p.get_departman(),
            'maas': p.get_maas(), 'uzmanlik': getattr(p, 'get_uzmanlik', lambda: 0)(), 'deneyim_yili': getattr(p, 'get_deneyim_yili', lambda: 0)(),
            'hastane': getattr(p, 'get_hastane', lambda: 0)(), 'calisma_saati': getattr(p, 'get_calisma_saati', lambda: 0)(),
            'sertifika': getattr(p, 'get_sertifika', lambda: 0)()
        } for p in personeller]

        hasta_data = [{
            'hasta_no': h.get_hasta_no(), 'ad': h.get_ad(), 'soyad': h.get_soyad(), 'dogum_tarihi': h.get_dogum_tarihi(), 'hastalik': h.get_hastalik(), 'tedavi': h.get_tedavi()
        } for h in hastalar]

        df_personel = pd.DataFrame(personel_data)
        df_hasta = pd.DataFrame(hasta_data)

        # Boş olan değişken değerleri için 0 atama
        df_personel.fillna(0, inplace=True)
        df_hasta.fillna(0, inplace=True)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
        doktor_sayisi_uzmanlik = df_personel[df_personel['uzmanlik'] != 0].groupby('uzmanlik').size()
        print("Doktor sayısı (uzmanlık alanlarına göre):\n", doktor_sayisi_uzmanlik)

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
        deneyimli_doktor_sayisi = df_personel[(df_personel['deneyim_yili'] > 5) & (df_personel['uzmanlik'] != 0)].shape[0]
        print("5 yıldan fazla deneyime sahip doktor sayısı:", deneyimli_doktor_sayisi)

        # Hasta adına göre DataFrame’i alfabetik olarak sıralama ve yazdırma
        df_hasta_sorted = df_hasta.sort_values(by='ad')
        print("Alfabetik sırayla hastalar:\n", df_hasta_sorted)

        # Maaşı 7000 TL üzerinde olan personelleri bulma ve yazdırma
        maasi_yuksek_personeller = df_personel[df_personel['maas'] > 7000]
        print("Maaşı 7000 TL üzerinde olan personeller:\n", maasi_yuksek_personeller)

        # Doğum tarihi 1990 ve sonrası olan hastaları gösterme
        df_hasta['dogum_tarihi'] = pd.to_datetime(df_hasta['dogum_tarihi'])
        dogum_tarihi_1990_sonrasi = df_hasta[df_hasta['dogum_tarihi'] >= '1990-01-01']
        print("Doğum tarihi 1990 ve sonrası olan hastalar:\n", dogum_tarihi_1990_sonrasi)

        # Yeni bir DataFrame oluşturma
        yeni_df = df_personel[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili']].copy()
        yeni_df_hasta = df_hasta[['ad', 'soyad', 'hastalik', 'tedavi']].copy()
        print("Yeni Personel DataFrame:\n", yeni_df)
        print("Yeni Hasta DataFrame:\n", yeni_df_hasta)

    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()