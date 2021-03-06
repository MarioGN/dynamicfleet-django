from django.db.models import QuerySet
from django.test import TestCase
from django.shortcuts import reverse, resolve_url as r


class ReservesListGet(TestCase):
    def setUp(self):
       self.response = self.client.get(r('reservas:reserves_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'reservas/reserves_list.html')

    def test_reserves_in_context(self):
        reserves = self.response.context['reserves']
        self.assertIsInstance(reserves, QuerySet)
