from django import forms
from django.utils.translation import gettext_lazy as _

from Reservacion.models import Reservacion


class ReservarForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['fecha', 'hora', 'laboratorio', 'maquina', 'usuario', ]

        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'laboratorio': 'Laboratorio',
            'maquina': 'Máquina',
            'usuario': 'usuario',
        }

        widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'),
                                     attrs={'class': 'form-control', 'placeholder': 'Selecciona la fecha',
                                            'type': 'date'}),

            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Selecciona la hora',
                                           'type': 'time'}),
            'laboratorio': forms.Select(attrs={'class': 'form-control'}),
            'maquina': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),

        }

        help_texts = {

            'fecha': _('Formato de la fecha dd/mm/yyyy'),
        }
        error_messages = {
            'fecha': {
                'max_length': _("El formato de la fecha es incorrecto ejemplo : 01/12/2020 ."),
            }
        }
