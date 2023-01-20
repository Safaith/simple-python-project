import random


# def guess(x):
#     random_integer = random.randint(1, x)
#     guess = 0

#     while guess != random_integer:
#         guess = int(input("guess the number integer betweeen 1 to 10: "))
#         if guess < random_integer:
#             print("sorry, your guess is too low, try again!")
#         elif guess > random_integer:
#             print("sorry, your guess is too high,guess again")
#     print("congratulations! you guess right.")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        cguess = random.randint(low, high)
        feedback = input(
            f"is the value {cguess} is high(h),low(l) or correct(c): ")
        if feedback == 'l':
            low = cguess + 1
        elif feedback == 'h':
            high = cguess - 1

    print("congrats! you guess correctly.")


computer_guess(10)


# guess(10)
