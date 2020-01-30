from django.test import TestCase
from django.shortcuts import resolve_url as r
from dynamicfleet.reservas.forms import ReserveForm


class ReserveVehicleGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('reservas:reserve_vehicle'))
    
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
