from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from football.teams.common import generate_matches
from football.teams.models import Team


class CreateTeamView(CreateView):
    model = Team
    template_name = 'create_team.html'
    success_url = reverse_lazy('list teams')
    fields = ('name',)

    def form_valid(self, form):
        team = form.save(commit=False)
        team.save()
        return super().form_valid(form)


class ListTeamsView(ListView):
    model = Team
    template_name = 'list_teams.html'
    context_object_name = 'teams'


class ListMatchesView(ListView):
    paginate_by = 1
    template_name ='list_matches.html'
    context_object_name = 'result'

class MatchesDetailsView(DetailView):
    def get(self, request, *args, **kwargs):
        result = generate_matches()
        context = {"result": result}
        return render(request, "list_matches.html", context)


class IndexView(DetailView):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")



