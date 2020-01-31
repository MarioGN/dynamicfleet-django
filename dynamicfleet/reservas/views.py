from django.shortcuts import render, get_object_or_404, HttpResponse
from dynamicfleet.reservas.forms import ReserveForm
from dynamicfleet.reservas.models import Reserve
from dynamicfleet.veiculos.models import Vehicle


def reserve_vehicle(request, pk=None):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'POST':
        form = ReserveForm(request.POST)

        if not form.is_valid():
            return render(request, 
                  'reservas/reserve_vehicle.html', 
                  {'form': form, 'vehicle': vehicle })
        else:
            reserve = Reserve()
            reserve.vehicle = vehicle
            reserve.start = form.cleaned_data.get('start')
            reserve.end = form.cleaned_data.get('end')
            reserve.state = form.cleaned_data.get('state')

            reserve.save()
   
    return render(request, 
                  'reservas/reserve_vehicle.html', 
                  {'form': ReserveForm(), 'vehicle': vehicle })

def reserves_list(request):
    return render(request, 'reservas/reserves_list.html')