from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    admin = models.BooleanField()

class Zahtjev(models.Model):
    vrsta_prijavitelja = models.CharField(max_length=255)
    ime_prezime_naziv = models.CharField(max_length=255)
    prebivaliste_sjediste = models.CharField(max_length=255)
    zastupnik = models.CharField(max_length=255)
    oib_mbs = models.CharField(max_length=255)
    tel_mob = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # Da se ne radi jos jedna tablica, sve ce ici ovdje...
    # Lokacija je uvijek Grad Zagreb
    gradska_cetvrt = models.CharField(max_length=255)
    mjesni_odbor = models.CharField(max_length=255)
    naziv_prostora = models.CharField(max_length=255)
    adresa_prostora = models.CharField(max_length=255)
    kvadratura = models.IntegerField()
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
    files = models.CharField(max_length=255)

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
    datum_unosa = models.DateTimeField()
    osoba_unijela = models.CharField(max_length=255)
    osoba_obradila = models.CharField(max_length=255)
    token_potvrda_maila = models.CharField(max_length=255)

    # Field can be used to quickly extend
    freeform = models.CharField(max_length=255)
