import random

class Validation:
    @staticmethod
    def input(num):
        try:
            int(num)
            return True
        except ValueError:
            print("input integral value")
            return False

    @staticmethod
    def inputMax(min, max):
        try:
            if min < max:
                return True
        except ValueError:
            print("input number larger than minimum")
            return False
    
    @staticmethod
    def inputGuess(min, max, guess):
        try:
            if min <= guess and guess <= max:
                return True
        except ValueError:
            print("input number larger than minimum and smaller than maximum")

def inputMin():
    min = input("input minimum number: ")
    if not Validation.input(min):
        return inputMin()
    return int(min)


def inputMax(min):
    min = int(min)
    max = input("input maximum number: ")
    if not Validation.input(max): return inputMax(min)
    if not Validation.inputMax(min, int(max)): inputMax(min)
    return int(max)

def inputGuess(min, max):
    min, max = int(min), int(max)
    guess = input("input guess number: ")
    if not Validation.input(guess): return inputGuess(min, max)
    if not Validation.inputGuess(min, max, int(guess)): return inputGuess(min, max)
    return int(guess)

def getAnswer(min, max):
    return random.randint(min, max)

def guessTheNumber(min, max, answer):
    try_times = 3

    for i in range(try_times):
        guess = inputGuess(min, max)
        if guess == answer:
            print("Great!!")
            return
        else:
            print("No...")

    print("Game over")

def main():
    min = inputMin()
    max = inputMax(min)
    answer = getAnswer(min, max)
    guessTheNumber(min, max, answer)

if __name__ == "__main__":
    main()
