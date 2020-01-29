from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.db.models import QuerySet
from dynamicfleet.veiculos.models import Vehicle


class VehiclesListeGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('veiculos:vehicles_list'))
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'veiculos/vehicles_list.html')

    def test_vehicles_in_context(self):
        vehicles = self.response.context['vehicles']
        self.assertIsInstance(vehicles, QuerySet)


class VehiclesListeGetEmpty(TestCase):
    def setUp(self):
        self.response = self.client.get(r('veiculos:vehicles_list'))

    def test_vehicles_list_empty(self):
        vehicles = self.response.context['vehicles']
        self.assertEqual(0, len(vehicles))

    def test_vehicles_list_empty_message(self):
        message = '<p id="alert-empty-list">Ainda não existem veículos registrados no sistema!</p>'
        self.assertContains(self.response, message)


class VehiclesListeGetHasItems(TestCase):
    def setUp(self):
        self.obj = Vehicle(
            model='Gol',
            license_plate='XYZ2284',
            year=2018,
        )

        self.obj.save()

        self.response = self.client.get(r('veiculos:vehicles_list'))

    def test_vehicles_list_has_items(self):
        vehicles = self.response.context['vehicles']
        self.assertEqual(1, len(vehicles))


    def test_vehicles_list_hide_empty_message(self):
        message = '<p id="alert-empty-list">Ainda não existem veículos registrados no sistema!</p>'
        self.assertNotContains(self.response, message)

    def test_vehicles_list(self):
        contents = [
            'Gol',
            'XYZ2284',
            '2018',
            'disponivel',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
