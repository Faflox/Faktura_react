from django.urls import path
from .views import (
    KlientListCreateAPIView, KlientRetrieveUpdateDestroyAPIView,
    ProduktListCreateAPIView, ProduktRetrieveUpdateDestroyAPIView,
    FakturaListCreateAPIView, FakturaRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    #klient
    path('klienci/', KlientListCreateAPIView.as_view(), name='klient-list-create'),
    path('klienci/<int:pk>/', KlientRetrieveUpdateDestroyAPIView.as_view(), name='klient-detal'),
    #produkt
    path('produkty/', ProduktListCreateAPIView.as_view(), name='produkt-list-create'),
    path('produkty/<int:pk>/', ProduktRetrieveUpdateDestroyAPIView.as_view(), name='produkt-detal'),
    #faktura
    path('faktury/', FakturaListCreateAPIView.as_view(), name='faktura-list-create'),
    path('faktury/<int:pk>/', FakturaRetrieveUpdateDestroyAPIView.as_view(), name='faktura-detal'),
]   
