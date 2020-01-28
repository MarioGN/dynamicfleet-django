from django.db import models
from dynamicfleet.veiculos.validators import validate_license, validate_year


class Vehicle(models.Model):

    STATE_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
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
                             max_length=2, 
                             choices=STATE_CHOICES, 
                             default='SP')

    created = models.DateTimeField('Registrado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'

    def __str__(self):
        return '{} - {}'.format(self.model, self.license_plate)
