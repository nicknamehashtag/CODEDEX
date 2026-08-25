import random
print("welcome to the number guessing game")
a=random.randint(1,100)
b=int(input("guess a number between 1 and 100: "))
while b!=a:
    c=a-b
    print("your guess is wrong")
    print("the difference between your guess and the number is", c)

    b=int(input("guess again: "))
print("congratulations! you guessed the number", a)