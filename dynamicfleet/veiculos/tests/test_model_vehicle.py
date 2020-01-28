from django.test import TestCase
from dynamicfleet.veiculos.models import Vehicle


class VehicleModelTest(TestCase):

    def setUp(self):
        self.obj = Vehicle(
            model='Gol',
            license_plate='XYZ2284',
            year=2018,
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Vehicle.objects.exists())

    def test_model(self):
        self.assertEqual('Gol', self.obj.model)

    def test_license(self):
        self.assertEqual('XYZ2284', self.obj.license_plate)

    def test_year(self):
        self.assertEqual(2018, self.obj.year)
    
    def test_default_state(self):
        self.assertEqual('SP', self.obj.state)

    def test_update_state(self):
        self.obj.state = 'PR'
        self.obj.save()
        self.assertEqual('PR', self.obj.state)

