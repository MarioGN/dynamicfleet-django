from datetime import datetime, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from dynamicfleet.reservas.models import Reserve
from dynamicfleet.veiculos.models import Vehicle


class ReserveModelTest(TestCase):

    def setUp(self):
        self.vehicle_obj = Vehicle(
            model='Gol',
            license_plate='XYZ2284',
            year=2018,
        )
        self.vehicle_obj.save()

        self.reserve_obj = Reserve(vehicle=self.vehicle_obj)
        self.reserve_obj.save()

    def test_create(self):
        self.assertTrue(Reserve.objects.exists())

    def test_start_date_cannot_be_less_than_today(self):
        self.reserve_obj.start = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.reserve_obj.full_clean()

    def test_end_date_cannot_be_less_start(self):
        self.reserve_obj.start = datetime.now()
        self.reserve_obj.end = datetime.now() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.reserve_obj.clean()

    def test_default_state(self):
        self.assertEqual('provisoria', self.reserve_obj.state)
