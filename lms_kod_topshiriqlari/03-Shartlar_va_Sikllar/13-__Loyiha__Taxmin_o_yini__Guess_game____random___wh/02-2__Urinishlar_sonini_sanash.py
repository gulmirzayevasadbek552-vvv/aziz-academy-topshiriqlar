secret = 5
attempts = 0
while True:
    guess = int(input())
    attempts += 1
    if guess == secret:
        break
print(attempts)