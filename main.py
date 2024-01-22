from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Funcion to check user check with actual answer
def check_answer(guess, answer, turns):
    '''check answer against guess. Returns number of turns remaining'''
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

print(logo)

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    #We need to define difficulty
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS


    #We need to select a random number
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        #Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

        print(f"You have {turns} attempts remaining to guess the number.")

    #Track the number of turns and reduce by 1 if they get it wrong

    #Repete the guessing funtionlity if they get it wrong.

game()

