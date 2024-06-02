import random
Jackpot = random.randint(1, 100)
guess = int(input("chal guess kar"))
counter = 1
while guess != Jackpot:
    if guess < Jackpot:
        print("guess higher ")
    else:
        print("guess Lower")

    guess = int(input("chal guess kar"))
    counter += 1
print("shai Jawab")
print("you took", counter, "attempts")