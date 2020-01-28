from django.urls import path
from dynamicfleet.veiculos.views import register_vehicle

app_name = 'veiculos'

urlpatterns = [
    path('', register_vehicle, name='register_vehicle'),
]