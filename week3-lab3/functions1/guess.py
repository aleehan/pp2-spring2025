import random

print("Hello! What is your name?")
name = input("Write your name: ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
# number = int(input())

behavior = True
rundomnum = random.randint(1, 20)
guesses = 0
while behavior == True:
    number = int(input())
    if number < rundomnum:
        guesses+=1
        print("Your guess is too low.")
    elif number > rundomnum:
        print("Your guess is too high.")
        guesses+=1
    else:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        behavior = False
