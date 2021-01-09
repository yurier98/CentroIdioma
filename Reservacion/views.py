from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from Reservacion.models import Reservacion
from Reservacion.forms import ReservarForm


@login_required
def index(request):
    reservaciones_list = Reservacion.objects.all()
    context = {'reservaciones_list': reservaciones_list}
    return render(request, 'reservaciones/reservaciones_index.html', context)


@login_required
def reservar(request):
    if request.method == 'POST':
        form = ReservarForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('reservaciones:reservaciones'))
    # return HttpResponseRedirect(Reservacion)
    else:
        form = ReservarForm()
    return render(request, 'reservaciones/reservar.html', {'form': form})


@login_required
def reservacion_detail(request, id):
    reservacion = get_object_or_404(Reservacion, pk=id)
    return render(request, 'reservaciones/reservar.html', {'reservacion': reservacion})


@login_required
def reservacion_edit(request, id):
    reservacion = get_object_or_404(Reservacion, pk=id)
    if request.method == 'POST':
        form = ReservarForm(request.POST, instance=reservacion)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('reservaciones:reservaciones'))
    # return HttpResponseRedirect(Reservacion)
    else:
        form = ReservarForm(instance=reservacion)
    return render(request, 'reservaciones/reservacion_edit.html', {'form': form})


@login_required
def reservacion_delete(request, id):
    reservacion = get_object_or_404(Reservacion, pk=id)
    # if request.method == 'POST':
    #     form = ReservarForm(request.POST, instance=reservacion)
    #     if form.is_valid():
    #         form.save()
    #     return HttpResponseRedirect(reverse('reservaciones:reservaciones'))
    # # return HttpResponseRedirect(Reservacion)
    # else:
    #     form = ReservarForm(instance=reservacion)
    return render(request, 'reservaciones/reservacion_delete.html', {'reservacion': reservacion})
