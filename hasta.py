class Hasta():
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi): #class yapısının özelliklerini tanımlama
        self._hasta_no = hasta_no
        self._ad = ad
        self._soyad = soyad
        self._dogum_tarihi = dogum_tarihi
        self._hastalik = hastalik
        self._tedavi = tedavi

    #get metotları
    def get_hasta_no(self): 
        return self._hasta_no

    def get_ad(self):
        return self._ad

    def get_soyad(self):
        return self._soyad

    def get_dogum_tarihi(self):
        return self._dogum_tarihi

    def get_hastalik(self):
        return self._hastalik

    def get_tedavi(self):
        return self._tedavi

    def __str__(self): #str metoduyla bilgileri yazdırma
        return f"Hasta No:{self._hasta_no}, Hasta Ad:{self._ad}, Hasta soyad:{self._soyad}, Hasta Doğum Tarihi:{self._dogum_tarihi}, Teşhis:{self._hastalik}, Tedavi:{self._tedavi}"

    def tedavi_suresi_hesapla(self): #tedavi ismine göre tedavi süresi hesaplayan metot
        tedavi_suresi = 0
        if self._hastalik.lower() == "insülin tedavisi":
            tedavi_suresi = 200
        elif self._hastalik.lower() == "soğuk algınlığı":
            tedavi_suresi = 10
        elif self._hastalik.lower() == "kemoterapi":
            tedavi_suresi = 365
        if tedavi_suresi == 0:
            return "Tedavi süresi belli değil:("
        else:
            return f"Tedavi süresi {tedavi_suresi} gün"