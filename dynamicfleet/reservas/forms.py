from django import forms
from django.core.exceptions import ValidationError
from dynamicfleet.reservas.models import Reserve


class ReserveForm(forms.ModelForm):
    start = forms.DateTimeField(label="Inicio", input_formats=['%d/%m/%Y %H:%M'])
    end = forms.DateTimeField(label="Fim", input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Reserve
        fields = ['start', 'end', 'state']


class FilterReserveForm(forms.Form):
    start = forms.DateTimeField(label="Inicio", input_formats=['%d/%m/%Y %H:%M'])
    end = forms.DateTimeField(label="Fim", input_formats=['%d/%m/%Y %H:%M'])
