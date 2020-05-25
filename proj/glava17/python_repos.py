import requests

# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Сохранение ответа API в переменной.
reesponse_dict = r.json()
print(f"Все репозитории: {reesponse_dict['total_count']}")
# Анализ информации о репозиториях.
repo_dicts = reesponse_dict['items']
print(f'Найденные репозитории: {len(repo_dicts)}')

# Анализ первого репозитория.
repo_dict = repo_dicts[0]
# print(f'\nКлюч: {len(repo_dict)}')
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\nСобираем инфу из первого репозитория ")
print(f"Имя: {repo_dict['name']}")
print(f"Владелец: {repo_dict['owner']['login']}")
print(f"Звёзды: {repo_dict['stargazers_count']}")
print(f"Репозиторий: {repo_dict['html_url']}")
print(f"Создан: {repo_dict['created_at']}")
print(f"Обновлён: {repo_dict['updated_at']}")
print(f"Описание: {repo_dict['description']}")
