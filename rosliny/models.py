from django.db import models

# Create your models here.
class Rosliny(models.Model):
    gatunek=models.CharField(max_length=20)
    wzrost= models.IntegerField()
    mrozoodporne=models.BooleanField()
    opis=models.CharField(max_length=30)

    def __str__(self):
        return self.gatunek

class Rynek(models.Model):
    miejscowosc = models.CharField(max_length=20)
    rosliny = models.ForeignKey(Rosliny, on_delete=models.DO_NOTHING)
    cena = models.IntegerField()
    ilosc =models.IntegerField()
    dostepnosc = models.BooleanField()


    def __str__(self):
        return self.miejscowosc