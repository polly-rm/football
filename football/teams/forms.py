from django import forms

from football.teams.models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name',)
