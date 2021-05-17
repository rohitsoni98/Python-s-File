import random
def guessGame(a, b, x):
    guess = int(input(f"Guess a number between {a} , {b}\n"))
    n_guess = 1
    while guess != x:
        if guess < x:
            guess = int(input(f"Enter a bigger number:\n"))
            n_guess += 1
        else:
            guess = int(input(f"Enter a smaller number:\n"))
            n_guess += 1

    print(f"you guessed the number in {n_guess} guesses\n")
    return n_guess


if __name__ == '__main__':
    a = int(input("Enter the value of a:\n"))
    b = int(input("Enter the value of b:\n"))

    x1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessGame(a, b, x1)

    x2 = random.randint(a, b)
    print("Player 2's turn\n")
    g2 = guessGame(a, b, x2)

    if g1 > g2:
        print("Player 1 won the match!\n ")

    elif g1 < g2:
        print("Player 2 won the match!\n")

    else:
        print("Its a Tie")

    print(f"The number of player 1 was {x1} and player 2 was {x2}!")

