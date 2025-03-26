import json

with open ("users.json", "r") as f:
    users = f.read()
    json_data = json.loads(users)

with open ("users.json", "w") as f:
    user = {'name': 'admin', 'password': 'admin'}
    json_data.append({'name': 'juan', 'password': '123'})
    f.write(json.dumps(json_data))

    