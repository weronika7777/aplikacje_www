from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Rosliny
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from rest_framework import status

# Create your tests here.
class RoslinyTestCase(TestCase):

    def post(self,_gatunek, _wzrost, _mrozoodporne, _opis):
        url = reverse(views.RoslinyList.name)
        data= {
            'gatunek': _gatunek,
            'wzrost': _wzrost,
            'mrozoodporne': _mrozoodporne,
            'opis': _opis,

        }
        response = self.client.post(url, data, format='json')
        return response

    def test_rosliny_czy_mrozoodporne(self):
        response = self.post('skierniewicka', '80', False, 'latwe_w_uprawie')
        self.assertFalse(response.data['mrozoodporne'])

    def test_rosliny_liczba(self):
        self.post('kumkwat', '30', False, 'smieszny')
        self.post('kumkwat', '30', False, 'smieszny')
        self.post('kumkwat', '30', False, 'smieszny')
        rosliny_count = Rosliny.objects.all().count()
        self.assertEqual(rosliny_count, 3)

    def test_rosliny_dodaj(self):
        response = self.post('kumkwat', '30', False, 'smieszny')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rosliny_czywysokie(self):
        response = self.post('kumkwat', '30', False, 'smieszny')
        self.assertLess(response.data['wzrost'], 80)

    def test_rosliny_czykumkwat(self):
        response = self.post('kumkwat', '30', False, 'smieszny')
        self.assertEqual(response.data['gatunek'], 'kumkwat')