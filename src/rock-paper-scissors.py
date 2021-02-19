import random

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a tie'

    #r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
         or (player == 'p' and opponent == 'r'):
         return True
        
print(play())