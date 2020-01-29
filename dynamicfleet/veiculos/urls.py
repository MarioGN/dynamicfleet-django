from django.urls import path
from dynamicfleet.veiculos.views import register_vehicle, vehicles_list

app_name = 'veiculos'

urlpatterns = [
    path('', vehicles_list, name='vehicles_list'),
    path('veiculos/', register_vehicle, name='register_vehicle'),
]