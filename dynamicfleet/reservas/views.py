from django.shortcuts import render, get_object_or_404
from dynamicfleet.reservas.forms import ReserveForm
from dynamicfleet.veiculos.models import Vehicle


def reserve_vehicle(request, pk=None):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    return render(request, 
                  'reservas/reserve_vehicle.html', 
                  {'form': ReserveForm(), 'vehicle': vehicle },)
