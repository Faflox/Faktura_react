from django.core.exceptions import ValidationError
from django.db import models
from datetime import timedelta, datetime

# Create your models here.
class Klient(models.Model):
    RODZ_DZ_WYBORY = [
        ('P', 'Osoba prywatna'),
        ('J', 'Jednoosobowa działalność gospodarcza'),
        ('I', 'Inna forma działalności'),
    ]
    
    imie = models.CharField(max_length=50, blank=True, null=True)
    nazwisko = models.CharField(max_length=100, blank=True, null=True)
    nr_telefonu = models.CharField(max_length=12, blank=True, null=True)
    #
    rodzaj_dzialalnosci = models.CharField(max_length=1, choices=RODZ_DZ_WYBORY, default='I')
    nazwa_firmy = models.CharField(max_length=200, blank=True, null=True)
    nip = models.CharField(max_length=10, unique=True, blank=True, null=True)
    #
    ulica = models.CharField(max_length=50)
    nr_budynku = models.CharField(max_length=20)
    nr_lokalu = models.CharField(max_length=20, blank=True, null=True)
    kod_pocztowy = models.CharField(max_length=6)
    miejscowosc = models.CharField(max_length=60)
    kraj = models.CharField(max_length=60)
    
    def clean(self):
        if self.rodzaj_dzialalnosci == 'P':
            if not self.imie or not self.nazwisko or not self.nr_telefonu:
                raise ValidationError('Dla osoby prywatnej musisz podać imię, nazwisko i numer telefonu.')
        elif self.rodzaj_dzialalnosci in ['I', 'J']:
            if not self.nazwa_firmy or not self.nip:
                raise ValidationError('Dla firmy musisz podać nazwę firmy i NIP.')
            
    def __str__(self):
        nazwa = ''
        if self.nip:
            nazwa = f'{self.nazwa_firmy}'
        else:
            nazwa  = f'{self.imie} {self.nazwisko}'
        return nazwa
        
class Faktura(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.SET_NULL, null=True)
    numer_faktury = models.CharField(max_length=50, unique=True)
    data_wystawienia = models.DateField()
    data_sprzedazy = models.DateField()
    termin_platnosci = models.DateField()
    status = models.CharField(max_length=1, choices=[('N', 'Nieopłacona'), ('O', 'Opłacona')], default='N') 
    suma_netto = models.DecimalField(max_digits=10, decimal_places=2)
    suma_brutto = models.DecimalField(max_digits=10, decimal_places=2)
    podatek_vat = models.DecimalField(max_digits=5, decimal_places=2)   

    def save(self, *args, **kwargs):
        if not self.termin_platnosci:
            self.termin_platnosci = self.data_wystawienia + timedelta(days=14)
        if not self.numer_faktury:
            numer = f'{self.id or 1}/{datetime.now().month:02}/{datetime.now().year}'
            self.numer_faktury = numer
        super().save(*args, **kwargs)

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField(blank=True, null=True)
    cena_netto = models.DecimalField(max_digits=10, decimal_places=2)
    stawka_vat = models.DecimalField(max_digits=5, decimal_places=2, default=23)
    
    def __str__(self):
        return self.nazwa

class Pozycja_na_fakturze(models.Model):
    faktura = models.ForeignKey(Faktura, on_delete=models.CASCADE, related_name='pozycje')
    produkt = models.ForeignKey(Produkt, on_delete=models.SET_NULL, null=True, blank=True)
    ilosc = models.PositiveIntegerField()
    cena_netto = models.DecimalField(max_digits=10, decimal_places=2)
    stawka_vat = models.DecimalField(max_digits=5, decimal_places=2, default=23)  # Domyślnie 23%
    kwota_vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    kwota_brutto = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.kwota_vat = (self.cena_netto * self.ilosc) * (self.stawka_vat / 100)
        self.kwota_brutto = (self.cena_netto * self.ilosc) + self.kwota_vat
        super().save(*args, **kwargs)
        
