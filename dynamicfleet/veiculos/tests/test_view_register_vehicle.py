from django.test import TestCase
from django.shortcuts import resolve_url as r
from dynamicfleet.veiculos.models import Vehicle
from dynamicfleet.veiculos.forms import VehicleForm


class RegisterVehicleGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('veiculos:register_vehicle'))
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'veiculos/register_vehicle.html')

    def test_html(self):
        tags = (('<form', 1),
                ('<input', 4),
                ('<select', 1),
                ('type="text"', 2),
                ('type="number"', 1),
                ('type="button"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, VehicleForm)


class RegisterVehiclePostValid(TestCase):
    def setUp(self):
        data = dict(model='Gol', 
                    license_plate='XYZ2284', 
                    year=2018, 
                    state='disponivel')
        self.response = self.client.post(r('veiculos:register_vehicle'), data)

    def test_post(self):
        self.assertEqual(self.response.status_code, 200)

    def test_save_vehicle(self):
        self.assertTrue(Vehicle.objects.exists())


class RegisterVehiclePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('veiculos:register_vehicle'), {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'veiculos/register_vehicle.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, VehicleForm)

    def test_has_form_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_vehicle(self):
        self.assertFalse(Vehicle.objects.exists())
