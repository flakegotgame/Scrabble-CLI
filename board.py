def create_board():
    """Creates a 15x15 Scrabble board."""
    return [[" " for _ in range(15)] for _ in range(15)]

def append_special_tiles(board):
    SPECIAL_TILES = {
        "DL": [(1, 2), (2, 1), (3, 2), (2, 3), (1, 12), (2, 13), (3, 12), (2, 11), (12, 1), (13, 2), (12, 3), (11, 2), (12, 13), (13, 12), (12, 11), (11, 12)],
        "TL": [(0, 6), (0, 8), (2, 6), (2, 8), (3, 7), (6, 0), (6, 14), (8, 0), (8, 14), (12, 6), (12, 8), (14, 6), (14, 8), (7, 3), (7, 11)],
        "DW": [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13),(9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)],
        "TW": [(0, 0), (0, 14), (7, 0), (7, 14), (14, 0), (14, 14)],
        "*": [(7, 7)]
    }
    for tile_type, positions in SPECIAL_TILES.items():
        for row, col in positions:
            board[row][col] = tile_type
         
    print("\nDebug: Special tiles added to the board.")  # Debugging line  
    return board

def print_board(board):
    """Prints the board in a readable format."""
    print("    " + " "+"   ".join(f"{i:2}" for i in range(15)))
    print("   " + "-" * 76)
    for i, row in enumerate(board):
        print(f"{i:2} | " + " | ".join(f"{cell:2}" if len(cell) == 1 else f"{cell}" for cell in row) + " |")
        print("   " + "-" * 76)


def place_word(board, word, start_row, start_col, direction):
    """
    Places a word on the board.
    direction: 'H' for horizontal, 'V' for vertical
    """
    if direction == "H":
        for i, letter in enumerate(word):
            board[start_row][start_col + i] = letter
    elif direction == "V":
        for i, letter in enumerate(word):
            board[start_row + i][start_col] = letter

def is_valid_move(board, word, start_row, start_col, direction):
    """
    Validates if the word can be placed on the board.
    Returns True if valid, False otherwise.
    """
    print(f"Debug: Validating move for '{word}' at ({start_row}, {start_col}) going {direction}")
    
    if direction == "H":
        if start_col + len(word) > 15:
            print("Debug: Word goes out of horizontal bounds.")
            return False
        for i, letter in enumerate(word):
            current_cell = board[start_row][start_col + i]
            # Allow placement on empty spaces or special tiles
            if current_cell not in (" ", "DL", "TL", "DW", "TW", "*", letter):  
                print(f"Debug: Cell conflict at ({start_row}, {start_col + i}). Cell: '{current_cell}', Letter: '{letter}'")
                return False
    elif direction == "V":
        if start_row + len(word) > 15:
            print("Debug: Word goes out of vertical bounds.")
            return False
        for i, letter in enumerate(word):
            current_cell = board[start_row + i][start_col]
            if current_cell not in (" ", "DL", "TL", "DW", "TW", "*", letter):
                print(f"Debug: Cell conflict at ({start_row + i}, {start_col}). Cell: '{current_cell}', Letter: '{letter}'")
                return False
    return True

if __name__ == "__main__":
    board = create_board()
    board = append_special_tiles(board)
    print_board(board)
    
    word = "HELLO"
    start_row, start_col = 7, 7
    direction = "H"
    
    if is_valid_move(board, word, start_row, start_col, direction):
        place_word(board, word, start_row, start_col, direction)
    else:
        print("Invalid move")
    
    print_board(board)
