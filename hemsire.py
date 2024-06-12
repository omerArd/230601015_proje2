from personel import Personel #personel classını ekleme

class Hemsire(Personel): #personel classından kalıtım sayesinde hamsire classını oluşturma
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas) #super().__init__() sayesinde personeldeki özellikleri kalıtım yoluyla ekleme
        self._calisma_saati = calisma_saati #hemsire classına özel özellikleri ekleme
        self._sertifika = sertifika
        self._hastane = hastane

    # Getter metotları
    def get_calisma_saati(self):
        return self._calisma_saati
    
    def get_sertifika(self):
        return self._sertifika
    
    def get_hastane(self):
        return self._hastane

    def __str__(self): #str metoduyla bilgileri yazdırma
        return f"Personel No:{self.__personel_no}, Personel Ad:{self.__ad}, Personel soyad:{self.__soyad}, Personel departmanı:{self.__departman}, Personel maaşı:{self._maas}, Personel Çalışma Saati:{self._calisma_saati}, Personelin Sertifikası:{self._sertifika}, Personelin Hastanesi:{self._hastane}"

    def maas_arttir(self): #maası belirli zam oranı kadar arttıran metot
        zam_orani = 1.16
        self._maas = self._maas * zam_orani
        return self._maas