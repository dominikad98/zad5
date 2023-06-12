from django.db import models

class Kurs(models.Model):
    nazwa = models.CharField(max_length=100)
    data_rozpoczecia = models.DateField()
    ilosc_miejsc = models.IntegerField(default=0)

    def __str__(self):
        return self.nazwa

    def ilosc_miejsc_wolnych(self):
        return self.ilosc_miejsc - self.uczestnik_set.count()

    def ilosc_uczestnikow(self):
        return self.uczestnik_set.count()

class Uczestnik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
