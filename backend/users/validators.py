from rest_framework.exceptions import ValidationError


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            'Запрещено имя "me", придумайте другое имя!'
        )
    return value
