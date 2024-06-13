
# imports random lib
import random

# Variable setting
num = random.randint(1, 100)
response = ''
lives = 5

# While loop which prints lives and outcome.
while response != num and lives > 0:
    print(f"You have {lives} attempts")
    response = int(input("Enter your guess: "))

# incorrect number given
    if response >= 51:
        print("Please insert a Number between 1 and 50")
# correct response outcome
    elif response == num:
        print(f"You got it!! The number is {num}")
# response is too high outcome
    elif response > num:
        print("Your guess is too high")
        lives -= 1
# response is too low outcome
    else:
        print("Your guess is too low")
        lives -= 1
# if lives run out outcome is given.
if lives == 0:
    print(f"GAME OVER! No more attempts, the number to guess was {num}")