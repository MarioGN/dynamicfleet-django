from django import forms
from django.core.exceptions import ValidationError
from dynamicfleet.reservas.models import Reserve


class ReserveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReserveForm, self).__init__(*args, **kwargs)

        self.fields['start'].widget.attrs['class'] = 'form-control'
        self.fields['end'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'

    start = forms.DateTimeField(label="Inicio", input_formats=['%d/%m/%Y %H:%M'])
    end = forms.DateTimeField(label="Fim", input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Reserve
        fields = ['start', 'end', 'state']


class EditReserveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditReserveForm, self).__init__(*args, **kwargs)

        self.fields['start'].widget.attrs['class'] = 'form-control'
        self.fields['end'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'

    start = forms.DateTimeField(label="Inicio", 
                                input_formats=['%d/%m/%Y %H:%M'],
                                required=False,
                                widget=forms.TextInput(attrs={'disabled': 'disabled'}))
    end = forms.DateTimeField(label="Fim", 
                                input_formats=['%d/%m/%Y %H:%M'],
                                required=False,
                                widget=forms.TextInput(attrs={'disabled': 'disabled'}))


    class Meta:
        model = Reserve
        fields = ['start', 'end', 'state']


class FilterReserveForm(forms.Form):
    start = forms.DateTimeField(label="Inicio", 
                                input_formats=['%d/%m/%Y %H:%M'],
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    end = forms.DateTimeField(label="Fim", 
                              input_formats=['%d/%m/%Y %H:%M'],
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
