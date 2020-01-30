from django.shortcuts import render, HttpResponse
from django.contrib import messages
from dynamicfleet.veiculos.forms import VehicleForm
from dynamicfleet.veiculos.models import Vehicle


def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)

        if not form.is_valid():
            return render(request, 'veiculos/register_vehicle.html', 
                          {'form': form})
        else:
            form.save()
            messages.success(request, 'O veículo foi registrado com sucesso.')

    return render(request, 'veiculos/register_vehicle.html', 
                    {'form': VehicleForm()})


def vehicles_list(request):
    vehicles = Vehicle.objects.filter(state='disponivel')
    return render(request, 'veiculos/vehicles_list.html', { 'vehicles' : vehicles})
    