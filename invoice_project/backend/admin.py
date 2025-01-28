from django.contrib import admin
from .models import Klient, Faktura, Produkt, Pozycja_na_fakturze

# Register your models here.
@admin.register(Klient)
class KlientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Klient._meta.fields]
    search_fields = ['imie', 'nazwisko', 'nr_telefonu', 'rodzaj_dzialalnosci', 'nazwa_firmy', 'nip']
    list_filter = ['rodzaj_dzialalnosci']
    
@admin.register(Faktura)
class FakturaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Faktura._meta.fields]
    search_fields = ['numer_faktury', 'klient__nazwa_firmy', 'klient__nip', 'klient__imie', 'klient__nazwisko']
    list_filter = ['status']
    
@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'cena_netto', 'stawka_vat']
    search_fields = ['nazwa']
    list_filter = ['stawka_vat']
    
@admin.register(Pozycja_na_fakturze)
class PozycjaNaFakturze(admin.ModelAdmin):
    fields = ('faktura', 'produkt', 'ilosc', 'cena_netto', 'stawka_vat', 'kwota_vat', 'kwota_brutto')
    readonly_fields = ('kwota_vat', 'kwota_brutto')