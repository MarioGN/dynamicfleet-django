from django.test import TestCase
from django.shortcuts import reverse, resolve_url as r
from dynamicfleet.reservas.forms import ReserveForm
from dynamicfleet.veiculos.models import Vehicle


class ReserveVehicleGet(TestCase):
    def setUp(self):
        self.obj = Vehicle(
            model='Gol',
            license_plate='XYZ2284',
            year=2018,
        )
        self.obj.save()
        
        self.response = self.client.get(reverse('reservas:reserve_vehicle', kwargs={'pk': self.obj.pk}))
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'reservas/reserve_vehicle.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ReserveForm)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_html(self):
        tags = (('<form', 1),
                ('<input', 3),
                ('<select', 1),
                ('type="text"', 2),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_has_vehicle_object(self):
        form = self.response.context['vehicle']
        self.assertIsInstance(form, Vehicle)

    def test_html_vehicle(self):
        tags = (('<td>{}</td>'.format(self.obj.model), 1),
                ('<td>{}</td>'.format(self.obj.license_plate), 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


class ReserveVehicleDoesNotExistGet(TestCase):
    def test_get(self):
        self.response = self.client.get(reverse('reservas:reserve_vehicle', kwargs={'pk': 99}))
        self.assertEqual(404, self.response.status_code)
    
