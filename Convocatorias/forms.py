from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from Convocatorias.models import Inscripcion


# from bootstrap_datepicker_plus import DateTimePickerInput


class InscripcionForm(ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['fecha', 'convocatoria']
        help_texts = {

            'fecha': _('Formato de la fecha dd/mm/yyyy 00:00'),
        }
        error_messages = {
            'fecha': {
                'max_length': _("El formato de la fecha es incorrecto ejemplo : 01/12/2020 ."),
            }
        }
        # widgets = {
        #     'fecha': DateTimePickerInput(),  # default date-format %m/%d/%Y will be used
        #   #  'end_date': DatePickerInput(format='%Y-%m-%d'),  # specify date-frmat
        # }
