
def mat():
    matrix = []
    steps = 0
    player = True
    winner = False
    for i in range(9):
        matrix.append(str(0))
    while steps<=9 and winner == False:
        print("", matrix[0], matrix[1], matrix[2], "\n", matrix[3], matrix[4], matrix[5], "\n", matrix[6], matrix[7], matrix[8])
        print("'x' for player 1, 'o' for player 2")
        if player:
            print("player1")
        else:
            print("player2")
        inp = int(input())
        if player:
            matrix[inp] = "x"
        else:
            matrix[inp] = "o"
        if (player == True and inp == "o") or (player == False and inp == "x"):
            print("invalid command")
        player = not player
        if (matrix[0] == matrix[3] == matrix[6] == "x"
            or matrix[1] == matrix[4] == matrix[7] == "x"
            or matrix[2] == matrix[7] == matrix[8] == "x"):
            print("player 1 wins")
            winner = True
        elif (matrix[0] == matrix[3] == matrix[6] == "o"
            or matrix[1] == matrix[4] == matrix[7] == "o"
            or matrix[2] == matrix[7] == matrix[8] == "o"):
            print("player 2 wins")
            winner = True
        if (matrix[0] == matrix[4] == matrix[8] == "x"
            or matrix[2] == matrix[4] == matrix[6] == "x"):
            print("player 1 wins")
            winner = True
        elif (matrix[0] == matrix[4] == matrix[8] == "o"
            or matrix[2] == matrix[4] == matrix[6] == "o"):
            print("player 2 wins")
            winner = True
        steps += 1
        if steps == 9:
            break
    print("game over")
if __name__ == '__main__':
    mat()
