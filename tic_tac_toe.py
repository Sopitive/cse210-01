#Wyatt Moore Tic-Tac-Toe assignment


def main():
    print("Here is your play area.")
    init_interface()
    won = False
    count = 0
    while True:
        print("Player 1: To select a square, type the number that corresponds to the square you want to select.")
        player_one()
        count += 1
        if count == 9:
            print("It is a tie.")
            break
        won = check_win()
        if won: break
        print("Player 2: To select a square, type the number that corresponds to the square you want to select.")
        player_two()
        count += 1
        if count == 9:
            print("It is a tie.")
            break
        won = check_win()
        if won: break

def player_one(): 
    selection = int(input("Select the number that corresponds to the square you want to select: "))
    for i in range(3):
        print()
        for x in range(3):
            square = x+i*3
            if square != selection:
                print(f"_|_{played_squares[square]}_|_", end="")
            else: 
                played_squares[square] = "x"
                print(f"_|_{played_squares[square]}_|_", end="")
    print()


def check_win(): 
    if played_squares[0] == played_squares[1] == played_squares[2]: #across top
        print("Game Over")
        return True
    elif played_squares[3] == played_squares[4] == played_squares[5]: #across middle
        print("Game Over")
        return True
    elif played_squares[6] == played_squares[7] ==played_squares[8]: #across bottom
        print("Game Over")
        return True
    elif played_squares[0] == played_squares[3] == played_squares[6]: #down left
        print("Game Over")
        return True
    elif played_squares[2] == played_squares[5] == played_squares[8]: #down right
        print("Game Over")
        return True
    elif played_squares[1] == played_squares[4] == played_squares[7]: #down middle
        print("Game Over")
        return True
    elif played_squares[0] == played_squares[4] == played_squares[8] : #diaganol left-right
        print("Game Over")
        return True
    elif played_squares[2] == played_squares[4] == played_squares[6]: #diaganol right-left
        print("Game Over")
        return True
    else: #If no condition is met, game continues.
        return False
    
        
def player_two(): 
    selection = int(input("Select the number that corresponds to the square you want to select: "))
    for i in range(3):
        print()
        for x in range(3):
            square = x+i*3
            if square != selection:
                print(f"_|_{played_squares[square]}_|_", end="")
            else: 
                played_squares[square] = "o"
                print(f"_|_{played_squares[square]}_|_", end="")

def init_interface(): 
    for i in range(3):
        print()
        for x in range(3):
            print(f"_|_{x+i*3}_|_", end="")
    print()


if __name__ == '__main__':
    print("Welcome to the tic-tac-toe program!")
    played_squares = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    main()


