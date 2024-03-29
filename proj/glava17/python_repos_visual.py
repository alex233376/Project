import requests

from plotly.graph_objects import Bar
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Обработка результатов.
reesponse_dict = r.json()
repo_dicts = reesponse_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# Построение визуализации.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Самые популярные проекты Python на GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Репозитории',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {'title': 'Звёзды',
              'titlefont': {'size': 14},
              },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
