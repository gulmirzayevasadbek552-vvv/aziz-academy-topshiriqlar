n = int(input())
d = []
for _ in range(n):
    entry = input().split()
    d.append(entry)
x_limit = int(input())
result_dict = {}
for k, v in d:
    v_i = int(v)
    if v_i >= x_limit:
        result_dict[k] = v_i
print(result_dict)