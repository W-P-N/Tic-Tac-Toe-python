import numpy as np
from ui import UI
from logic import LoginFunctions as Logic


u_i = UI()

u_i.show_welcome()

l = Logic()


# TODO: Declare zero matrix.
# TODO: Let user choose Multiplayer or with computer.

game_running = True

while game_running:
    usr_ch = int(input("\n\nChoose one of the following.\nType:\n1 to play multiplayer game\n2 to play with computer\n0 to exit\n\nYour choice:"))

    if usr_ch == 1:
        mul_usr_game = True
        while mul_usr_game:
            # Taking name of the users:
            u_1 = input("\nEnter the name of player_1: ")
            if u_1 == "" or u_1 == " ":
                u_1 = "player_1"
            u_2 = input("\nEnter the name of player_2: ")
            if u_2 == "" or u_1 == " ":
                u_2 = "player_2"
            
            if u_1 == u_2:
                u_1 = "player_1"
                u_2 = "player_2"

            if l.multiplayer_game(p_1=u_1, p_2=u_2):
                print("\nHere we go again!")
            else:
                mul_usr_game = False


    elif usr_ch == 2:
        cmp_usr_game = True
        while cmp_usr_game:
            # Taking name of the users:
            u_1 = input("\nEnter the name of player: ")
            if u_1 == "" or u_1 == " ":
                u_1 = "player"
            
            cor_sym = True
            while cor_sym:
                try:
                    p_sym = int(input("\nChoose the symbol:\nType:\n1 - 'X'\n2 - 'O'\nYour choice: "))
                except ValueError:
                    print("\nPlease enter a number.")
                    continue
                if p_sym == 1 or p_sym == 2:
                    if p_sym == 1:
                        p_sym = 'X'
                    else:
                        p_sym = 'O'
                    cor_sym = False
                else:
                    print("\nInvalid input. Please enter a valid choice.")
                    cor_sym = True

            if l.computer_game(p_1=u_1, sym=p_sym):
                print("\nHere we go again!")
            else:
                print("\nThank you for playing the game!")
                cmp_usr_game = False
                
    elif usr_ch == 0:
        game_running=False
    else:
        print("\n\nInvalid input. Please enter a valid choice.")

# TODO: Multiplayer Game - 
## Ask user to choose symbol.
## Ask user to enter the symbol at place (number convention or direct?)
## Check position validity.
## Check win condition
## Ask another user to enter the symbol.
## Check position validity.
## Check win condition.
# TODO: Computer Game -
## Ask user to choose symbol.
## Ask user to enter the symbol at place (number convention or direct?)
## Check position validity.
## Check win condition.
## Computer choose symbol
## Check position validity.
## Check win condition.
