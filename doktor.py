from personel import Personel  # Personel classını ekleme

class Doktor(Personel): #personel classından kalıtım sayesinde doktor classını türetme
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas) #super().__init__() sayesinde personeldeki özellikleri kalıtım yoluyla ekleme
        self._uzmanlik = uzmanlik #doktora özel özellikleri tanımlama
        self._deneyim_yili = deneyim_yili
        self._hastane = hastane

    # Getter metotları
    def get_uzmanlik(self):
        return self._uzmanlik
    
    def get_deneyim_yili(self):
        return self._deneyim_yili
    
    def get_hastane(self):
        return self._hastane

    def __str__(self): #bilgileri yazdırıcak str metodu
        return f"Personel No:{self.__personel_no}, Doktor Ad:{self.__ad}, Doktor Soyad:{self.__soyad}, Doktorun Departmanı:{self.__departman}, Doktorun Maaşı:{self.__maas}, Doktorun Uzmanlığı:{self._uzmanlik}, Doktorun Deneyim Yılı:{self._deneyim_yili}, Doktorun Çalıştığı Hastane:{self._hastane}"

    def maas_arttir(self): #maası belirli zam oranı kadar arttıran metot
        zam_orani = 1.2
        self.__maas = self.__maas * zam_orani
        return self.__maas