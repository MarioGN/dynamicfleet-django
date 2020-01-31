from django.shortcuts import render, HttpResponse
from django.contrib import messages
from dynamicfleet.veiculos.forms import VehicleForm, FilterVehicleForm
from dynamicfleet.veiculos.models import Vehicle
from django.db.models import Q


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
    vehicles = Vehicle.objects.filter(state='disponivel', reserves__isnull=True).distinct() 

    if request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')

        if start and end:
            form = FilterVehicleForm(request.GET)
            form.full_clean()
            
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')

            vehicles = Vehicle.objects.filter(state='disponivel')
            vehicles = vehicles.filter(
                            Q(reserves__isnull=True) | 
                            ~Q(
                                Q(
                                    Q(reserves__start__range=(start, end)) |
                                    Q(reserves__end__range=(start, end))
                                ) | ~Q(reserves__state='cancelada')
                            )
                        ).distinct()

    return render(request, 
                  'veiculos/vehicles_list.html', 
                  {'vehicles' : vehicles, 'form': FilterVehicleForm()})
    