from alak_utils import *


def new_board(n: int) -> list[int]:
    board = []
    for _ in range(n):
        board.append(0)
    return board


def alak(n: int):
    player = 1
    board = new_board(n)
    removed: list[int] = []
    while again(board, n, removed):
        display_board(board)
        selected_pos = select(board, n, player, removed)
        play_pawn(board, n, player, removed, selected_pos)
        player = 2 if player == 1 else 1
    display_board(board)
    print("Victoire : Player 1" if player == 2 else "Victoire : Player 2")


alak(9)
