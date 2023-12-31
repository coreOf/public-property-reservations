from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Zahtjev(models.Model):
    vrsta_prijavitelja = models.CharField(
        max_length = 30,
        choices = [
            ("Fizicka_osoba", "Fizička osoba"),
            ("Pravna_osoba", "Pravna osoba"),
            ("Neprofitna_organizacija", "Neprofitna organizacija"),
            ("Drugo", "Drugo")
        ])
    ime_prezime_naziv = models.CharField(max_length=255)
    prebivaliste_sjediste = models.CharField(max_length=255)
    zastupnik = models.CharField(max_length=255, blank=True)
    oib_mbs = models.CharField(max_length=255)
    tel_mob = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # Da se ne radi jos jedna tablica, sve ce ici ovdje...
    # Lokacija je uvijek Grad Zagreb
    gradska_cetvrt = models.CharField(max_length=255, blank=True)
    mjesni_odbor = models.CharField(max_length=255, blank=True)
    naziv_prostora = models.CharField(max_length=255, blank=True)
    adresa_prostora = models.CharField(max_length=255, blank=True)
    kvadratura = models.IntegerField(blank=True)
    opis = models.CharField(max_length=255)
    # Ako se uspije dodati, moze biti i slika pohranjena na frontendu
    slika = models.CharField(max_length=255)

    vrsta_prostora = models.CharField(
        max_length = 20,
        choices = [
            ("Ured", "Ured"),
            ("Prostor", "Prostor"),
            ("Dvorana", "Dvorana")
        ])
    dan_u_tjednu = models.CharField(
        max_length = 20,
        choices = [
            ("Ponedjeljak", "Ponedjeljak"),
            ("Utorak", "Utorak"),
            ("Srijeda", "Srijeda"),
            ("Cetvrtak", "Četvrtak"),
            ("Petak", "Petak"),
            ("Subota", "Subota"),
            ("Nedjelja", "Nedjelja")
        ])
    sat_od = models.IntegerField()
    sat_do = models.IntegerField()

    vrsta_termina = models.CharField(
        max_length = 20,
        choices = [
            ("Tjedno", "Tjedno"),
            ("Mjesecno", "Mjesečno")
        ])
    
    # Ideja - napravi se upload folder za zahtjev ako je potrebno, pa je ovo folder
    files = models.CharField(max_length=255, blank=True)

    # Pomocna polja za obradu
    status = models.CharField(
        max_length = 20,
        choices = [
            ("Zaprimljen", "Zaprimljen"),
            ("Prihvacen", "Prihvaćen"),
            ("Odbijen", "Odbijen"),
            ("Odbijen_uvjetno", "Uvjetno odbijen")
        ])
    datum_unosa = models.DateTimeField()
    osoba_unijela = models.CharField(max_length=255, blank=True)
    osoba_obradila = models.CharField(max_length=255, blank=True)
    token_potvrda_maila = models.CharField(max_length=255, blank=True)

    # Field can be used to quickly extend
    freeform = models.CharField(max_length=255, blank=True)
