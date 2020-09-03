import random

def dice_roller():
    dice_number = random.randint(1,6)
    return dice_number

def main():
    player_1 = 0
    player_2 = 0
    player_1Win = 0
    player_2Win = 0
    rounds = 1

    while rounds != 4:
        print("Round : " + str(rounds))
        player_1 = dice_roller()
        player_2 = dice_roller()
        print('player 1 roll is : ' + str(player_1))
        print('player 2 roll is : ' + str(player_2))
        if player_1 > player_2:
            print("player 1 win!")
            player_1Win += 1
        elif player_2 > player_1:
            print("player 2 win!")
            player_1Win += 1
        elif player_1 == player_2:
            print("the game is draw")
        rounds += 1
        if rounds < 4:
            print("__________________next round___________________\n")
    print("\nThe result is ")
    if player_1 > player_2:
        print(f"player 1 win! {player_1Win} times")
    elif player_2 > player_1:
        print(f"player 2 win!  {player_1Win} times")
    elif player_1 == player_2:
        print(f"the game is draw")

main()
        
