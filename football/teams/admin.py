from django.contrib import admin

# Register your models here.
from football.teams.models import Team

admin.site.register(Team)