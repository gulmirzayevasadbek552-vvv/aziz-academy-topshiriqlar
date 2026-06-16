n = int(input())
for i in range(n):
    na, f = input().split()
    s = "present" if f == "1" else "absent"
    print(f"{na}|{s}")