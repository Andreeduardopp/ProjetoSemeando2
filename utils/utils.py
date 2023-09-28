from django.core.exceptions import ValidationError


def valida_telefone(phone_number):
   
    if len(phone_number) < 9:
        raise ValidationError('Número de celular muito curto')
    elif len(phone_number) > 12:
        raise ValidationError('Número de celular muito longo')



