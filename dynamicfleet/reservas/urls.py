from django.urls import path, re_path
from dynamicfleet.reservas.views import reserve_vehicle, reserves_list, edit_reserve

app_name = 'reservas'

urlpatterns = [
    path('', reserves_list, name='reserves_list'),
    re_path(r'^new/(?P<pk>\d+)/$', reserve_vehicle, name='reserve_vehicle'),
    re_path(r'^edit/(?P<pk>\d+)/$', edit_reserve, name='edit_reserve'),
]