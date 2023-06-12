from django.shortcuts import render
from rest_framework import viewsets
from .models import Kurs, Uczestnik
from .serializers import KursSerializer, UczestnikSerializer

def kurs_detail(request, kurs_id):
    kurs = Kurs.objects.get(id=kurs_id)
    ilosc_uczestnikow = kurs.ilosc_uczestnikow()
    ilosc_miejsc_wolnych = kurs.ilosc_miejsc_wolnych()
    
    context = {
        'kurs': kurs,
        'ilosc_uczestnikow': ilosc_uczestnikow,
        'ilosc_miejsc_wolnych': ilosc_miejsc_wolnych
    }
    

    return render(request, 'kurs_detail.html', context)


class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class UczestnikViewSet(viewsets.ModelViewSet):
    queryset = Uczestnik.objects.all()
    serializer_class = UczestnikSerializer
