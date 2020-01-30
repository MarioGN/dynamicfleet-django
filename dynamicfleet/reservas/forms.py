from django import forms
from django.core.exceptions import ValidationError
from dynamicfleet.reservas.models import Reserve


class ReserveForm(forms.ModelForm):
    
    class Meta:
        model = Reserve
        fields = ['start', 'end', 'state']