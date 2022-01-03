from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from Reservacion.forms import ReservarForm
from Reservacion.models import Reservacion


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
    return render(request, 'reservaciones/reservaciones_create.html', {'form': form})


@login_required
def reservacion_detail(request, id):
    reservacion = get_object_or_404(Reservacion, pk=id)
    return render(request, 'reservaciones/reservacion_detail.html', {'reservacion': reservacion})


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


@login_required
def index(request):
    reservaciones_list = Reservacion.objects.all()
    context = {'reservaciones_list': reservaciones_list}
    return render(request, 'reservaciones/reservaciones_index.html', context)


class ReservacionesView(LoginRequiredMixin, ListView):
    """ Return all reservaciones """

    template_name = 'reservaciones/reservaciones_index.html'
    model = Reservacion
    ordering = ('-fecha',)
    context_object_name = 'reservaciones_list'


class ReservacionDetailView(LoginRequiredMixin, DetailView):
    """Return reservaciones detail."""

    template_name = 'reservaciones/reservacion_detail.html'
    queryset = Reservacion.objects.all()
    context_object_name = 'reservacion'


class ReservacionCreate(LoginRequiredMixin, CreateView):
    model = Reservacion
    form_class = ReservarForm
    template_name = 'reservaciones/reservaciones_create.html'
    success_message = 'Reservación creada correctamente !'  # Mostramos este Mensaje luego de Crear una reservacion
    success_url = reverse_lazy('reservaciones:reservaciones')
