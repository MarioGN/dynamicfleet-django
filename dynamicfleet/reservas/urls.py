from django.urls import path, re_path
from dynamicfleet.reservas.views import reserve_vehicle

app_name = 'reservas'

urlpatterns = [
    re_path(r'^new/(?P<pk>\d+)/$', reserve_vehicle, name='reserve_vehicle'),
]