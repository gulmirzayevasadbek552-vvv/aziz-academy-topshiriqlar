text = input().strip()
char = input().split()[0]
if char in text:
    print(0)
else:
    print(-1)