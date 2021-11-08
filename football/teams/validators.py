from django.core.exceptions import ValidationError


def validate_text_starts_with_capital(text):
    first_letter = text[0]
    if first_letter.islower():
        raise ValidationError('This field must start with a capital letter!')


def validate_text_consists_only_of_letters(text):
    if not text.isalpha():
        raise ValidationError('This field must consist only of letters!')