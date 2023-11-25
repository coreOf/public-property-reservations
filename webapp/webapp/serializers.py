from rest_framework import serializers
from .models import User, Zahtjev
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.save()
        return user

class ZahtjevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zahtjev
        fields = (
            'id',
            'vrsta_prijavitelja',
            'ime_prezime_naziv',
            'prebivaliste_sjediste',
            'zastupnik',
            'oib_mbs',
            'tel_mob',
            'email',
            'gradska_cetvrt',
            'mjesni_odbor',
            'naziv_prostora',
            'adresa_prostora',
            'kvadratura',
            'opis',
            'slika',
            'vrsta_prostora',
            'sat_od',
            'sat_do',
            'vrsta_termina',
            'files',
            'status',
            'datum_unosa',
            'osoba_unijela',
            'osoba_obradila',
            'token_potvrda_maila',
            'freeform')
    
    def create(self, validated_data):
        zahtjev = Zahtjev.objects.create(
            vrsta_prijavitelja = validated_data['vrsta_prijavitelja'],
            ime_prezime_naziv = validated_data['ime_prezime_naziv'],
            prebivaliste_sjediste = validated_data['prebivaliste_sjediste'],
            zastupnik = validated_data['zastupnik'],
            oib_mbs = validated_data['oib_mbs'],
            tel_mob = validated_data['tel_mob'],
            email = validated_data['email'],
            gradska_cetvrt = validated_data['gradska_cetvrt'],
            mjesni_odbor = validated_data['mjesni_odbor'],
            naziv_prostora = validated_data['naziv_prostora'],
            adresa_prostora = validated_data['adresa_prostora'],
            kvadratura = validated_data['kvadratura'],
            opis = validated_data['opis'],
            slika = validated_data['slika'],
            vrsta_prostora = validated_data['vrsta_prostora'],
            sat_od = validated_data['sat_od'],
            sat_do = validated_data['sat_do'],
            vrsta_termina = validated_data['vrsta_termina'],
            files = validated_data['files'],
            status = validated_data['status'],
            datum_unosa = validated_data['datum_unosa'],
            osoba_unijela = validated_data['osoba_unijela'],
            osoba_obradila = validated_data['osoba_obradila'],
            token_potvrda_maila = validated_data['token_potvrda_maila'],
            freeform = validated_data['freeform']
        )
        zahtjev.save()
        return zahtjev
