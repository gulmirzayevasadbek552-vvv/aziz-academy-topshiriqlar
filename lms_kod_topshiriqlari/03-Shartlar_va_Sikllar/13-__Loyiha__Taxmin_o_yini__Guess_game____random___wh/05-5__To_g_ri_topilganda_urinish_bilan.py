t = 0
while True:
    try:
        line = input()
        if line.strip() != "":
            t += 1
    except EOFError:
            break
print(f"Correct in {t} tries")