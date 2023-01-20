import random


def play():
    user = input('enter rock(r) or paper(p) or scissor(s): ')
    computer = random.choice(['r', 's', 'p'])
    print(computer)
    if user == computer:
        return 'its tie'
    if is_win(user, computer):
        return 'you won'
    return 'you lost'


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())
