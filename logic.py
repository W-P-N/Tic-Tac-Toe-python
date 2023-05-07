import numpy as np
import random as r
from ui import UI
import time as t

interface = UI()

class LoginFunctions:

    def __init__(self):
        self.game_board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    

    def check_pos(self, pos):
        for i in range(0, 3):
            for j in range(0, 3):
                if pos == self.game_board[i][j]:
                    return False
        
        return True

    def get_player(self, p_1, p_2):
        if r.randint(0, 1) == 1:
            return p_1
        else:
            return p_2
    

    def computer_game(self, p_1, sym):
        """This function is the brain of the computer game"""

        if sym == 'X':
            cmp_sym = 'O'
        else:
            cmp_sym = 'X'

        # Choose the first player to play logic:
        if r.randint(0, 1) == 1:
            turn = True
        else:
            turn = False

        self.get_board()

        win = False

        while not self.game_board_full() and not win:

            if turn:
                print("\nComputer Turn .")
                for i in range(0, 7):
                    t.sleep(0.5)
                    print(".")
                self.computer_turn(c_sym=cmp_sym)
                if self.check_win():
                    interface.show_congratulations()  # Show congratulations message.
                    print(f"\n{'Computer' if turn is True else p_1}. You won the game!!")
                    win = True  # Break out of the multiplayer game loop.
                    self.game_board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])  # Reset the board.
            else:
                usr_trn = True
                while usr_trn:
                    try:
                        u_ch = int(input(f"\n{p_1} your turn. Enter the number where you want to play your move:  "))
                    except ValueError:
                        print("\nPlease enter a number.")
                        continue

                    check_validated = self.checks(pos=u_ch, sym=sym)

                    if check_validated:
                        if self.check_win():
                            interface.show_congratulations()  # Show congratulations message.
                            print(f"\n{'Computer' if turn is True else p_1}. You won the game!!")
                            win = True  # Break out of the multiplayer game loop.
                            self.game_board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])  # Reset the board.
            
                        usr_trn = False
            turn = not turn

        if self.game_board_full():
            print("\nIt's a tie.")
            self.game_board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])  # Reset the board.

        ch_run = True

        while ch_run:
            resp = input("\nDo you want to play the with computer again?\nType \n'y' to continue\n'n' to return to main menu.\nYour choice: ")
            if resp == 'y':
                return True
            elif resp == 'n':
                return False
            else:
                print("\nInvalid input!")
            




    def computer_turn(self, c_sym):

        # Check the correctness of the random number chosen by computer.
        corr_pos = False

        while not corr_pos:
            cmp_ch = r.randint(1, 10)
            if 1<=cmp_ch<=3:
                if self.check_pos(cmp_ch):
                    self.game_board[0][cmp_ch-1] = c_sym
                    self.get_board()
                    corr_pos = True
            elif 4<=cmp_ch<=6:
                if self.check_pos(cmp_ch):
                    self.game_board[1][cmp_ch-4] = c_sym
                    self.get_board()
                    corr_pos = True
            elif 7<=cmp_ch<=9:
                if self.check_pos(cmp_ch):
                    self.game_board[2][cmp_ch-7] = c_sym
                    self.get_board()
                    corr_pos = True


    
    def multiplayer_game(self, p_1, p_2):
        """This function is the brain of multiplayer game."""

        # Choose the first player to play logic:
        if r.randint(0, 1) == 1:
            turn = True
        else:
            turn = False
        
        # Show the Tic-Tac-Toe board.
        self.get_board()

        # win confition.
        win = False

        # Game Begins:
        while not self.game_board_full() and not win:

            # Give turn to player.
            re_q = True  # To maintain answer correctness.
            if turn == True:
                while re_q:
                    try:
                        u_ch =  int(input(f"\n{p_1} your turn. Enter the number where you want to play your move:  "))
                    except ValueError and UnboundLocalError as e:
                        print("\nPlease enter a number!")
                    else:
                        if u_ch in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            re_q = False
                        else:
                            print("\nInvalid number!")
            else:
                while re_q:
                    try:
                        u_ch =  int(input(f"\n{p_2} your turn. Enter the number where you want to play your move:  "))
                    except ValueError:
                        print("\nPlease enter a number!")
                    else:
                        if u_ch in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            re_q = False
                        else:
                            print("\nInvalid number!")
            
            # Write changes on the board after passing of all the checks.
            if turn == True: 
                check_validated = self.checks(pos=u_ch, sym='X')
            else: 
                check_validated = self.checks(pos=u_ch, sym='O')

            # Check if there is a winner.
            if self.check_win():
                interface.show_congratulations()  # Show congratulations message.
                print(f"\n{p_1 if turn is True else p_2}. You won the game!!")
                win = True  # Break out of the multiplayer game loop.
                self.game_board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])  # Reset the board.
            else:
                if check_validated:  # Check if all the checks are validated.
                    turn = not turn  # Switch turns if checks are validated.
                else:
                    turn = turn  # Keep the same turn.
            

            # Tie condition.
            if self.game_board_full():
                print("\nIt's a tie.")
                self.game_board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])  # Reset the board.


        ch_run = True

        while ch_run:
            resp = input("\nDo you want to play the multiplayer game again?\nType \n'y' to continue\n'n' to return to main menu.\nYour choice: ")
            if resp == 'y':
                return True
            elif resp == 'n':
                return False
            else:
                print("\nInvalid input!")



    def game_board_full(self):
        for i in range(0, 3):
            for j in range(0, 3):
                for val in range(1, 10):
                    if str(val) == self.game_board[i][j]:
                        return False

        return True
                

    
    def check_pos(self, pos):
        for i in range(0, 3):
            for j in range(0, 3):
                if str(pos) == self.game_board[i][j]:
                    return True
        
        return False
    

    def get_board(self):
        print("\n\n")
        print(f"            |            |            ")
        print(f"    {self.game_board[0][0]}       |      {self.game_board[0][1]}     |      {self.game_board[0][2]}     ")
        print(f"____________|____________|____________")
        print(f"            |            |            ")
        print(f"     {self.game_board[1][0]}      |      {self.game_board[1][1]}     |      {self.game_board[1][2]}     ")
        print(f"____________|____________|____________")
        print(f"            |            |            ")
        print(f"     {self.game_board[2][0]}      |      {self.game_board[2][1]}     |      {self.game_board[2][2]}     ")
        print(f"            |            |            ")



    def check_win(self):
        if self.col_win() or self.row_win() or self.cross_win():
            return True
        return False
    
    
    def col_win(self):
        for i in range(0, 3):
            if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i]:
                return True
        return False


    def row_win(self):
        for i in range(0,3):
            if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2]:
                return True
        return False
    

    def cross_win(self):
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]:
            return True
        return False


    def checks(self, pos, sym):

        correct = False
        while not correct:

            if 1<=pos<=3:
                if self.check_pos(pos):
                    self.game_board[0][pos-1] = sym
                    self.get_board()
                else:
                    print("\nInvalid position")
                    return False
            elif 4<=pos<=6:
                if self.check_pos(pos):
                    self.game_board[1][pos-4] = sym
                    self.get_board()
                else:
                    print("\nInvalid position")
                    return False
            elif 7<=pos<=9:
                if self.check_pos(pos):
                    self.game_board[2][pos-7] = sym
                    self.get_board()
                else:
                    print("\nInvalid position")
                    return False
            else:
                print("\nInvalid position")
                return False
            correct = True

        return True
    

