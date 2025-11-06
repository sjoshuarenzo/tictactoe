def display_grid(grid):

    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print("---+---+---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print("---+---+---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y','N']:

        choice = input("Keep playing? (Y / N): ")

        if choice not in ['Y','N']:
            print("Sorry, I do not understand, please choose Y or N.")

    if choice == 'Y':
        return True
    else:
        return False

def place_tic(grid,player):
    
    position = int(input(f"{player} please choose a cell (1-9): "))
    
    row = (position - 1) // 3
    col = (position - 1) % 3

    if grid[row][col] != ' ':

        print("Choose an empty cell!")
        return player

    grid[row][col] = player

    return 'O' if player == 'X' else 'X'

def check_win(grid,player):

    filled = 0
    won = False

    for r in range(3):
        for c in range(3):
            if grid[r][c] != ' ':
                filled = filled + 1
                
    for row in grid:

        if len(set(row)) == 1 and row[0] == player:
            print(f"{player} wins")
            won = True

    for col in range(3):

        if grid[0][col] == player and grid[1][col] == player and grid[2][col] == player:
            print(f"{player} wins")
            won = True

    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        print(f"{player} wins")
        won = True
    elif grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        print(f"{player} wins")
        won = True

    if filled == 9 and won != True:
        print("Draw!")

game_on = True
grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player = 'X'

while game_on:

    display_grid(grid)

    current_player = player

    player = place_tic(grid,player)

    display_grid(grid)

    if check_win(grid,current_player):
        print(f"{current_player} wins!")
    
    game_on = gameon_choice()

    print("\n"*100)