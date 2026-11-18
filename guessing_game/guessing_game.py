import random

answer = random.randint(1, 10)

def run_guess(guess, answer):
    
    if 0 < guess < 11:
        if guess == answer:
            print("You are such a genius")
            return True
        else:
            return False
    else:
        print("I said 1-10, Dolozyy!")
        return False


if __name__ == "__main__":
    while True:
        try:
            guess = int(input("Guess a number 1-10: "))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print("Please enter a number")
            continue
