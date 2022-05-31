import random

def play():
    user = input("Type Rock(r) or Paper(p) Scissor(s): ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie'

    if iswin(user, computer):
        return "You won"
    return "Computer won"


def iswin(player, opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True

print(play())