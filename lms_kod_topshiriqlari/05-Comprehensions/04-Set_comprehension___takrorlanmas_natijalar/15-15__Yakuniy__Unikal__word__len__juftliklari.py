w = input().split()
paris = {(word.lower(), len(word)) for word in w}
print(len(paris))
sorted_paris = sorted(paris)
for word, lenght in sorted_paris:
    print(f"{word}:{lenght}")