from django.urls import path, re_path
from dynamicfleet.reservas.views import reserve_vehicle, reserves_list

app_name = 'reservas'

urlpatterns = [
    path('', reserves_list, name='reserves_list'),
    re_path(r'^new/(?P<pk>\d+)/$', reserve_vehicle, name='reserve_vehicle'),
]