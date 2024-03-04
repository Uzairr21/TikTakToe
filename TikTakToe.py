import random

def draw_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def input_player_letter():
    letter = ""
    while letter not in ["X", "O"]:
        letter = input("Do you want to be X or O? ").upper()
    return ["X", "O"] if letter == "X" else ["O", "X"]

def who_goes_first():
    return "computer" if random.randint(0, 1) == 0 else "player"

def play_again():
    return input("Do you want to play again? (yes or no) ").lower().startswith("y")

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    return any(
        [all(bo[i] == le for i in line) for line in [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]]
    )

def is_board_full(board):
    return all(x != ' ' for x in board[1:])

def get_player_move(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not is_space_free(board, int(move)):
        move = input("What is your next move? (1-9) ")
    return int(move)

def get_computer_move(board, computer_letter):
    player_letter = "O" if computer_letter == "X" else "X"

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if is_space_free(board, 5):
        return 5

    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_space_free(board, move):
    return board[move] == " "

def choose_random_move_from_list(board, moves_list):
    possible_moves = [move for move in moves_list if is_space_free(board, move)]
    return random.choice(possible_moves) if possible_moves else None

def get_board_copy(board):
    return board[:]

def play_tic_tac_toe_game():
    print("Welcome to Tic Tac Toe!")
    while True:
        the_board = [" "] * 10
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print(f"The {turn} will go first.")
        game_is_playing = True

        while game_is_playing:
            if turn == "player":
                draw_board(the_board)
                move = get_player_move(the_board)
                make_move(the_board, player_letter, move)

                if is_winner(the_board, player_letter):
                    draw_board(the_board)
                    print("Hooray! You have won the game!")
                    game_is_playing = False
                elif is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
            else:
                move = get_computer_move(the_board, computer_letter)
                make_move(the_board, computer_letter, move)

                if is_winner(the_board, computer_letter):
                    draw_board(the_board)
                    print("The computer has beaten you! You lose.")
                    game_is_playing = False
                elif is_board_full(the_board):
                    draw_board(the_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

        if not play_again():
            break

# Run the game
play_tic_tac_toe_game()
 