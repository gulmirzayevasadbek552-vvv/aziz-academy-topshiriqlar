emails = input().split()
d = {email.split('@')[1].lower() for email in emails if '@' in email}
if d:
    print(' '.join(sorted(d)))
else:
    print("BO'SH")