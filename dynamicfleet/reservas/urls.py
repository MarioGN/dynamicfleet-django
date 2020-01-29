from django.urls import path
from dynamicfleet.reservas.views import reserve_vehicle

app_name = 'reservas'

urlpatterns = [
    path('', reserve_vehicle, name='reserve_vehicle'),
]