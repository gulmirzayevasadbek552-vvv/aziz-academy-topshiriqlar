s1 = input().strip().lower().split()
s2 = input().strip().lower().split()

unique_words = set(s1) | set(s2)

print(len(unique_words))