from django import forms
from dynamicfleet.veiculos.models import Vehicle


class VehicleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)

        # customize unique error message
        self.fields['license_plate'].error_messages.update({
            'unique': 'Já existe um veículo cadastrado com esta placa.',
        })

    class Meta:
        model = Vehicle
        fields = ['model', 'license_plate', 'year', 'state']


class FilterVehicleForm(forms.Form):
    start = forms.DateTimeField(label="Inicio", input_formats=['%d/%m/%Y %H:%M'])
    end = forms.DateTimeField(label="Fim", input_formats=['%d/%m/%Y %H:%M'])
