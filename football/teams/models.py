from django.db import models

from football.teams.validators import validate_text_starts_with_capital, validate_text_consists_only_of_letters


class Team(models.Model):
    name = models.CharField(
        max_length=20,
        validators=[validate_text_starts_with_capital, validate_text_consists_only_of_letters,]
    )

