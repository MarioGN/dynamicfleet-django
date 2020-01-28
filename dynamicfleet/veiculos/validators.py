import re
import datetime
from django.core.exceptions import ValidationError


def validate_license(license):
    
    if len(license) != 7:
        raise ValidationError('Placa do veículo deve conter 7 letras e números.', 'length')

    pattern = re.compile('^[a-zA-Z]{3}[0-9]{4}$')
    if pattern.match(license) == None:
        raise ValidationError('A placa informada não é uma placa válida.', 'invalid value')

def validate_year(year):
    current_year = datetime.date.today().year

    if year < 1950 or year > current_year:
        raise ValidationError('O ano de fabricação informado não é válido.', 'invalid value')
