from rest_framework import serializers
from .models import Klient, Produkt, Faktura, Pozycja_na_fakturze

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'
        
class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'
        
class FakturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faktura
        fields = '__all__'
        
class Pozycja_na_fakturzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pozycja_na_fakturze
        fields = '__all__'
