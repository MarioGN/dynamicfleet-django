from django.shortcuts import render
from dynamicfleet.reservas.forms import ReserveForm
from dynamicfleet.veiculos.models import Vehicle


def reserve_vehicle(request):
    vehicle = Vehicle.objects.all()[0]

    return render(request, 
                  'reservas/reserve_vehicle.html', 
                  {'form': ReserveForm(), 'vehicle': vehicle },)
