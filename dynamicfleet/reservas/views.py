from django.shortcuts import render
from dynamicfleet.reservas.forms import ReserveForm


def reserve_vehicle(request):
    return render(request, 
                  'reservas/reserve_vehicle.html', 
                  {'form': ReserveForm()})
