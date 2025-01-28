from rest_framework import generics
from .models import Klient, Faktura, Produkt, Pozycja_na_fakturze
from .serializers import  KlientSerializer, ProduktSerializer, FakturaSerializer, Pozycja_na_fakturzeSerializer

class KlientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    
class KlientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

#Produkt
class ProduktListCreateAPIView(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer

class ProduktRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer

#Faktura
class FakturaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Faktura.objects.all()
    serializer_class = FakturaSerializer

class FakturaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faktura.objects.all()
    serializer_class = FakturaSerializer