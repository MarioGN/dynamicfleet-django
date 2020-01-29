from django.test import TestCase
from django.shortcuts import resolve_url as r


class RerserveVehicleGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('reservas:reserve_vehicle'))
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'reservas/reserve_vehicle.html')
