m = input()
x = {'a', 'e', 'i', 'o', 'u'}
t = {char.lower() for char in m if char.lower() in x}
if t:
    print(' '.join(sorted(t)))
else:
    print("BO'SH")