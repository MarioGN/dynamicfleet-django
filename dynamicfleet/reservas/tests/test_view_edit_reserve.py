from datetime import datetime, timedelta
from django.test import TestCase
from django.shortcuts import reverse, resolve_url as r, reverse
from dynamicfleet.reservas.models import Reserve
from dynamicfleet.veiculos.models import Vehicle


class EditReserveGet(TestCase):
    def setUp(self):
        self.vehicle_obj = Vehicle(
            model='Gol',
            license_plate='XYZ2284',
            year=2018,
        )
        self.vehicle_obj.save()

        self.reserve = Reserve(vehicle=self.vehicle_obj,
                                start=datetime.now() + timedelta(days=5),
                                end=datetime.now() + timedelta(days=10))
        self.reserve.save()
        
        self.response = self.client.get(reverse('reservas:edit_reserve', kwargs={'pk': self.reserve.pk}))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'reservas/reserve_vehicle.html')
