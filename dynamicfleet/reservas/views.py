from django.shortcuts import render, HttpResponse


def reserve_vehicle(request):
    return render(request, 'reservas/reserve_vehicle.html')
