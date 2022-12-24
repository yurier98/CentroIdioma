from bootstrap_modal_forms.generic import BSModalCreateView, \
    BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView

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


class ReservacionDelete(SuccessMessageMixin, BSModalDeleteView):
    model = Reservacion
    template_name = 'reservaciones/delete_reservacion.html'
    success_message = 'Su reservación se ha eliminado con exito'
    success_url = reverse_lazy('reservaciones:reservaciones')


class ReservacionUpdate(LoginRequiredMixin, BSModalUpdateView):
    model = Reservacion
    form_class = ReservarForm
    template_name = 'reservaciones/update_reservacion.html'
    success_message = 'Su reservación se ha actualizado con exito'
    success_url = reverse_lazy('reservaciones:reservaciones')


class ReservacionCreate(LoginRequiredMixin, BSModalCreateView):
    form_class = ReservarForm
    template_name = 'reservaciones/create_reservacion.html'
    success_message = 'Reservación creada correctamente.'  # Mostramos este Mensaje luego de Crear una reservacion
    success_url = reverse_lazy('reservaciones:reservaciones')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class DetailReservacion(BSModalReadView):
    model = Reservacion
    template_name = 'reservaciones/detail_reservacion.html'
