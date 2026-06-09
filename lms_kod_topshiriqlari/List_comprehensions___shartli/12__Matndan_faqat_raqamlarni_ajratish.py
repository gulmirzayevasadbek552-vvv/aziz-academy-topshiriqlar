s = input()
natija = [ch for ch in s if ch.isdigit()]
if natija:
    print("".join(natija))
else:
    print("BO'SH")