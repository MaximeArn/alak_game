from alak_capture import *


def display_board(board: list[int]) -> None:
    board_str = ""
    numbers_str = ""
    for i, n in enumerate(board):
        numbers_str += str(i + 1) + " "
        variable_space = " " if i < 9 else "  "  # for large boards
        if n == 0:
            board_str += "." + variable_space
        elif n == 1:
            board_str += "x" + variable_space
        else:
            board_str += "o" + variable_space
    print("\n\n\t", "| ", board_str, "|")
    print("\t", "| ", numbers_str, "|\n\n")


def is_possible(
    board: list[int],
    n: int,
    removed: list[int],
    selected_pos: int,
    disp_logs: bool = True,
) -> bool:
    # disp_logs avoid logs printing during again
    if selected_pos in removed:
        if disp_logs:
            print(" \t this position was captured at previous round ")
        return False
    if selected_pos > n or selected_pos <= 0:
        print("\tnot in board")
        return False
    if board[selected_pos - 1] != 0:
        if disp_logs:
            print("\t there is already a pawn in position ", selected_pos)
        return False
    return True


def select(
    board: list[int],
    n: int,
    player: int,
    removed: list[int],
) -> int:
    print("Joueur ", str(player))
    selected_pos = int(input("Choose a position : "))
    while not is_possible(board, n, removed, selected_pos):
        selected_pos = int(input("Choose a valid position : "))
    return selected_pos


def play_pawn(
    board: list[int],
    n: int,
    player: int,
    removed: list[int],
    selected_pos: int,
) -> None:
    board[selected_pos - 1] = 1 if player == 1 else 2
    to_capture = find_captured_pawn(board, n, player, selected_pos - 1)
    for pawn_pos in to_capture:
        board[pawn_pos - 1] = 0
    removed.clear()
    removed.extend(to_capture)


def again(
    board: list[int],
    n: int,
    removed: list[int],
) -> bool:
    possibilities = []
    for i in range(1, n + 1):
        possibilities.append(is_possible(board, n, removed, i, False))
    return True in possibilities
