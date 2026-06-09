n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
all_tags = set()
for user in users:
    all_tags.update(user['tags'])
print(len(all_tags))