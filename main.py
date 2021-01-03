# Dict of length 9, Key here is for the move of playe. User can input any number and specific block in the board will be occupied according to user input
blocks = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}
keys = []

# Function to append keys in game board
for key in blocks:
    keys.append(key)


# Tnis function simply prints all the blocks of a board
def print_game_board(block):
    print(block['1'] + '|' + block['2'] + '|' + block['3'])
    print('-----')
    print(block['4'] + '|' + block['5'] + '|' + block['6'])
    print('-----')
    print(block['7'] + '|' + block['8'] + '|' + block['9'])


def game():
    player_turn = 'X'
    blocks_count = 0
    for i in range(10):
        print_game_board(blocks)
        # User will input number of block and if/else statement will check whether the block is available or not
        print("\nPlayer : " + player_turn + " Your Turn, Make a Move")
        player_input = input()
        if blocks[player_input] == ' ':
            blocks[player_input] = player_turn
            blocks_count += 1
        else:
            print("This already occupied by Opponent. Make a move again")
            continue

        # Now we will check which player won the game, player x or player o.
        # this if elif statements checks victory of player for every move after 5 moves
        if blocks_count >= 5:
            # first row blocks will be checked
            if blocks['7'] == blocks['8'] == blocks['9'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break
            # middle row blocks will be checked
            elif blocks['4'] == blocks['5'] == blocks['6'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break
            # last row blocks will be checked
            elif blocks['1'] == blocks['2'] == blocks['3'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break
                # Diagonal will be checked
            elif blocks['7'] == blocks['5'] == blocks['3'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break

            # Diagonal will be checked
            elif blocks['1'] == blocks['5'] == blocks['9'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break

                # first column blocks will be checked
            elif blocks['1'] == blocks['4'] == blocks['7'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break

            # middle column blocks will be checked
            elif blocks['2'] == blocks['5'] == blocks['8'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break

            # Last column blocks will be checked
            elif blocks['3'] == blocks['6'] == blocks['9'] != ' ':
                print_game_board(blocks)
                print("\nMatch Finished\n")
                print(" Congratulations " + player_turn + " You won the game")
                break

                # if no one wins
        if blocks_count == 9:
            print("\n***Game Over***\n Match Tied :)")

            # Players turn managment
        if player_turn == 'X':
            player_turn = 'O'
        else:
            player_turn = 'X'

    re_game = input("Another game (y/n)")
    if re_game == "y" or re_game == "Y":
        for key in keys:
            blocks[key] = " "
        game()


if __name__ == "__main__":
    game()
