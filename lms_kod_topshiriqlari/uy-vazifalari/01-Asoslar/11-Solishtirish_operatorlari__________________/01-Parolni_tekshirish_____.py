a = input()
print(a.isalnum() and a.islower() and any(c.isdigit() for c in a))