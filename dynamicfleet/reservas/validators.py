import datetime
from django.core.exceptions import ValidationError


def validate_start_date(date):
    current_date = datetime.datetime.now()

    if date < current_date:
        raise ValidationError('Data de inicio da reserva inválida.', 'invalid value')
