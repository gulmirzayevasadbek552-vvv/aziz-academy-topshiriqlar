ws = input().split()
f = {}
for w in ws:
    w = w.lower()
    if w in f:
        f[w] += 1
    else:
        f[w] = 1
t = len(ws)
u = len(f)
tw = ""
c = 0
for w in sorted(f):
    if f[w] > c:
        c = f[w]
        tw = w 
print(f"total: {t}")
print(f"unique: {u}")
print(f"top: {tw} {c}")