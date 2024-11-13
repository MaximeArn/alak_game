def find_captured_pawn(board: list[int], n: int, player: int, selected_index):
    to_capture = []

    # check pawns on right side
    right_captured = []
    pawn_to_check = selected_index + 1

    turns = 0
    while turns < n:
        if pawn_to_check == n:
            pawn_to_check = 0
        if board[pawn_to_check] == 0 or board[pawn_to_check] == player:
            break
        else:
            right_captured.append(pawn_to_check + 1)
            pawn_to_check += 1
        turns += 1

    if board[pawn_to_check] == player:
        to_capture.extend(right_captured)

    # check pawns on left side
    leftCaptured = []
    pawn_to_check = selected_index - 1

    turns = 0
    while turns < n:
        if board[pawn_to_check] == 0 or board[pawn_to_check] == player:
            break
        else:
            leftCaptured.append(pawn_to_check + 1)
            pawn_to_check -= 1
        turns += 1

    if board[pawn_to_check] == player:
        to_capture.extend(leftCaptured)

    return to_capture
