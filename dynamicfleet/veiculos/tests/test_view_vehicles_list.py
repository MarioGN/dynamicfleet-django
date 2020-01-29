from django.test import TestCase
from django.shortcuts import resolve_url as r


class VehiclesListeGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('veiculos:vehicles_list'))
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'veiculos/vehicles_list.html')
