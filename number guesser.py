import random

x = random.randint(1,100)
y = -1
while y != x:
    y = int(input("Guess the number between 1 and 100: "))
    if y > x:
        print("Too high")
    elif y < x:
        print("Too low")
print("Correct!")