def find_captured_pawn(board: list[int], n: int, player: int, selected_index):
    opponent_pawn = 2 if player == 1 else 1
    to_capture = []

    # check pawn's right side
    right_captured = []
    pawn_to_check = selected_index + 1
    while pawn_to_check < n and board[pawn_to_check] == opponent_pawn:
        right_captured.append(pawn_to_check + 1)
        pawn_to_check += 1

    if pawn_to_check >= n or (pawn_to_check < n and board[pawn_to_check] == player):
        to_capture.extend(right_captured)

    # check pawn's left side
    left_captured = []
    pawn_to_check = selected_index - 1
    while pawn_to_check >= 0 and board[pawn_to_check] == opponent_pawn:
        left_captured.append(pawn_to_check + 1)
        pawn_to_check -= 1

    if pawn_to_check < 0 or (pawn_to_check >= 0 and board[pawn_to_check] == player):
        to_capture.extend(left_captured)

    return to_capture
