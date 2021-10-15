from django.urls import path

from football.teams.views import ListTeamsView, CreateTeamView, MatchesDetailsView

urlpatterns = [
    path('', CreateTeamView.as_view(), name='create team'),
    path('list/', ListTeamsView.as_view(), name='list teams'),
    path('matches/', MatchesDetailsView.as_view(), name='list matches')
]