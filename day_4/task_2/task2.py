import requests, json

github_username = "Surajtalwar"
repo_name = "Python-tasks"
# API url to grab user data
request = f'https://api.github.com/repos/{github_username}/{repo_name}'

# send get request
response = requests.get(request)
# print("Status code :", response.status_code)
# print("Headers content-type :", response.headers['content-type'])

data = response.json()
data = sorted(data.items())
# print(data)
for i in data:
    print(f"* {i[0]}: {i[1]}")