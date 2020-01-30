from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from dynamicfleet.reservas.validators import validate_start_date


class Reserve(models.Model):
    STATES_CHOICES = [
        ('provisoria', 'Provisória'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ]

    vehicle = models.ForeignKey("veiculos.Vehicle", 
                                on_delete=models.CASCADE, 
                                related_name='reserves')
    start = models.DateTimeField('Inicio', 
                                 default=datetime.now, 
                                 validators=[validate_start_date])
    end = models.DateTimeField('Fim', default=datetime.now,)
    state = models.CharField('Estado da Reserva', 
                              max_length=10, 
                              choices=STATES_CHOICES, 
                              default='provisoria')

    created = models.DateTimeField('Registrado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def clean(self):
        super(Reserve, self).clean()
        
        if self.start > self.end:
            raise ValidationError('Data de fim da reserva inválida.', 'invalid value')

    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'

    def __str__(self):
        return '[ veiculo: {}, start: {}, end: {}, state: {}]'.format(
            self.vehicle.model,
            self.start,
            self.end,
            self.state)
