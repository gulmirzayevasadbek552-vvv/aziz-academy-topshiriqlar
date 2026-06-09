w = input().split()
unique_w = {word.lower() for word in w}
print(' '.join(sorted(unique_w)))