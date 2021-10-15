import datetime

from football.teams.models import Team


def generate_teams():
    return [team.name for team in Team.objects.all()]


def generate_date(f):
    today = datetime.date.today() + datetime.timedelta(days=f+1)
    return f'{today.day}.{today.month}.{today.year}'


def format_output(matches):
    teams = generate_teams()
    n = len(teams)
    matches_per_day_count = n//2
    result = []

    for i in range(n-1):
        day = []
        result.append(day)

        date = generate_date(i)
        day.append('Date:')
        day.append(date)
        day.append('Matches:')

        for k in range(matches_per_day_count):
            day.append(' <----> '.join(matches[i][k]))

    return result


def generate_matches():
    teams = generate_teams()
    n = len(teams)

    if n % 2 == 1:
        return

    matches_per_day_count = n // 2

    matches_per_day = []
    matches_total = []

    for _ in range(n-1):
        for i in range(matches_per_day_count):
            matches_per_day.append((teams[i], teams[n - 1 - i]))

        teams.insert(1, teams.pop())
        matches_total.insert(0, matches_per_day)
        matches_per_day = []

    result = format_output(matches_total)
    return result
