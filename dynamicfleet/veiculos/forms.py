from django import forms
from dynamicfleet.veiculos.models import Vehicle


class VehicleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)

        # customize unique error message
        self.fields['license_plate'].error_messages.update({
            'unique': 'Já existe um veículo cadastrado com esta placa.',
        })

        self.fields['model'].widget.attrs['class'] = 'form-control'
        self.fields['license_plate'].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Vehicle
        fields = ['model', 'license_plate', 'year', 'state']


class FilterVehicleForm(forms.Form):
    start = forms.DateTimeField(label="Inicio", 
                                input_formats=['%d/%m/%Y %H:%M'],
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    end = forms.DateTimeField(label="Fim", 
                              input_formats=['%d/%m/%Y %H:%M'],
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
