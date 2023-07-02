import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper:"Paper", scissors:"Scissors"}
rules = {rock: scissors, paper:rock, scissors:paper}

human_score = 0
computer_score = 0

def start():
    print("The Game is Rock, Paper, Scissors (you know the drill)")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)

    if player not in (1,2,3):
        print("I didn't understand that. Please enter 1, 2, or 3.")
        return play_again()
    else:
        result(player, computer)
        return play_again()

def move():
    player_move = input("Rock = 1\nPaper = 2\nScissors = 3\nShoot: ")

    try:
        player_move = int(player_move)
        if player_move in (1,2,3):
            return player_move
    except ValueError:
        pass

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!!")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global human_score, computer_score
    if player == computer:
        print("TIE!")
    else:
        if rules[player] == computer:
            print("You won that round")
            human_score += 1
        else:
            print("Hahaha I won the round, silly human")
            computer_score +=1

def play_again():
    loop = True

    while loop:
        answer = input("Would you like to play again? Y/N: ")

        if answer in ['y', 'Y', 'Yes', 'yes']:
            loop = False
            return 1
        elif answer in ['n', 'N', 'No', 'no']:
            loop = False
            print("\nThanks for playing!!! See you next time!")
            return 0
        else:
            print("I didn't understand that, please respond \'Y\' or \'N\'")

def scores():
    global human_score, computer_score
    print("HIGH SCORES\nPlayer: " + str(human_score) + "\nComputer: " + str(computer_score))

if __name__ == "__main__":
    start()