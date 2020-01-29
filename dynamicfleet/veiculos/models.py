from django.db import models
from dynamicfleet.veiculos.validators import validate_license, validate_year


class Vehicle(models.Model):

    STATES_CHOICES = [
        ('disponivel', 'Disponível'),
        ('manutencao', 'Manutenção')
    ]

    model = models.CharField('Modelo', max_length=128)
    license_plate = models.CharField('Placa', 
                                      max_length=7, 
                                      unique=True, 
                                      validators=[validate_license])
    year = models.PositiveIntegerField('Ano', 
                                        validators=[validate_year],
                                        default=2020)
    state = models.CharField('Estado', 
                              max_length=10, 
                              choices=STATES_CHOICES, 
                              default='disponivel')

    created = models.DateTimeField('Registrado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'

    def __str__(self):
        return '{} - {}'.format(self.model, self.license_plate)
