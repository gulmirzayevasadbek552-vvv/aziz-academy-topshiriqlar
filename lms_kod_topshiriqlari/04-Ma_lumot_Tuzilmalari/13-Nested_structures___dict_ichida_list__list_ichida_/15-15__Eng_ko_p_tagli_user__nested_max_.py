n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
max_user = users[0]
for user in users:
    if len(user['tags']) > len(max_user['tags']):
        max_user = user
print(max_user['username'])